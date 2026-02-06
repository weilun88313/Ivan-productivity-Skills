import os
import re
import json
import argparse
import time
import requests

try:
    import markdown
except ImportError:
    print("Missing dependency: pip install markdown")
    exit(1)

API_BASE = "https://api.webflow.com/v2"
MAX_RETRIES = 3
TIMEOUT = 30


SECRETS_PATH = os.path.expanduser("~/.claude/lensmor_secrets.json")


def load_secrets():
    """Load secrets from env vars, falling back to secrets file."""
    secrets = {}
    try:
        with open(SECRETS_PATH, "r") as f:
            secrets = json.load(f)
    except Exception:
        pass
    return {
        "token": os.environ.get("WEBFLOW_API_TOKEN") or secrets.get("WEBFLOW_API_TOKEN"),
        "collection_id": os.environ.get("WEBFLOW_BLOG_COLLECTION_ID") or secrets.get("WEBFLOW_BLOG_COLLECTION_ID"),
    }


def parse_blog_markdown(filepath):
    """Parse blog markdown into metadata and body content."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract title from first H1
    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled"

    # Extract slug
    slug_match = re.search(r"\*\*Slug\*\*:\s*(.+)", text)
    slug = ""
    if slug_match:
        raw_slug = slug_match.group(1).strip()
        # Take the last segment of the path
        slug = raw_slug.rstrip("/").split("/")[-1]

    # Extract meta description
    meta_match = re.search(r"\*\*Meta Description\*\*:\s*(.+)", text)
    meta_desc = meta_match.group(1).strip() if meta_match else ""

    # Extract body: everything after the first "---" divider
    parts = text.split("\n---\n", 1)
    body_md = parts[1].strip() if len(parts) > 1 else text

    # Remove local image references (user uploads manually)
    body_md = re.sub(r"!\[([^\]]*)\]\([^)]*\)\n?", "", body_md)

    # Convert markdown to HTML
    body_html = markdown.markdown(
        body_md,
        extensions=["tables", "fenced_code"],
    )

    return {
        "title": title,
        "slug": slug,
        "meta_description": meta_desc,
        "body_html": body_html,
    }


def api_request(method, endpoint, token, json_data=None):
    """Make a Webflow API request with retry logic."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept-Version": "2.0.0",
    }
    url = f"{API_BASE}{endpoint}"

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.request(
                method, url, json=json_data, headers=headers, timeout=TIMEOUT
            )

            if resp.status_code == 429:
                wait = int(resp.headers.get("Retry-After", 2 ** attempt))
                print(f"Rate limited, waiting {wait}s... ({attempt}/{MAX_RETRIES})")
                time.sleep(wait)
                continue

            if resp.status_code >= 500 and attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"Server error {resp.status_code}, retrying in {wait}s...")
                time.sleep(wait)
                continue

            return resp

        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}, attempt {attempt}/{MAX_RETRIES}")
            if attempt < MAX_RETRIES:
                time.sleep(2 ** attempt)

    return None


def get_collection_fields(token, collection_id):
    """Fetch collection schema to discover field slugs."""
    resp = api_request("GET", f"/collections/{collection_id}", token)
    if not resp or resp.status_code != 200:
        return None
    return resp.json().get("fields", [])


def publish_blog(filepath, collection_id=None, publish=False):
    secrets = load_secrets()
    token = secrets["token"]
    collection_id = collection_id or secrets["collection_id"]

    if not token:
        print("Error: WEBFLOW_API_TOKEN not found.")
        print("Set it via environment variable or add to ~/.claude/lensmor_secrets.json")
        print("See references/webflow-setup-guide.md for instructions.")
        return None

    if not collection_id:
        print("Error: Collection ID not provided.")
        print("Pass --collection_id or add WEBFLOW_BLOG_COLLECTION_ID to ~/.claude/lensmor_secrets.json")
        return None

    # Parse the blog markdown
    print(f"Parsing {filepath}...")
    data = parse_blog_markdown(filepath)
    print(f"  Title: {data['title']}")
    print(f"  Slug: {data['slug']}")
    print(f"  Meta: {data['meta_description'][:80]}...")
    print(f"  Body: {len(data['body_html'])} chars HTML")

    # Discover collection field slugs
    print(f"\nFetching collection schema ({collection_id})...")
    fields = get_collection_fields(token, collection_id)
    if fields is None:
        print("Error: Could not fetch collection schema. Check your collection_id and API token.")
        return None

    # Build field mapping by type
    field_map = {f["slug"]: f for f in fields}
    print(f"  Found {len(fields)} fields: {', '.join(field_map.keys())}")

    # Auto-detect field slugs for common blog fields
    field_data = {"name": data["title"]}
    if data["slug"]:
        field_data["slug"] = data["slug"]

    # Map body to the first RichText field found
    richtext_fields = [f["slug"] for f in fields if f.get("type") == "RichText"]
    if richtext_fields:
        field_data[richtext_fields[0]] = data["body_html"]
        print(f"  Mapped body → '{richtext_fields[0]}'")
    else:
        print("  Warning: No RichText field found in collection. Body not mapped.")

    # Map meta description to PlainText fields that look like summary/excerpt
    summary_candidates = ["post-summary", "summary", "excerpt", "meta-description", "description"]
    for candidate in summary_candidates:
        if candidate in field_map:
            field_data[candidate] = data["meta_description"]
            print(f"  Mapped meta description → '{candidate}'")
            break

    # Create the CMS item
    payload = {
        "isArchived": False,
        "isDraft": not publish,
        "fieldData": field_data,
    }

    print(f"\nCreating CMS item ({'published' if publish else 'draft'})...")
    resp = api_request("POST", f"/collections/{collection_id}/items", token, payload)

    if not resp:
        print("Error: All retries exhausted.")
        return None

    if resp.status_code not in (200, 201, 202):
        print(f"Error {resp.status_code}: {resp.text}")
        return None

    result = resp.json()
    item_id = result.get("id", "unknown")
    print(f"\nSuccess! CMS item created.")
    print(f"  Item ID: {item_id}")
    print(f"  Status: {'Published' if publish else 'Draft'}")

    if not publish:
        print(f"\n  To publish, run again with --publish flag,")
        print(f"  or publish manually in Webflow CMS editor.")

    return item_id


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Publish a blog markdown file to Webflow CMS"
    )
    parser.add_argument("--file", required=True, help="Path to the blog markdown file")
    parser.add_argument("--collection_id", default=None, help="Webflow CMS collection ID (or set WEBFLOW_BLOG_COLLECTION_ID in secrets)")
    parser.add_argument("--publish", action="store_true", help="Publish immediately (default: create as draft)")
    args = parser.parse_args()

    publish_blog(args.file, args.collection_id or None, args.publish)
