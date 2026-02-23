import os
import sys
import re
import json
import argparse
import time
import math
import random
import hashlib
from datetime import datetime, timezone
import requests

# Initialize environment from .env (with legacy JSON fallback)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "..", "scripts"))
import env_setup; env_setup.init_env()

try:
    import markdown
except ImportError:
    print("Missing dependency: pip install markdown")
    exit(1)

API_BASE = "https://api.webflow.com/v2"
MAX_RETRIES = 3
TIMEOUT = 30
WORDS_PER_MINUTE = 200

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WRITERS_PATH = os.path.join(SCRIPT_DIR, "..", "assets", "writers", "writers.json")


def load_secrets():
    """Load secrets from environment variables (populated by env_setup)."""
    return {
        "token": os.environ.get("WEBFLOW_API_TOKEN"),
        "collection_id": os.environ.get("WEBFLOW_BLOG_COLLECTION_ID"),
        "site_id": os.environ.get("WEBFLOW_SITE_ID"),
    }


def load_writers():
    """Load writer profiles from assets/writers/writers.json."""
    try:
        with open(WRITERS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def pick_writer(writers, name=None):
    """Pick a writer by name, or randomly if not specified."""
    if not writers:
        return None
    if name:
        for w in writers:
            if w["name"].lower() == name.lower():
                return w
        print(f"  Warning: Writer '{name}' not found. Available: {', '.join(w['name'] for w in writers)}")
        return None
    return random.choice(writers)


MIME_TYPES = {
    "png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
    "gif": "image/gif", "webp": "image/webp", "avif": "image/avif",
    "svg": "image/svg+xml",
}


def upload_image_to_webflow(token, site_id, file_path):
    """Upload a local image to Webflow Assets. Returns CDN URL or None."""
    if not os.path.isfile(file_path):
        print(f"  Warning: Image not found: {file_path}")
        return None

    with open(file_path, "rb") as f:
        file_bytes = f.read()

    file_hash = hashlib.md5(file_bytes).hexdigest()
    file_name = os.path.basename(file_path)
    ext = file_name.rsplit(".", 1)[-1].lower() if "." in file_name else "png"
    content_type = MIME_TYPES.get(ext, "application/octet-stream")

    # Step 1: Request presigned upload URL from Webflow
    resp = api_request("POST", f"/sites/{site_id}/assets", token, {
        "fileName": file_name,
        "fileHash": file_hash,
    })
    if not resp or resp.status_code not in (200, 201, 202):
        print(f"  Error requesting upload URL: {resp.status_code if resp else 'no response'}")
        return None

    asset_data = resp.json()
    upload_url = asset_data.get("uploadUrl")
    upload_details = asset_data.get("uploadDetails", {})
    cdn_url = asset_data.get("hostedUrl") or asset_data.get("assetUrl")

    if not upload_url or not upload_details:
        print(f"  Error: Missing upload URL in response")
        return None

    # Step 2: Upload file to S3 via presigned URL
    fields = [(k, (None, str(v))) for k, v in upload_details.items()]
    fields.append(("file", (file_name, file_bytes, content_type)))

    try:
        s3_resp = requests.post(upload_url, files=fields, timeout=120)
        if s3_resp.status_code in (200, 201, 204):
            print(f"  Uploaded: {file_name} → {cdn_url}")
            return cdn_url
        else:
            print(f"  S3 upload failed: {s3_resp.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"  Upload error: {e}")
        return None


def parse_blog_markdown(filepath):
    """Parse blog markdown into metadata, body content, and image references."""
    base_dir = os.path.dirname(os.path.abspath(filepath))

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled"

    slug_match = re.search(r"\*\*Slug\*\*:\s*(.+)", text)
    slug = ""
    if slug_match:
        raw_slug = slug_match.group(1).strip()
        slug = raw_slug.rstrip("/").split("/")[-1]

    meta_match = re.search(r"\*\*Meta Description\*\*:\s*(.+)", text)
    meta_desc = meta_match.group(1).strip() if meta_match else ""

    keywords_match = re.search(r"\*\*Primary Keywords\*\*:\s*(.+)", text)
    primary_keywords = keywords_match.group(1).strip() if keywords_match else ""

    reading_time_match = re.search(r"\*\*Reading Time\*\*:\s*(.+)", text)
    reading_time = None
    if reading_time_match:
        digits = re.sub(r"[^\d]", "", reading_time_match.group(1))
        reading_time = int(digits) if digits else None

    # Extract cover image (in metadata section, before ---)
    cover_image = None
    cover_match = re.search(r"\*\*Cover Image\*\*:\s*\n?\s*!\[([^\]]*)\]\(([^)]+)\)", text)
    if cover_match:
        cover_path = cover_match.group(2).strip()
        if not os.path.isabs(cover_path):
            cover_path = os.path.join(base_dir, cover_path)
        cover_image = cover_path

    parts = text.split("\n---\n", 1)
    body_md = parts[1].strip() if len(parts) > 1 else text

    # Extract inline image paths and resolve to absolute paths
    inline_images = []
    for match in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", body_md):
        alt, path = match.group(1), match.group(2).strip()
        abs_path = path if os.path.isabs(path) else os.path.join(base_dir, path)
        inline_images.append({"alt": alt, "path": abs_path, "original": match.group(0), "raw_path": path})

    # Don't convert to HTML yet — images need to be uploaded first
    plain_text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", "", body_md)
    plain_text = re.sub(r"[#*_\[\]`>|~-]", "", plain_text)
    word_count = len(plain_text.split())
    read_minutes = max(1, math.ceil(word_count / WORDS_PER_MINUTE))

    return {
        "title": title,
        "slug": slug,
        "meta_description": meta_desc,
        "primary_keywords": primary_keywords,
        "reading_time": reading_time if reading_time is not None else read_minutes,
        "body_md": body_md,
        "cover_image": cover_image,
        "inline_images": inline_images,
        "read_time": f"{read_minutes} min read",
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


def get_item_count(token, collection_id, published_only=False):
    """Get number of items in a collection.

    Args:
        published_only: If True, count only published (non-draft) items.
    """
    if not published_only:
        resp = api_request("GET", f"/collections/{collection_id}/items?limit=1", token)
        if not resp or resp.status_code != 200:
            return 0
        return resp.json().get("pagination", {}).get("total", 0)

    # Count only published items by paginating through all items
    count = 0
    offset = 0
    limit = 100
    while True:
        resp = api_request("GET", f"/collections/{collection_id}/items?limit={limit}&offset={offset}", token)
        if not resp or resp.status_code != 200:
            break
        data = resp.json()
        items = data.get("items", [])
        count += sum(1 for item in items if not item.get("isDraft", True))
        total = data.get("pagination", {}).get("total", 0)
        offset += limit
        if offset >= total or not items:
            break
    return count


def find_item_by_slug(token, collection_id, slug):
    """Find an existing item by slug. Returns (item_id, is_draft) tuple if found, (None, None) otherwise."""
    if not slug:
        return None, None
    # Search for item with matching slug
    resp = api_request("GET", f"/collections/{collection_id}/items", token)
    if not resp or resp.status_code != 200:
        return None, None
    items = resp.json().get("items", [])
    for item in items:
        fd = item.get("fieldData", {})
        if fd.get("slug") == slug:
            return item.get("id"), item.get("isDraft", False)
    return None, None


def delete_item(token, collection_id, item_id):
    """Delete a CMS item."""
    resp = api_request("DELETE", f"/collections/{collection_id}/items/{item_id}", token)
    return resp and resp.status_code in (200, 204)


def resolve_category(token, ref_field, category_slug):
    """Resolve a category slug to its Webflow item ID."""
    ref_collection_id = ref_field.get("validations", {}).get("collectionId")
    if not ref_collection_id:
        return None
    resp = api_request("GET", f"/collections/{ref_collection_id}/items", token)
    if not resp or resp.status_code != 200:
        return None
    for item in resp.json().get("items", []):
        fd = item.get("fieldData", {})
        if fd.get("slug") == category_slug or fd.get("name", "").lower() == category_slug.lower():
            return item["id"]
    return None


def list_categories(token, ref_field):
    """List available categories for display."""
    ref_collection_id = ref_field.get("validations", {}).get("collectionId")
    if not ref_collection_id:
        return []
    resp = api_request("GET", f"/collections/{ref_collection_id}/items", token)
    if not resp or resp.status_code != 200:
        return []
    return [(item["id"], item["fieldData"].get("name"), item["fieldData"].get("slug"))
            for item in resp.json().get("items", [])]


def publish_blog(filepath, collection_id=None, publish=False,
                 writer_name=None, category=None):
    secrets = load_secrets()
    token = secrets["token"]
    collection_id = collection_id or secrets["collection_id"]
    site_id = secrets.get("site_id")

    if not token:
        print("Error: WEBFLOW_API_TOKEN not found.")
        print("Add WEBFLOW_API_TOKEN to .env in the repository root.")
        print("See .env.example and references/webflow-setup-guide.md for instructions.")
        return None

    if not collection_id:
        print("Error: Collection ID not provided.")
        print("Pass --collection_id or add WEBFLOW_BLOG_COLLECTION_ID to .env")
        return None

    # Parse the blog markdown
    print(f"Parsing {filepath}...")
    data = parse_blog_markdown(filepath)
    print(f"  Title: {data['title']}")
    print(f"  Slug: {data['slug']}")
    print(f"  Meta: {data['meta_description'][:80]}...")
    print(f"  Cover image: {'yes' if data['cover_image'] else 'none'}")
    print(f"  Inline images: {len(data['inline_images'])}")
    print(f"  Primary keywords: {data['primary_keywords'] or '(none)'}")
    print(f"  Reading time: {data['reading_time']} min")
    print(f"  Read time: {data['read_time']}")

    # === Upload images to Webflow Assets ===
    cover_cdn_url = None
    body_md = data["body_md"]

    if site_id and (data["cover_image"] or data["inline_images"]):
        print(f"\nUploading images to Webflow Assets...")

        # Upload cover image
        if data["cover_image"]:
            cover_cdn_url = upload_image_to_webflow(token, site_id, data["cover_image"])

        # Upload inline images and replace paths in markdown
        for img in data["inline_images"]:
            cdn_url = upload_image_to_webflow(token, site_id, img["path"])
            if cdn_url:
                body_md = body_md.replace(img["raw_path"], cdn_url)
            else:
                # Remove failed image references
                body_md = body_md.replace(img["original"], "")
    elif not site_id and (data["cover_image"] or data["inline_images"]):
        print(f"\n  Warning: WEBFLOW_SITE_ID not set, skipping image uploads.")
        print(f"  Add WEBFLOW_SITE_ID to .env to enable.")
        # Strip images if we can't upload
        body_md = re.sub(r"!\[([^\]]*)\]\([^)]*\)\n?", "", body_md)

    # Convert markdown to HTML (now with CDN URLs for uploaded images)
    body_html = markdown.markdown(body_md, extensions=["tables", "fenced_code"])

    # Open all links in new tab
    body_html = body_html.replace("<a ", '<a target="_blank" rel="noopener noreferrer" ')

    # Add full-width styling to all images with !important to override Webflow defaults
    # Use container-relative width to ensure images fill the content area without overflow
    figure_style = (
        "width: 100% !important; "
        "max-width: 100% !important; "
        "margin: 2em 0 !important; "
        "padding: 0 !important; "
        "display: block !important;"
    )
    img_style = (
        "width: 100% !important; "
        "max-width: 100% !important; "
        "height: auto !important; "
        "display: block !important; "
        "margin: 0 !important; "
        "border-radius: 8px !important; "
        "object-fit: cover !important;"
    )

    body_html = re.sub(
        r'<img\s+([^>]*?)alt="([^"]*)"([^>]*?)src="([^"]*)"([^>]*)>',
        rf'<figure style="{figure_style}"><img \1alt="\2"\3src="\4"\5 style="{img_style}"></figure>',
        body_html
    )
    # Handle cases where src comes before alt
    body_html = re.sub(
        r'<img\s+([^>]*?)src="([^"]*)"([^>]*?)alt="([^"]*)"([^>]*)>',
        rf'<figure style="{figure_style}"><img \1src="\2"\3alt="\4"\5 style="{img_style}"></figure>',
        body_html
    )

    # Add styling to tables for Webflow dark theme (black background)
    table_style = (
        "width: 100% !important; "
        "border-collapse: separate !important; "
        "border-spacing: 0 !important; "
        "margin: 1.5em 0 !important; "
        "font-size: 0.95em !important; "
        "border: 1px solid rgba(255,255,255,0.15) !important; "
        "border-radius: 8px !important; "
        "overflow: hidden !important;"
    )
    thead_style = (
        "background: rgba(107,117,255,0.12) !important;"
    )
    th_style = (
        "padding: 12px 16px !important; "
        "text-align: left !important; "
        "font-weight: 600 !important; "
        "color: #fff !important; "
        "border-bottom: 1px solid rgba(107,117,255,0.4) !important;"
    )
    td_style = (
        "padding: 10px 16px !important; "
        "text-align: left !important; "
        "background: rgba(255,255,255,0.04) !important; "
        "border-bottom: 1px solid rgba(255,255,255,0.08) !important;"
    )
    body_html = body_html.replace("<table>", f'<table style="{table_style}">')
    body_html = body_html.replace("<thead>", f'<thead style="{thead_style}">')
    body_html = re.sub(r"<th(?:\s[^>]*)?>", lambda m: f'<th style="{th_style}">', body_html)
    body_html = re.sub(r"<td(?:\s[^>]*)?>", lambda m: f'<td style="{td_style}">', body_html)

    print(f"  Body: {len(body_html)} chars HTML")

    # Load writer profiles
    writers = load_writers()
    writer = pick_writer(writers, writer_name)
    if writer:
        print(f"  Writer: {writer['name']}")

    # Discover collection field slugs
    print(f"\nFetching collection schema ({collection_id})...")
    fields = get_collection_fields(token, collection_id)
    if fields is None:
        print("Error: Could not fetch collection schema. Check your collection_id and API token.")
        return None

    field_map = {f["slug"]: f for f in fields}
    print(f"  Found {len(fields)} fields: {', '.join(field_map.keys())}")

    # Auto-detect sort from published item count (drafts don't count)
    published_count = get_item_count(token, collection_id, published_only=True)
    sort_order = published_count + 1
    print(f"  Published articles: {published_count}, new sort → {sort_order}")

    # === Build fieldData ===
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

    field_data = {"name": data["title"]}
    if data["slug"]:
        field_data["slug"] = data["slug"]

    # Body → first RichText field
    richtext_fields = [f["slug"] for f in fields if f.get("type") == "RichText"]
    if richtext_fields:
        field_data[richtext_fields[0]] = body_html
        print(f"  Mapped body → '{richtext_fields[0]}'")

    # Cover image → thumbnail-image + large-image
    if cover_cdn_url:
        for img_field in ["thumbnail-image", "large-image"]:
            if img_field in field_map:
                field_data[img_field] = {"url": cover_cdn_url}
                print(f"  Mapped {img_field} → cover image")

    # Meta description
    summary_candidates = ["post-summary", "summary", "excerpt", "meta-description", "description"]
    for candidate in summary_candidates:
        if candidate in field_map:
            field_data[candidate] = data["meta_description"]
            print(f"  Mapped meta description → '{candidate}'")
            break

    # Date + Recently Updated
    if "date" in field_map:
        field_data["date"] = now_iso
        print(f"  Mapped date → '{now_iso}'")
    if "recently-updated" in field_map:
        field_data["recently-updated"] = now_iso

    # Read time (legacy text field)
    if "read-time" in field_map:
        field_data["read-time"] = data["read_time"]
        print(f"  Mapped read-time → '{data['read_time']}'")

    # Reading time (number field, minutes only)
    if "reading-time" in field_map:
        field_data["reading-time"] = data["reading_time"]
        print(f"  Mapped reading-time → {data['reading_time']}")

    # Primary keywords
    if "primary-keywords" in field_map and data["primary_keywords"]:
        field_data["primary-keywords"] = data["primary_keywords"]
        print(f"  Mapped primary-keywords → '{data['primary_keywords']}'")

    # Sort order (auto)
    if "sort" in field_map:
        field_data["sort"] = sort_order
        print(f"  Mapped sort → {sort_order}")

    # Writer name + image
    if writer:
        if "writer-name" in field_map:
            field_data["writer-name"] = writer["name"]
            print(f"  Mapped writer-name → '{writer['name']}'")
        if "writer-image" in field_map and writer.get("image_url"):
            field_data["writer-image"] = {"url": writer["image_url"]}
            print(f"  Mapped writer-image → '{writer['image_url'][:60]}...'")

    # Category (ref field)
    if category and "ref" in field_map:
        cat_id = resolve_category(token, field_map["ref"], category)
        if cat_id:
            field_data["ref"] = cat_id
            print(f"  Mapped ref → '{category}' (ID: {cat_id})")
        else:
            cats = list_categories(token, field_map["ref"])
            print(f"  Warning: Category '{category}' not found. Available:")
            for cid, cname, cslug in cats:
                print(f"    - {cslug} ({cname})")

    # Check if item already exists by slug
    existing_item_id, is_draft = find_item_by_slug(token, collection_id, data["slug"])

    # Prepare payload
    payload = {
        "isArchived": False,
        "isDraft": not publish,
        "fieldData": field_data,
    }

    if existing_item_id:
        # If existing item is published, unpublish it first, then update, then republish
        if not is_draft:
            print(f"\nFound existing published item (ID: {existing_item_id})")
            print(f"  Step 1: Unpublishing...")
            unpublish_payload = {
                "isArchived": False,
                "isDraft": True,
                "fieldData": field_data,
            }
            resp = api_request("PATCH", f"/collections/{collection_id}/items/{existing_item_id}", token, unpublish_payload)
            if not resp or resp.status_code not in (200, 201, 202):
                print(f"  ✗ Failed to unpublish, will attempt direct update")
            else:
                print(f"  ✓ Unpublished")

        # Update the item with new content
        print(f"  Step 2: Updating content...")
        resp = api_request("PATCH", f"/collections/{collection_id}/items/{existing_item_id}", token, payload)
        action = "updated"
    else:
        # Create new item
        print(f"\nCreating new CMS item ({'published' if publish else 'draft'})...")
        resp = api_request("POST", f"/collections/{collection_id}/items", token, payload)
        action = "created"

    if not resp:
        print("  ✗ Error: All retries exhausted.")
        return None

    if resp.status_code not in (200, 201, 202):
        print(f"  ✗ Error {resp.status_code}: {resp.text}")
        return None

    result = resp.json()
    item_id = result.get("id") or existing_item_id or "unknown"

    if existing_item_id and not is_draft:
        print(f"  ✓ Content updated")
        if publish:
            print(f"  Step 3: Publishing...")
            print(f"  ✓ Published")

    print(f"\n✅ Success! CMS item {action}.")
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
    parser.add_argument("--writer", default=None, help="Writer name (random if not specified)")
    parser.add_argument("--category", default=None, help="Category slug or name (e.g. 'strategy', 'playbooks', 'teardowns')")
    args = parser.parse_args()

    publish_blog(
        args.file,
        args.collection_id or None,
        args.publish,
        writer_name=args.writer,
        category=args.category,
    )
