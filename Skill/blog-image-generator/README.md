# Blog Image Generator

**Unified AI image generation for all platforms** - A standalone skill that generates high-quality, consistent images for blog posts, social media, and presentations.

## Overview

This skill consolidates image generation functionality from multiple skills (blog-writer, linkedin-post-writer, twitter-post-writer, jike-post-writer, pptx) into a single, unified service.

### Key Features

- **Multiple API Support**: Gemini (primary) with automatic Fal.ai fallback
- **Platform-Specific Styles**: Optimized prompts for each platform
- **Linear Dark Mode Aesthetic**: Consistent visual style across all images
- **CLI & Python API**: Use standalone or import into other skills
- **Batch Generation**: Generate multiple images at once

## Installation

1. Clone this skill to your `Skill/` directory:
```bash
cd /Users/ivan/Documents/Ivan_Skills/Skill/blog-image-generator
```

2. Install dependencies:
```bash
pip install requests
```

3. Configure API keys in `~/.claude/lensmor_secrets.json`:
```json
{
  "NANO_API_KEY": "your-gemini-api-key",
  "FAL_KEY": "your-fal-ai-key"
}
```

Or set environment variables:
```bash
export GEMINI_API_KEY="your-gemini-api-key"
export FAL_KEY="your-fal-ai-key"
```

## Usage

### Command Line Interface

Generate a single image:
```bash
python scripts/generate.py \
  --platform blog \
  --type cover \
  --prompt "Email Marketing Best Practices" \
  --output cover.png
```

Batch generation:
```bash
python scripts/batch.py \
  --platform blog \
  --prompts prompts.json \
  --output_dir images/
```

### Python API

```python
from Skill.blog_image_generator.scripts.image_generator import ImageGenerator
from Skill.blog_image_generator.prompts import BlogPrompts, LinkedInPrompts

# Initialize generator
gen = ImageGenerator()

# Generate blog cover image
prompt = BlogPrompts.cover("Email Marketing Best Practices")
image = gen.generate(prompt, style="blog", aspect_ratio="16:9")
gen.save(image, "cover.png")

# Generate LinkedIn post image
prompt = LinkedInPrompts.post("Excited to announce our new product launch!")
image = gen.generate(prompt, style="linkedin", aspect_ratio="16:9")
gen.save(image, "linkedin_post.png")
```

## Platform Support

| Platform | Aspect Ratio | Style | Use Case |
|----------|--------------|-------|----------|
| `blog` | 16:9 | Linear Dark Mode | Blog cover/inline images |
| `linkedin` | 16:9 | Linear Dark Mode / Photo Infographic | LinkedIn posts |
| `twitter` | 16:9, 1:1, 4:3 | Viral High-Impact | Twitter/X tweets |
| `jike` | 1:1 | Social Chinese | Jike posts |
| `pptx` | 16:9 | Linear Presentation | PowerPoint slides |

### LinkedIn Image Styles

LinkedIn posts support **three visual styles**:

| Style | Type | When to Use |
|-------|------|-------------|
| **Linear Dark Mode** | `inline` | Tech/AI/abstract concepts, frameworks, formulas (no person) |
| **Photo Infographic** | `photo_infographic` | Personal branding with your photo + Apple-style minimal labels |
| **Photo + Info** | `photo_info` | Personal stories, human-centric content |

**For LinkedIn posts, generate BOTH Linear and Photo Infographic styles for user to choose from.**

## Prompt Templates

### Blog Images

```python
from Skill.blog_image_generator.prompts import BlogPrompts

# Cover image - purely abstract
cover_prompt = BlogPrompts.cover("Your Blog Title")

# Inline image - conceptual visualization
inline_prompt = BlogPrompts.inline("Data flow visualization showing user journey")
```

### Social Media Images

```python
from Skill.blog_image_generator.prompts import LinkedInPrompts, TwitterPrompts, JikePrompts

# LinkedIn - Linear Dark Mode (abstract, no person)
linkedin_prompt = LinkedInPrompts.inline("Three interconnected stages: Input, Process, Output")

# LinkedIn - Photo Infographic (with person photo, Apple-style minimalism)
# emotion: thinking, excited, shocked, worried, confused, amazed
photo_prompt = LinkedInPrompts.photo_infographic(
    topic="AI Revolution in 2025",
    emotion="thinking",
    labels=["1M TOKENS", "AGENT PLANNING", "CODE EXECUTION"],
    photo_url="/Users/ivan/Documents/Ivan_Skills/Skill/blog-image-generator/Avatar/1760175502370.jpeg"
)

# Twitter
twitter_prompt = TwitterPrompts.tweet("Your tweet content", aspect_ratio="16:9")

# Jike
jike_prompt = JikePrompts.post("你的即刻内容")
```

### Presentation Images

```python
from Skill.blog_image_generator.prompts import PPTPrompts

slide_prompt = PPTPrompts.slide(
    title="Data Analysis",
    content=["Key insight 1", "Key insight 2"],
    image_concept="Abstract data visualization",
    slide_type="content"
)
```

## Visual Style System

All generated images follow the **Linear Dark Mode** aesthetic:

- **Background**: Deep charcoal (#1a1a1a to #0a0a0a)
- **Accent Color**: Violet-blue (#6B75FF)
- **Quality**: Minimalist, matte finish, high detail
- **Elements**: Abstract geometric shapes, data flow, subtle grid

See `visual-style-guide.md` for complete specifications.

## CLI Options

### generate.py

```
--platform     Platform: blog, linkedin, twitter, jike, pptx
--type         Image type: cover, inline, post, slide, photo_infographic, photo_info
--prompt       Text description or title
--output       Output file path
--aspect-ratio Aspect ratio (default: 16:9)
--quality      Image quality: 2K, 4K (default: 2K)

# Photo Infographic specific options:
--labels       Comma-separated labels (e.g., "AI WINS,300%")
--emotion      Facial expression: thinking, shocked, surprised, excited, worried, confused, headache, amazed
--photo-url    URL or path to your photo
```

### Photo Infographic Example

```bash
python scripts/generate.py \
  --platform linkedin \
  --type photo_infographic \
  --prompt "The Learning Formula" \
  --labels "PRE-TRAINING,POST-TRAINING,REINFORCEMENT" \
  --emotion thinking \
  --photo-url "/path/to/your/photo.jpg" \
  --output linkedin_post.png \
  --aspect-ratio 16:9
```

### batch.py

```
--platform     Platform: blog, linkedin, twitter, jike, pptx
--prompts      JSON file with prompts array
--output_dir   Directory for generated images
--delay        Delay between API calls (seconds)
```

## API Fallback Behavior

The generator automatically tries providers in order:

1. **Gemini API** (NANO_API_KEY / GEMINI_API_KEY)
2. **Fal.ai Nano Banana Pro** (FAL_KEY)

If one fails, it automatically tries the next available provider.

## File Structure

```
blog-image-generator/
├── README.md              # This file
├── README.zh.md           # Chinese documentation
├── SKILL.md               # AI instructions
├── scripts/
│   ├── generate.py        # CLI entry point
│   ├── batch.py           # Batch generation
│   └── image_generator.py # Core API client
├── prompts/
│   ├── base.py            # Base templates
│   ├── blog.py            # Blog prompts
│   ├── linkedin.py        # LinkedIn prompts
│   ├── twitter.py         # Twitter prompts
│   ├── jike.py            # Jike prompts
│   └── pptx.py            # PPT prompts
└── styles/
    ├── common.py          # Shared definitions
    ├── linear.py          # Linear blog style
    ├── linkedin.py        # LinkedIn style
    ├── twitter.py         # Twitter style
    ├── jike.py            # Jike style
    └── pptx.py            # PPT style
```

## Integration with Other Skills

After installing, other skills can use the shared service:

```python
# In any skill's script
from Skill.blog_image_generator.scripts.image_generator import ImageGenerator
from Skill.blog_image_generator.prompts import BlogPrompts

gen = ImageGenerator()
prompt = BlogPrompts.cover("Article Title")
image = gen.generate(prompt, style="blog")
```

## Error Handling

The generator handles common errors:

- **Rate Limiting**: Automatic retry with exponential backoff
- **Region Restrictions**: Falls back to alternative provider
- **Timeout**: Configurable timeout (default: 180s)
- **API Errors**: Detailed error messages for debugging

## License

Part of Ivan's Skills collection.

## See Also

- [blog-writer](../blog-writer/) - Generate SEO-optimized blog posts
- [linkedin-post-writer](../linkedin-post-writer/) - Generate LinkedIn content
- [twitter-post-writer](../twitter-post-writer/) - Generate Twitter content
- [content-pipeline](../content-pipeline/) - End-to-end automation workflow
