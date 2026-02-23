---
name: webflow-blog-publisher
description: "Publish blog posts to Webflow CMS. Use when the user asks to publish, upload, sync, or push a blog post or article to Webflow."
---

# Webflow Blog Publisher

Publish markdown blog posts to Webflow CMS via API V2.

## Prerequisites

1. **Webflow API Token**, **Collection ID**, and **Site ID** — see [references/webflow-setup-guide.md](references/webflow-setup-guide.md) for setup instructions
2. **Python dependency**: `pip install markdown`

## Usage

### Publish a Blog Post

```bash
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file <blog-markdown-file> \
  --category strategy
```

| Flag | Required | Description |
|------|----------|-------------|
| `--file` | Yes | Path to blog markdown file |
| `--writer` | No | Writer name (random from `assets/writers/writers.json` if omitted) |
| `--category` | No | Category slug: `strategy`, `playbooks`, or `teardowns` |
| `--publish` | No | Publish immediately (default: draft) |
| `--collection_id` | No | Override collection ID from secrets |

Credentials (`WEBFLOW_API_TOKEN`, `WEBFLOW_BLOG_COLLECTION_ID`, `WEBFLOW_SITE_ID`) are read from `.env` in the repository root automatically.

### What the Script Does

1. **Parses** the markdown file: extracts title, slug, meta description, cover image, and body
2. **Uploads images** to Webflow Assets (cover + inline) via presigned S3 URLs
3. **Converts** markdown body to Webflow-compatible HTML (with CDN image URLs)
4. **Auto-fills**: date, recently-updated, read time, sort order, writer (name + image)
5. **Maps cover image** to `thumbnail-image` and `large-image` CMS fields
6. **Resolves** category slug to Webflow reference ID
7. **Creates** the CMS item via Webflow API V2

### Writer Profiles

Writers are stored in [assets/writers/writers.json](assets/writers/writers.json). To add a writer:
1. Upload their avatar to Webflow Assets and copy the CDN URL
2. Add an entry: `{"name": "Name", "image_url": "https://cdn.prod.website-files.com/..."}`

If `--writer` is not specified, a random writer is selected.

### Input Format

The script expects markdown files with this header structure (produced by the Blog Writer skill):

```
# [Title]

**Slug**: /blog/category/slug-name
**Meta Description**: Summary text here
**Primary Keywords**: keyword one, keyword two, keyword three
**Reading Time**: 8
**Cover Image**:
![description](images/cover.png)

---

[Article body in markdown, with inline images like ![alt](images/img.png)]
```

### Field Mapping

| Source | Webflow Field |
|--------|---------------|
| `# Title` | `name` |
| `**Slug**` | `slug` (last path segment) |
| `**Meta Description**` | `meta-description` |
| `**Primary Keywords**` | `primary-keywords` (PlainText, comma-separated) |
| `**Reading Time**` | `reading-time` (Number, minutes only; falls back to auto-calc from word count) |
| `**Cover Image**` | `thumbnail-image` + `large-image` (auto-uploaded to Webflow Assets) |
| Body content (with images) | First `RichText` field (`details-01`), inline images auto-uploaded |
| Current timestamp | `date`, `recently-updated` |
| Word count ÷ 200 wpm | `read-time` (e.g. "6 min read") |
| Writer from `assets/writers/writers.json` | `writer-name` + `writer-image` (CDN URL) |
| `--category` flag | `ref` (resolved to item ID) |
| Auto: existing item count + 1 | `sort` |

### Publish FAQs

After publishing a blog post, publish its FAQ items to the FAQ CMS collection:

```bash
python Skill/webflow-blog-publisher/scripts/publish_faqs.py \
  --file <blog-markdown-file> \
  --blog-item-id <BLOG_ITEM_ID>
```

| Flag | Required | Description |
|------|----------|-------------|
| `--file` | Yes | Path to blog markdown file (same file used for blog publishing) |
| `--blog-item-id` | Yes | Webflow item ID of the parent blog post (returned by `publish_to_webflow.py`) |
| `--collection_id` | No | FAQ collection ID (default: `699bdef9a464252e0ab59b60`, or `WEBFLOW_FAQ_COLLECTION_ID` env var) |
| `--publish` | No | Publish immediately (default: draft) |

#### What the Script Does

1. **Parses** the `## FAQ` section from the markdown file (after the `---` separator at the end)
2. **Generates** deterministic slugs: `{blog-slug}-faq-{N}`
3. **Creates or updates** FAQ CMS items (idempotent — safe to re-run)
4. **Links** each FAQ to the parent blog post via the `related-blog-2` reference field
5. **Cleans up** orphaned FAQs when the FAQ count decreases between runs

#### FAQ CMS Field Mapping

| Source | Webflow Field | Type |
|--------|---------------|------|
| Question text | `name` | PlainText |
| Generated slug | `slug` | PlainText |
| Answer text | `answer` | PlainText (singleLine) |
| Blog item ID | `related-blog-2` | Reference → Blog |
| Sequential index | `order` | Number |

#### FAQ Format in Markdown

The FAQ section must appear at the end of the article, after a horizontal rule:

```markdown
## Conclusion
[conclusion content]

---

## FAQ

**Q: Question text here?**
A: Single-line plain text answer here.

**Q: Another question?**
A: Another answer (max 256 chars, no HTML/markdown).
```

The blog publisher (`publish_to_webflow.py`) automatically strips the FAQ section from the blog body HTML, so it won't appear in the published article.

### Notes

- **Images**: Local images are auto-uploaded to Webflow Assets and replaced with CDN URLs. Requires `WEBFLOW_SITE_ID` in secrets. If Site ID is missing, images are stripped and must be uploaded manually.
- **Draft vs. Publish**: Default is draft mode. Use `--publish` flag only when ready to go live.
- The script prints all available collection fields on each run, making it easy to verify the mapping.
