[English](README.md) | [中文](README.zh.md)

---

# Blog Writer

> Create high-ranking, SEO-friendly blog posts with AI-generated visuals

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

Create professional, actionable, and SEO-optimized blog posts following proven content formulas. Combines expert content structure with AI-generated visual assets to produce publish-ready articles.

### Key Features

- ✍️ **Professional Content** - Actionable, empathetic tone with clear structure
- 📊 **SEO-Optimized** - Structured for search engine visibility
- 🎨 **AI-Generated Illustrations** - High-quality 16:9 images with Linear dark mode style
- 📝 **Structured Format** - Hook → Why → How → CTA framework
- 💡 **Pro Tips** - Insider advice callouts throughout
- 🎯 **Ready for Publishing** - Compatible with Webflow Blog Publisher

## Quick Start

### Prerequisites

```bash
# Install dependencies
pip install requests

# Set up API keys — copy .env.example to .env and fill in your keys
cp .env.example .env
# Edit .env:
#   GEMINI_API_KEY=your_api_key_here
#   FAL_KEY=your_fal_key_here
```

### Usage

**Generate a blog post:**
```
Write a blog post about email marketing best practices
```

**Generate images:**
```bash
python scripts/generate_image.py \
  --prompt "Abstract email marketing data visualization" \
  --output_dir workspace/blog/images \
  --filename cover
```

## Content Structure

Posts follow a proven formula:

1. **Hook** - Problem, agitation, promise
2. **Why** - Benefits and data
3. **How-To** - Step-by-step or listicle format
4. **Conclusion** - Key takeaways and CTA

### Output Format

```markdown
# [Engaging Title with Keywords]

**Slug**: /blog/[category]/[keyword-slug]
**Meta Description**: [150-160 chars SEO summary]
**Cover Image**:
![Description](images/cover.png)

---

[Article content]
```

## Image Generation

**Visual Style:** Linear dark mode aesthetic
- **Colors**: Deep charcoal (#1a1a1a), violet-blue accents (#6B75FF)
- **Quality**: 16:9 aspect ratio, high resolution (2K+)
- **Content**: Abstract shapes, data visualizations, minimal text

**API Providers (with automatic fallback):**
1. Gemini API (GEMINI_API_KEY)
2. Fal.ai Nano Banana Pro (FAL_KEY)

See [visual-style-guide.md](references/visual-style-guide.md) for complete prompt templates.

## Related Skills

| Skill | Purpose |
|-------|---------|
| [keyword-research](../keyword-research/) | Find target keywords first |
| [webflow-blog-publisher](../webflow-blog-publisher/) | Publish to Webflow |
| [content-pipeline](../content-pipeline/) | Full automated workflow |

## Troubleshooting

### Image Generation Fails

- **Region not supported**: Gemini API may fail in some regions. System auto-falls back to Fal.ai.
- **Add Fal.ai key**: Configure `FAL_KEY` for reliable fallback
- **Check API keys**: Verify both GEMINI_API_KEY and FAL_KEY are set in .env

### Content Quality

- Specify word count: "Write 2000-2500 words"
- Define target audience
- Request specific tone: "professional blog style"

## File Structure

```
blog-writer/
├── README.md              # This file
├── SKILL.md               # AI instructions
├── scripts/
│   ├── image_generator.py # Unified API (Gemini + Fal.ai)
│   └── generate_image.py  # Image generation tool
└── references/
    └── visual-style-guide.md # Image templates
```

## Resources

- [SKILL.md](SKILL.md) - Detailed AI instructions
- [Visual Style Guide](references/visual-style-guide.md) - Image templates
- [WORKFLOW.md](WORKFLOW.md) - Complete workflow guide

---

**Happy Writing!** 📝✨
