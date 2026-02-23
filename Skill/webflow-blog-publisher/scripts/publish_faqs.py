"""Publish FAQ items from a blog markdown file to Webflow CMS.

Parses the ## FAQ section at the end of article.md, then creates/updates
FAQ CMS items linked to the parent blog post via a reference field.

Usage:
    python publish_faqs.py --file workspace/blog/article.md --blog-item-id <ID> [--publish]
"""

import os
import sys
import re
import argparse

from publish_to_webflow import load_secrets, api_request, find_item_by_slug, delete_item

DEFAULT_FAQ_COLLECTION_ID = "699bdef9a464252e0ab59b60"


def parse_faqs_from_markdown(filepath):
    """Parse the ## FAQ section from a blog markdown file.

    Expects the format:
        ---

        ## FAQ

        **Q: Question text?**
        A: Single-line answer.

    Returns a list of dicts: [{"question": str, "answer": str}, ...]
    """
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Find the FAQ section: a horizontal rule followed by ## FAQ
    faq_match = re.search(r"\n---\s*\n+## FAQ\s*\n", text)
    if not faq_match:
        return []

    faq_text = text[faq_match.end():]

    faqs = []
    # Match Q&A pairs: **Q: ...?**\nA: ...
    for m in re.finditer(
        r"\*\*Q:\s*(.+?)\*\*\s*\nA:\s*(.+)",
        faq_text,
    ):
        question = m.group(1).strip()
        answer = m.group(2).strip()
        faqs.append({"question": question, "answer": answer})

    return faqs


def _make_faq_slug(blog_slug, index):
    """Generate a deterministic slug for a FAQ item."""
    return f"{blog_slug}-faq-{index}"


def _extract_blog_slug(filepath):
    """Extract the blog slug from the markdown header."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    slug_match = re.search(r"\*\*Slug\*\*:\s*(.+)", text)
    if slug_match:
        raw = slug_match.group(1).strip()
        return raw.rstrip("/").split("/")[-1]
    return None


def publish_faqs(filepath, blog_item_id, collection_id=None, publish=False):
    """Parse FAQs from markdown and publish them to Webflow CMS.

    Args:
        filepath: Path to the blog markdown file.
        blog_item_id: Webflow item ID of the parent blog post.
        collection_id: FAQ collection ID (uses default if not provided).
        publish: If True, publish items immediately.

    Returns:
        List of created/updated FAQ item IDs, or None on error.
    """
    secrets = load_secrets()
    token = secrets["token"]
    collection_id = collection_id or os.environ.get(
        "WEBFLOW_FAQ_COLLECTION_ID", DEFAULT_FAQ_COLLECTION_ID
    )

    if not token:
        print("Error: WEBFLOW_API_TOKEN not found.")
        return None

    # Parse FAQs
    faqs = parse_faqs_from_markdown(filepath)
    if not faqs:
        print("No FAQ section found in the markdown file.")
        return []

    blog_slug = _extract_blog_slug(filepath)
    if not blog_slug:
        print("Error: Could not extract blog slug from markdown.")
        return None

    print(f"Found {len(faqs)} FAQ(s) for blog '{blog_slug}'")

    faq_item_ids = []
    for i, faq in enumerate(faqs, start=1):
        slug = _make_faq_slug(blog_slug, i)
        question = faq["question"][:256]
        answer = faq["answer"][:256] if faq["answer"] else ""

        print(f"\n  [{i}/{len(faqs)}] {slug}")
        print(f"    Q: {question[:80]}{'...' if len(question) > 80 else ''}")
        print(f"    A: {answer[:80]}{'...' if len(answer) > 80 else ''}")

        field_data = {
            "name": question,
            "slug": slug,
            "answer": answer,
            "related-blog-2": blog_item_id,
            "order": i,
        }

        payload = {
            "isArchived": False,
            "isDraft": not publish,
            "fieldData": field_data,
        }

        # Check if FAQ already exists
        existing_id, is_draft = find_item_by_slug(token, collection_id, slug)

        if existing_id:
            # Unpublish first if currently published
            if not is_draft:
                unpublish_payload = {
                    "isArchived": False,
                    "isDraft": True,
                    "fieldData": field_data,
                }
                resp = api_request(
                    "PATCH",
                    f"/collections/{collection_id}/items/{existing_id}",
                    token,
                    unpublish_payload,
                )
                if resp and resp.status_code in (200, 201, 202):
                    print(f"    Unpublished existing item")

            resp = api_request(
                "PATCH",
                f"/collections/{collection_id}/items/{existing_id}",
                token,
                payload,
            )
            action = "updated"
        else:
            resp = api_request(
                "POST",
                f"/collections/{collection_id}/items",
                token,
                payload,
            )
            action = "created"

        if not resp or resp.status_code not in (200, 201, 202):
            status = resp.status_code if resp else "no response"
            body = resp.text if resp else ""
            print(f"    Error {status}: {body}")
            continue

        item_id = resp.json().get("id") or existing_id
        faq_item_ids.append(item_id)
        print(f"    {action} (ID: {item_id})")

    # Clean up orphaned FAQs
    _cleanup_orphaned_faqs(token, collection_id, blog_slug, len(faqs))

    print(f"\nFAQ publishing complete: {len(faq_item_ids)}/{len(faqs)} succeeded.")
    return faq_item_ids


def _cleanup_orphaned_faqs(token, collection_id, blog_slug, current_count):
    """Delete FAQ items whose index exceeds the current FAQ count.

    When the number of FAQs decreases between runs, the extra items
    (e.g., faq-6 when only 5 remain) are removed.
    """
    # Check indices beyond current count (probe up to 20)
    max_probe = max(current_count + 10, 20)
    deleted = 0
    for i in range(current_count + 1, max_probe + 1):
        slug = _make_faq_slug(blog_slug, i)
        item_id, _ = find_item_by_slug(token, collection_id, slug)
        if item_id:
            if delete_item(token, collection_id, item_id):
                print(f"  Deleted orphaned FAQ: {slug}")
                deleted += 1
        else:
            # No more items at higher indices — stop probing
            break

    if deleted:
        print(f"  Cleaned up {deleted} orphaned FAQ(s)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Publish FAQ items from a blog markdown to Webflow CMS"
    )
    parser.add_argument(
        "--file", required=True, help="Path to the blog markdown file"
    )
    parser.add_argument(
        "--blog-item-id",
        required=True,
        help="Webflow item ID of the parent blog post",
    )
    parser.add_argument(
        "--collection_id",
        default=None,
        help=f"FAQ collection ID (default: {DEFAULT_FAQ_COLLECTION_ID})",
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Publish immediately (default: draft)",
    )
    args = parser.parse_args()

    publish_faqs(
        args.file,
        args.blog_item_id,
        args.collection_id or None,
        args.publish,
    )
