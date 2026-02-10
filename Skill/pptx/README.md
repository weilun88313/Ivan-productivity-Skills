[English](README.md) | [中文](README.zh.md)

---


# PPTX Skill - AI-Powered Presentation Generator

> Transform documents into stunning presentations with AI-generated slides

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

AI-powered presentation creation using **Gemini 3 Pro** to generate high-quality slide images with embedded text. Follows Linear-inspired design with dark mode aesthetics.

### Key Features

- 🎨 **AI-Generated Slides** - Full-bleed images with text and visuals
- 🌙 **Linear Design System** - Dark mode, #6B75FF accent color
- 🧠 **Intelligent Templates** - Auto-detects slide types
- 📊 **Flexible Density** - Low (2-3 points) or high (4-6 points) content
- 🌍 **Multi-language** - Chinese and English support
- 🚀 **4K Resolution** - Ultra-high detail (3840x2160)

## Quick Start

### Prerequisites

```bash
pip install requests python-pptx markitdown[pptx]
export GEMINI_API_KEY='your_api_key_here'
```

### Usage

```bash
# 1. Create plan file (ppt_plan.json)
# 2. Generate slide images
python scripts/ppt_img_gen.py workspace/ppt_plan.json workspace/output/images

# 3. Convert to PowerPoint
python scripts/images2pptx.py workspace/output/images workspace/output/presentation.pptx
```

## Plan File Format

Create `ppt_plan.json`:

```json
[
  {
    "slide_number": 0,
    "title": "Your Title",
    "content": ["Subtitle", "Date"],
    "image_concept": "Cover slide with centered title, abstract background"
  },
  {
    "slide_number": 1,
    "title": "Key Points",
    "content": ["Point 1", "Point 2", "Point 3"],
    "image_concept": "Content slide with title top left, bullets left, visualization right"
  }
]
```

**Guidelines:**
- **slide_number**: Sequential from 0
- **title**: Slide title (target language)
- **content**: 2-6 bullet points
- **image_concept**: Complete slide description in English

## Scripts

### Generate Slides
```bash
python scripts/ppt_img_gen.py <plan_file> <output_dir> [--delay SECONDS]
```

### Create PowerPoint
```bash
python scripts/images2pptx.py <image_dir> <output_file>
```

### Test Single Image
```bash
python scripts/nano_banana.py --prompt "Test" --output_dir ./output
```

## Design System

**Visual Style:**
- Linear-inspired, minimalist dark mode
- Colors: Charcoal (#1a1a1a), Accent #6B75FF
- 4K resolution (3840x2160)

**Slide Types:**
- **Cover**: Centered/top-left, large title, minimal background
- **Content**: 50/50 split, title/content left, visuals right
- **Data**: 40/60 split, data left, 3D viz right
- **Closing**: Centered, title + contact info

## Content Density

**Low (Recommended)**: 2-3 points, 5-10 words each - Best for pitches
**High (Detailed)**: 4-6 points, 10-20 words each - Best for reports

## Troubleshooting

- **API Key Error**: `export GEMINI_API_KEY='your_key'`
- **Rate Limiting**: Increase delay with `--delay 2.0`
- **Invalid JSON**: Check syntax, remove trailing commas

## File Structure

```
pptx/
├── README.md              # This file
├── SKILL.md               # Detailed documentation
└── scripts/
    ├── gemini_api.py      # API client
    ├── ppt_img_gen.py     # Slide generator
    └── images2pptx.py     # PowerPoint converter
```

## Resources

- [SKILL.md](SKILL.md) - Detailed documentation
- Read existing PPTs: `python -m markitdown presentation.pptx`
