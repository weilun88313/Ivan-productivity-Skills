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

# Set up Gemini API key
export GEMINI_API_KEY='your_api_key_here'

# OR add to ~/.claude/lensmor_secrets.json
{
  "NANO_API_KEY": "your_api_key_here"
}
```

### Basic Usage

**Request a Blog Post**

```
"Write a blog post about email marketing best practices"
```

**Generate Images**

```bash
# Cover image
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Abstract email marketing data visualization, flowing connections, Linear dark mode aesthetic" \
  --output_dir workspace/blog/images \
  --filename cover

# Inline images (repeat 3-5 times)
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Email inbox interface wireframe, clean UI mockup, dark mode" \
  --output_dir workspace/blog/images \
  --filename inline_1
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

[Article content starts here]
```

## Formatting Standards

- **Paragraphs**: Maximum 3-4 lines, one idea each
- **Headers**: H2 for main sections, H3 for subsections
- **Lists**: Bullet points or numbered for steps
- **Pro Tips**: Minimum 3 per article
- **Tables**: Use markdown tables for comparisons

## Image Generation

### Visual Style

All images follow the **Linear dark mode aesthetic**:

- **Style**: Minimalist, technical, modern, abstract
- **Colors**: Deep charcoal backgrounds (#1a1a1a), violet-blue accents (#6B75FF)
- **Elements**: Abstract shapes, data visualizations, geometric forms
- **Quality**: 16:9 aspect ratio, high resolution (2K+)
- **Text**: Minimal keywords only

### Image Requirements

- **Cover Image**: Abstract header with Linear aesthetic
- **Inline Images**: Minimum 3 per article supporting content sections

Use complete 5-paragraph structured templates from [references/visual-style-guide.md](references/visual-style-guide.md)

### Generation Script

```bash
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Your detailed prompt here" \
  --output_dir "path/to/output" \
  --filename "image_name"
```

## SEO Best Practices

- **Title**: 50-60 characters, keyword-rich
- **Meta Description**: 150-160 characters with benefit and CTA
- **Slug**: `/blog/[category]/[keyword-slug]`
- **Keywords**: Primary in title/H2/first paragraph, 1-2% density
- **Internal Links**: 2-3 related articles per post

## Workflow Integration

Works seamlessly with [webflow-blog-publisher](../webflow-blog-publisher):

```bash
# 1. Write blog post (using AI)
# 2. Generate images
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "..." \
  --output_dir workspace/blog/images

# 3. Publish to Webflow
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

## Troubleshooting

### API Key Not Found

```bash
# Option 1: Environment variable
export GEMINI_API_KEY='your_key'

# Option 2: Secrets file
echo '{"NANO_API_KEY": "your_key"}' > ~/.claude/lensmor_secrets.json
```

### Image Generation Fails

- Simplify prompt if timeout occurs
- Check internet connection
- Avoid brand names or copyrighted content

### Content Quality

- Specify word count and target audience
- Request specific tone: "Write in professional blog style"
- Include data points and statistics

## File Structure

```
blog-writer/
├── README.md                  # This file
├── SKILL.md                   # AI workflow instructions
├── scripts/
│   ├── gemini_api.py         # Shared API client
│   └── generate_image.py     # Image generation tool
└── references/
    └── visual-style-guide.md # Detailed visual guidelines
```

## Resources

- [SKILL.md](SKILL.md) - Detailed AI instructions
- [Visual Style Guide](references/visual-style-guide.md) - Image templates
- [Webflow Blog Publisher](../webflow-blog-publisher) - Publishing integration

---

**Happy Writing!** 📝✨
