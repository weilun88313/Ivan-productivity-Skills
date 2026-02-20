[English](README.md) | [中文](README.zh.md)

---


# LinkedIn Post Writer

> Transform fragmented ideas into engaging LinkedIn posts with AI-generated visuals

## Overview

Create professional, engaging LinkedIn posts from scattered thoughts or general topics. Combines content structuring with AI-generated images to produce publish-ready posts.

### Key Features

- ✍️ **Two Creation Modes** - From fragments or topics
- 🎨 **AI-Generated Images** - Professional 16:9 or 1:1 images
- 📝 **5 Proven Templates** - Different post structures for various content types
- 💡 **Brand Consistency** - Approachable, professional voice
- 🎯 **Optimal Length** - 300-800 characters for maximum engagement

## Quick Start

### Prerequisites

```bash
# Install dependencies
pip install requests

# Set up Gemini API key (or configure via secrets file)
export GEMINI_API_KEY='your_api_key_here'
```

### Usage

**From Fragmented Ideas:**
```
"Help me write a LinkedIn post. Ideas:
- AI changes product design workflow
- Useful for brainstorming
- Can't rely on it completely"
```

**From Topic:**
```
"Write a LinkedIn post about team collaboration"
```

**Generate Image (standalone):**
```bash
python scripts/generate_image.py \
  --prompt "Your post content or description" \
  --aspect-ratio 16:9 \
  --output_dir output \
  --filename my_post
```

**With LinkedIn prompt enhancement:**
```bash
python scripts/generate_image.py \
  --prompt "Your post content" \
  --enhance \
  --style "professional, tech-focused" \
  --aspect-ratio 16:9
```

> **Note**: The primary image generation workflow uses the sibling `blog-image-generator` skill. The local `scripts/generate_image.py` is available as a standalone fallback.

## Post Templates

1. **Personal Story → Insight** - Share experience, extract lesson
2. **Observation → Analysis** - Notice pattern, provide interpretation
3. **Question → Exploration** - Pose question, explore perspectives
4. **Tip List → Value** - Share actionable advice
5. **Contrarian View → Debate** - Challenge assumption, invite discussion

## Resources

- **`references/brand_persona.md`** - Brand voice guide
- **`references/post_templates.md`** - Post structures and examples
- **`scripts/generate_image.py`** - Image generation tool

---

**Happy Posting!** 📝✨
