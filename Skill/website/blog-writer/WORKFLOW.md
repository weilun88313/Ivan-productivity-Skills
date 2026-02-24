# Blog Creation Workflow

> End-to-end workflow for creating and publishing SEO-optimized blog posts.

## Recommended: Use content-pipeline

For the full automated flow (keyword research → writing → images → publishing), use the **content-pipeline** skill instead of running each step manually:

```
Run the content pipeline for [topic]
```

See: [content-pipeline SKILL.md](../content-pipeline/SKILL.md)

## Manual Workflow

If you prefer to run each step separately:

### 1. Write a Blog Post

```
Write a blog post about [topic]
```

The blog-writer skill creates a markdown file with metadata (title, slug, meta description, cover image placeholder) and article body.

### 2. Generate Images

Use the unified **blog-image-generator** skill:

```bash
# Cover image (abstract, no text)
python Skill/website/blog-image-generator/scripts/generate.py \
  --platform blog \
  --type cover \
  --prompt "[ARTICLE TITLE]" \
  --output workspace/blog/images/cover.png

# Inline images (repeat for each, choose --type per content)
python Skill/website/blog-image-generator/scripts/generate.py \
  --platform blog \
  --type [data_cluster|data_flow|segmentation|temporal|inline] \
  --prompt "[DESCRIPTION]" \
  --output workspace/blog/images/inline_1.png
```

See `references/visual-style-guide.md` for prompt templates and `Skill/website/blog-image-generator/SKILL.md` for the full API.

### 3. Publish to Webflow

```bash
python Skill/website/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy
```

Add `--publish` to go live immediately (default: draft).

## File Structure

```
workspace/blog/
├── article.md
└── images/
    ├── cover_*.png
    ├── inline_1_*.png
    ├── inline_2_*.png
    └── inline_3_*.png
```

## Prerequisites

```bash
pip install requests markdown
```

API keys in `.env` (repository root):
- `GEMINI_API_KEY` — Gemini API
- `WEBFLOW_API_TOKEN` — Webflow API
- `WEBFLOW_BLOG_COLLECTION_ID` — Blog collection
- `WEBFLOW_SITE_ID` — Site for image uploads
