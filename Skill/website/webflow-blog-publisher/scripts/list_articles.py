"""
List existing blog articles from Webflow CMS.

Used by the content-pipeline to review existing content before writing,
preventing topic overlap, SEO cannibalization, and duplicate imagery.

Usage:
    python scripts/list_articles.py
    python scripts/list_articles.py --published-only
    python scripts/list_articles.py --format json
"""

import os
import sys
import json
import argparse

# Reuse shared helpers from publish_to_webflow
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from publish_to_webflow import load_secrets, api_request


def fetch_all_items(token, collection_id):
    """Fetch all CMS items with pagination."""
    items = []
    offset = 0
    limit = 100
    while True:
        resp = api_request(
            "GET",
            f"/collections/{collection_id}/items?limit={limit}&offset={offset}",
            token,
        )
        if not resp or resp.status_code != 200:
            break
        data = resp.json()
        batch = data.get("items", [])
        items.extend(batch)
        total = data.get("pagination", {}).get("total", 0)
        offset += limit
        if offset >= total or not batch:
            break
    return items


def extract_article_info(item):
    """Extract key metadata from a CMS item."""
    fd = item.get("fieldData", {})
    raw_keywords = fd.get("primary-keywords", "")
    keywords = [k.strip() for k in raw_keywords.split(",") if k.strip()] if raw_keywords else []
    return {
        "id": item.get("id"),
        "title": fd.get("name", "Untitled"),
        "slug": fd.get("slug", ""),
        "primary_keyword": keywords[0] if keywords else "",
        "secondary_keywords": keywords[1:],
        "summary": fd.get("post-summary", fd.get("summary", fd.get("excerpt", ""))),
        "is_draft": item.get("isDraft", True),
        "created": item.get("createdOn", ""),
        "updated": item.get("lastUpdated", ""),
    }


def print_table(articles):
    """Print articles as a readable table."""
    print(f"\n{'#':<4} {'Status':<9} {'Title':<50} {'Primary Keyword':<35} {'Slug':<30}")
    print("-" * 130)
    for i, a in enumerate(articles, 1):
        status = "DRAFT" if a["is_draft"] else "LIVE"
        title = a["title"][:48] + ".." if len(a["title"]) > 50 else a["title"]
        keyword = a["primary_keyword"][:33] + ".." if len(a["primary_keyword"]) > 35 else a["primary_keyword"]
        slug = a["slug"][:28] + ".." if len(a["slug"]) > 30 else a["slug"]
        print(f"{i:<4} {status:<9} {title:<50} {keyword:<35} {slug:<30}")
    print(f"\nTotal: {len(articles)} articles")
    live = sum(1 for a in articles if not a["is_draft"])
    draft = len(articles) - live
    print(f"  Published: {live}  |  Drafts: {draft}")
    no_keyword = sum(1 for a in articles if not a["primary_keyword"])
    if no_keyword:
        print(f"  Missing primary keyword: {no_keyword}")


def print_json(articles):
    """Print articles as JSON for programmatic use."""
    print(json.dumps(articles, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(
        description="List existing blog articles from Webflow CMS"
    )
    parser.add_argument(
        "--published-only",
        action="store_true",
        help="Show only published (non-draft) articles",
    )
    parser.add_argument(
        "--format",
        choices=["table", "json"],
        default="table",
        help="Output format (default: table)",
    )
    parser.add_argument(
        "--collection_id",
        default=None,
        help="Override Webflow CMS collection ID",
    )
    args = parser.parse_args()

    secrets = load_secrets()
    token = secrets["token"]
    collection_id = args.collection_id or secrets["collection_id"]

    if not token or not collection_id:
        print("Error: WEBFLOW_API_TOKEN and WEBFLOW_BLOG_COLLECTION_ID required.")
        print("Add them to .env in the repository root. See .env.example.")
        return 1

    print(f"Fetching articles from collection {collection_id}...")
    raw_items = fetch_all_items(token, collection_id)
    articles = [extract_article_info(item) for item in raw_items]

    # Sort: published first, then by title
    articles.sort(key=lambda a: (a["is_draft"], a["title"].lower()))

    if args.published_only:
        articles = [a for a in articles if not a["is_draft"]]

    if args.format == "json":
        print_json(articles)
    else:
        print_table(articles)

    return 0


if __name__ == "__main__":
    sys.exit(main())
