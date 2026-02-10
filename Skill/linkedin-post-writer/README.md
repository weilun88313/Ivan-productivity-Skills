[English](README.md) | [中文](README.zh.md)

---


# LinkedIn Post Writer

> Transform fragmented ideas into engaging LinkedIn posts with AI-generated visuals

## Overview

The **LinkedIn Post Writer** skill helps you create professional, engaging LinkedIn posts from scattered thoughts or general topics. It combines content structuring expertise with AI-generated images to produce publish-ready posts that align with your personal brand.

### Key Features

- ✍️ **Two Creation Modes** - From fragments to post, or from topic to full narrative
- 🎨 **AI-Generated Images** - Professional 16:9 or 1:1 images optimized for LinkedIn
- 📝 **Template-Based** - 5 proven post structures for different content types
- 💡 **Brand Consistency** - Maintains approachable, professional voice
- 🎯 **Optimal Length** - 300-800 characters for maximum engagement
- 🔄 **Complete Workflow** - From ideation to final post with image

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

**Scenario 1: From Fragmented Ideas**

```
"Help me write a LinkedIn post. Ideas:
- AI changes product design workflow
- Useful for brainstorming
- Can analyze user interviews
- But can't rely on it completely"
```

**Scenario 2: From Topic**

```
"Write a LinkedIn post about team collaboration"
```

**Generate Image**

```bash
python scripts/generate_image.py \
  --prompt "Your post content or image description" \
  --aspect-ratio 16:9 \
  --output_dir output \
  --filename post_image
```

## Post Structures

### 5 Template Types

1. **Personal Story → Insight**
   - Share experience, extract lesson
   - Example: Team moment that taught you something

2. **Observation → Analysis**
   - Notice pattern, provide interpretation
   - Example: Industry trend analysis

3. **Question → Exploration**
   - Pose question, explore perspectives
   - Example: "Should PMs know how to code?"

4. **Tip List → Value Delivery**
   - Share actionable advice with context
   - Example: "3 ways I use AI in product design"

5. **Contrarian View → Debate**
   - Challenge assumption, invite discussion
   - Example: "Unpopular opinion: MVP is outdated"

## Reference Files

- **`references/brand_persona.md`** - Complete brand voice and writing style guide
- **`references/post_templates.md`** - Detailed post structures and examples
- **`scripts/generate_image.py`** - Image generation tool
- **`scripts/gemini_api.py`** - Shared Gemini API client

---

**Happy Posting!** 📝✨
