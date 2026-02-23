[English](README.md) | [中文](README.zh.md)

---

# Content Pipeline

End-to-end content workflow that orchestrates keyword research, blog writing, image generation, and Webflow publishing in a single session.

## Key Features

- **One command, full pipeline**: Research → Write → Images → Publish
- **Smart orchestration**: Only pauses for key decisions (topic selection)
- **Brand-aware**: Auto-loads Lensmor brand guidelines for product content
- **Integrated image generation**: Gemini API with consistent Linear dark mode style
- **Webflow publishing**: Direct CMS integration with draft/publish options

## Quick Start

```
Run the content pipeline for [topic/product]
```

or

```
Research keywords, write an article, and publish to Webflow about [topic]
```

The pipeline will:
1. Brainstorm keywords and suggest article topics
2. Wait for your topic selection
3. Write the full article
4. Generate cover + inline images
5. Publish to Webflow (draft by default)

## Prerequisites

```bash
pip install requests markdown
```

API keys in `.env` (repository root):
- `GEMINI_API_KEY` (Gemini image generation)
- `WEBFLOW_API_TOKEN`
- `WEBFLOW_BLOG_COLLECTION_ID`
- `WEBFLOW_SITE_ID`

## Related Skills

| Skill | Purpose |
|-------|---------|
| [keyword-research](../keyword-research/) | Standalone keyword research |
| [blog-writer](../blog-writer/) | Standalone article writing |
| [webflow-blog-publisher](../webflow-blog-publisher/) | Standalone Webflow publishing |
| [lensmor-brand-guideline](../lensmor-brand-guideline/) | Lensmor brand context |
