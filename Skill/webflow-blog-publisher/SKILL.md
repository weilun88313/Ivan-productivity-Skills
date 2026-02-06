---
name: webflow-blog-publisher
description: "Publish blog posts to Webflow CMS. Use when the user asks to publish, upload, sync, or push a blog post or article to Webflow."
---

# Webflow Blog Publisher

Publish markdown blog posts to Webflow CMS via API V2.

## Prerequisites

1. **Webflow API Token** and **Collection ID** — see [references/webflow-setup-guide.md](references/webflow-setup-guide.md) for setup instructions
2. **Python dependency**: `pip install markdown`

## Usage

### Publish a Blog Post

```bash
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py --file <blog-markdown-file>
```

Both `WEBFLOW_API_TOKEN` and `WEBFLOW_BLOG_COLLECTION_ID` are read from `~/.claude/lensmor_secrets.json` automatically. Use `--collection_id` to override. Add `--publish` to publish immediately (default: draft).

### What the Script Does

1. **Parses** the markdown file: extracts title, slug, meta description, and body
2. **Converts** markdown body to Webflow-compatible HTML (headings, lists, tables, bold, code)
3. **Auto-detects** your collection's field schema and maps content to the correct fields
4. **Creates** the CMS item via Webflow API V2

### Input Format

The script expects markdown files with this header structure (produced by the Blog Writer skill):

```
# [Title]

**Slug**: /blog/category/slug-name
**Meta Description**: Summary text here

---

[Article body in markdown]
```

### Field Mapping

| Source | Webflow Field |
|--------|---------------|
| `# Title` | `name` |
| `**Slug**` | `slug` (last path segment) |
| `**Meta Description**` | First matching: `post-summary`, `summary`, `excerpt`, `meta-description` |
| Body content | First `RichText` field in collection |

### Notes

- **Images**: Local image references are stripped from the HTML. Upload images manually in the Webflow CMS editor after publishing.
- **Draft vs. Publish**: Default is draft mode. Use `--publish` flag only when ready to go live.
- The script prints all available collection fields on each run, making it easy to verify the mapping.
