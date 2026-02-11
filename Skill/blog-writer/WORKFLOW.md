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

```bash
# Cover image (abstract, no text)
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "FULL PROMPT" \
  --output_dir workspace/blog/images \
  --filename cover

# Inline images (repeat for each)
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "FULL PROMPT" \
  --output_dir workspace/blog/images \
  --filename inline_1
```

See `references/visual-style-guide.md` for prompt templates.

### 3. Publish to Webflow

```bash
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
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

Secrets in `~/.claude/lensmor_secrets.json`:
- `NANO_API_KEY` — Gemini API
- `WEBFLOW_API_TOKEN` — Webflow API
- `WEBFLOW_BLOG_COLLECTION_ID` — Blog collection
- `WEBFLOW_SITE_ID` — Site for image uploads
