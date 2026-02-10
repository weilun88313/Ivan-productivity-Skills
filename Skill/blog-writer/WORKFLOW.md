# Blog Creation Workflow

> Complete workflow for creating and publishing SEO-optimized blog posts

This document describes the end-to-end workflow using **blog-writer** and **webflow-blog-publisher** skills.

## Overview

```
User Request → Brand Check → Blog Writing → Image Generation → Publishing to Webflow
     ↓              ↓              ↓                ↓                    ↓
  Topic Idea   Product Info   professional blog Style    AI-Generated        Webflow CMS
              (if needed)      Content         Illustrations       (Live/Draft)
```

## Quick Start

### 0. Brand Guidelines Check (If Product-Related)

**Before writing**, determine if content references Lensmor or product features:

```bash
# If YES, read brand guidelines first:
- /Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/SKILL.md
- /Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/resources/product-details.md

# Extract:
- Current product features
- Value proposition
- Target audience
- Competitive positioning
- Correct terminology
```

**If NO** (generic industry content), skip to Step 1.

### 1. Write a Blog Post

Ask AI to write a blog post:
```
"Write a blog post about email marketing best practices"
```

The AI will:
- Create professional blog-style content
- Generate a metadata block (title, slug, meta description)
- Add image placeholders
- Save as markdown file

### 2. Generate Images

Generate cover and inline images:
```bash
# Cover image
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "Abstract email marketing visualization, data flow, Linear dark style" \
  --output_dir workspace/blog/images

# Inline images (repeat for each)
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "Email inbox interface wireframe, clean UI mockup" \
  --output_dir workspace/blog/images
```

### 3. Publish to Webflow

```bash
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

## Detailed Workflow

### Phase 1: Content Creation

**Tool**: `blog-writer`

1. **Define Topic**: Clear, specific blog topic
2. **Generate Content**: AI creates structured blog post
3. **Review Structure**:
   - Hook introduction
   - Problem/solution framework
   - Step-by-step guide or listicle
   - Pro Tips (minimum 3)
   - Clear CTA

**Output**: `article.md` with metadata block

### Phase 2: Visual Assets

**Tool**: `blog-writer/scripts/generate_image.py`

1. **Cover Image** (Required):
   - Abstract, no text
   - 16:9 aspect ratio
   - Linear dark mode style

2. **Inline Images** (Minimum 3):
   - Support content sections
   - Diagrams, wireframes, visualizations
   - Consistent visual style

**Output**: PNG files in `/images` directory

### Phase 3: Publishing

**Tool**: `webflow-blog-publisher`

1. **Prepare**:
   - Ensure images are referenced correctly in markdown
   - Verify metadata (slug, meta description)

2. **Publish**:
   - Script uploads images to Webflow Assets
   - Converts markdown to HTML
   - Creates CMS item (draft or published)

3. **Verify**:
   - Check Webflow CMS dashboard
   - Review live/staging site

## File Structure

```
workspace/
└── blog/
    ├── article.md              # Blog content with metadata
    └── images/
        ├── cover.png           # Cover image
        ├── diagram_1.png       # Inline image 1
        ├── diagram_2.png       # Inline image 2
        └── diagram_3.png       # Inline image 3
```

## Markdown Format

```markdown
# The Ultimate Guide to Email Marketing Best Practices

**Slug**: /blog/strategy/email-marketing-best-practices
**Meta Description**: Learn 10 proven email marketing strategies...
**Cover Image**:
![Email marketing visualization](images/cover.png)

---

## Introduction

Email marketing remains one of the most effective channels...

![Email inbox wireframe](images/diagram_1.png)

## Best Practice 1: Segment Your Audience

**Pro Tip**: Start with basic demographic segmentation...
```

## Prerequisites

### For professional blog Blog Writer
```bash
pip install requests

# Set API key
export GEMINI_API_KEY='your_api_key'
# OR add to ~/.claude/lensmor_secrets.json
```

### For Webflow Blog Publisher
```bash
pip install requests markdown

# Configure secrets in ~/.claude/lensmor_secrets.json:
{
  "WEBFLOW_API_TOKEN": "your_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "collection_id",
  "WEBFLOW_SITE_ID": "site_id"
}
```

## Best Practices

### Content
- **Length**: 1500-3000 words for SEO
- **Structure**: Clear H2/H3 hierarchy
- **Tone**: Professional yet accessible
- **CTAs**: Include 1-2 clear calls-to-action

### Images
- **Quantity**: 1 cover + 3-5 inline images
- **Style**: Consistent Linear dark mode aesthetic
- **Format**: PNG, 16:9 aspect ratio
- **Alt Text**: Descriptive for accessibility

### SEO
- **Slug**: Keyword-rich, readable URLs
- **Meta**: 150-160 characters, compelling
- **Keywords**: Natural integration, not stuffed
- **Headers**: Descriptive, search-friendly

## Troubleshooting

### Image Generation Fails
**Problem**: API timeout or error

**Solution**:
- Check GEMINI_API_KEY is set
- Verify internet connection
- Try simpler prompt
- Increase timeout in script

### Webflow Upload Fails
**Problem**: Images not uploading

**Solution**:
- Verify WEBFLOW_SITE_ID is set
- Check API token permissions
- Ensure image files exist
- Try uploading one image manually first

### Publishing as Draft Instead of Live
**Default**: Script creates drafts

**To Publish Live**: Add `--publish` flag
```bash
python publish_to_webflow.py --file article.md --publish
```

## Advanced Usage

### Batch Image Generation
```bash
# Generate multiple images
for prompt in "prompt1" "prompt2" "prompt3"; do
  python generate_image.py --prompt "$prompt" --output_dir images
done
```

### Custom Writer Profile
```bash
# Publish with specific writer
python publish_to_webflow.py \
  --file article.md \
  --writer "John Doe" \
  --category playbooks
```

### Re-publish Updated Content
1. Update markdown file
2. Re-run publish script
3. May create duplicate - manually delete old version in Webflow CMS

## Categories

Available categories (customize in Webflow):
- `strategy` - Strategic guides and frameworks
- `playbooks` - Step-by-step tactical guides
- `teardowns` - Case studies and analyses

## Workflow Tips

1. **Write First, Images Later**: Focus on content quality first
2. **Batch Image Generation**: Generate all images in one session
3. **Test as Draft**: Always publish as draft first, review, then make live
4. **Track Performance**: Monitor which categories and topics perform best
5. **Iterate**: Refine prompts based on image quality

## Resources

- [professional blog Blog Writer SKILL.md](blog-writer/SKILL.md) - Content guidelines
- [professional blog Blog Writer README.md](blog-writer/README.md) - User guide
- [Webflow Blog Publisher SKILL.md](webflow-blog-publisher/SKILL.md) - Technical docs
- [Webflow Blog Publisher README.md](webflow-blog-publisher/README.md) - User guide

## Support

For issues:
1. Check this workflow guide
2. Review individual skill README files
3. Verify API keys and credentials
4. Test each step independently

---

**Status**: ✅ Optimized workflow documentation
**Version**: 2.0
**Last Updated**: 2026-02-08
