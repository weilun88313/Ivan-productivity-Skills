[English](README.md) | [中文](README.zh.md)

---


# Webflow Blog Publisher

> Publish markdown blog posts to Webflow CMS with automatic image uploading

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

Automates publishing blog posts to Webflow CMS. Handles markdown-to-HTML conversion, automatic image uploading, metadata mapping, and CMS item creation via Webflow API v2.

### Key Features

- 📝 **Markdown to HTML** - Automatic conversion with tables and code blocks
- 🖼️ **Auto Image Upload** - Local images uploaded to Webflow Assets
- 👤 **Writer Management** - Random or specified writer profiles
- 🏷️ **Category Mapping** - Smart category resolution
- ⏱️ **Auto Fields** - Read time, timestamps, sort order
- 🔄 **Retry Logic** - Robust error handling with exponential backoff
- ✅ **Draft/Publish** - Control status with `--publish` flag

## Quick Start

### Prerequisites

```bash
pip install requests markdown

# Configure ~/.claude/lensmor_secrets.json
{
  "WEBFLOW_API_TOKEN": "your_api_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "your_collection_id",
  "WEBFLOW_SITE_ID": "your_site_id"
}
```

See [references/webflow-setup-guide.md](references/webflow-setup-guide.md) for setup.

### Usage

```bash
# Publish as draft
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy

# Publish live
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

## Input Format

Expects markdown files from [blog-writer](../blog-writer):

```markdown
# Your Blog Post Title

**Slug**: /blog/category/your-post-slug
**Meta Description**: SEO-friendly description
**Cover Image**:
![Cover](images/cover.png)

---

Article content with **bold** and *italic* text.

![Inline image](images/diagram.png)
```

## Process

1. Parse markdown (title, slug, meta, images, content)
2. Upload images to Webflow Assets → CDN URLs
3. Convert markdown to HTML
4. Map fields to CMS schema
5. Create CMS item (draft or published)

## Command Options

**Required:**
- `--file` - Path to markdown file

**Optional:**
- `--category` - Category slug (strategy, playbooks, teardowns)
- `--writer` - Writer name (random if not specified)
- `--publish` - Publish immediately (draft by default)
- `--collection_id` - Override collection ID

## Writer Management

Writers stored in `assets/writers/writers.json`:

```json
[
  {
    "name": "John Doe",
    "image_url": "https://cdn.prod.website-files.com/.../avatar.jpg"
  }
]
```

**Adding a writer:**
1. Upload avatar to Webflow Assets
2. Add to writers.json with name and CDN URL
3. Use with `--writer "Name"`

## Image Upload

**Supported formats:** PNG, JPEG, GIF, WebP, AVIF, SVG

**Requirements:**
- `WEBFLOW_SITE_ID` must be set
- Images must be local files
- Relative paths resolved from markdown location

**Without Site ID:** Images stripped from content, manual upload required

## Configuration

Create `~/.claude/lensmor_secrets.json`:

```json
{
  "WEBFLOW_API_TOKEN": "your_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "collection_id",
  "WEBFLOW_SITE_ID": "site_id"
}
```

Or use environment variables (takes precedence):

```bash
export WEBFLOW_API_TOKEN='your_token'
export WEBFLOW_BLOG_COLLECTION_ID='collection_id'
export WEBFLOW_SITE_ID='site_id'
```

## Workflow Integration

Works seamlessly with [blog-writer](../blog-writer):

```bash
# 1. Write content (AI-assisted)
# 2. Generate images
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "..." --output_dir workspace/blog/images

# 3. Publish to Webflow
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

## Troubleshooting

- **Image Upload Timeout**: Check internet, reduce file sizes (< 5MB)
- **Draft Not Visible**: Check CMS filters, verify "All Items" view
- **Images Not Uploading**: Add `WEBFLOW_SITE_ID` to secrets (find in Webflow Dashboard → Site Settings)
- **API Token Error**: Verify token in secrets file or environment variables
- **Category Not Found**: Use valid slug (strategy, playbooks, teardowns)

## Error Handling

Automatic retry logic:
- **Server Errors (5xx)**: Up to 3 retries with exponential backoff
- **Rate Limiting (429)**: Respects Retry-After header
- **Timeouts**: 30-second timeout per request

## Best Practices

**Before Publishing:**
- Proofread markdown file
- Verify images exist and paths are correct
- Test as draft first (omit `--publish`)

**Security:**
- Never commit secrets file to git
- Use minimal token permissions
- Rotate API keys periodically

## File Structure

```
webflow-blog-publisher/
├── README.md                     # This file
├── SKILL.md                      # AI workflow instructions
├── scripts/
│   └── publish_to_webflow.py    # Main script
├── references/
│   └── webflow-setup-guide.md   # Setup instructions
└── assets/
    └── writers/
        └── writers.json          # Writer profiles
```

## Resources

- [SKILL.md](SKILL.md) - Technical documentation
- [Setup Guide](references/webflow-setup-guide.md) - Webflow configuration
- [Blog Writer](../blog-writer) - Content creation skill
- [Webflow API Docs](https://developers.webflow.com/) - Official reference

---

**Happy Publishing!** 🚀📄
