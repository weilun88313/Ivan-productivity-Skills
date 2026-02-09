# PPTX Skill - AI-Powered Presentation Generator

> Transform documents into stunning presentations with AI-generated slides

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

The **PPTX Skill** is an AI-powered presentation creation tool that uses **Gemini 3 Pro** to generate high-quality, visually consistent slide images with embedded text. It follows a Linear-inspired design system with dark mode aesthetics and technical data visualization.

### Key Features

- 🎨 **AI-Generated Slides** - Full-bleed slide images with text and visuals baked in
- 🌙 **Linear Design System** - Dark mode, matte finish, #6B75FF accent color
- 🧠 **Intelligent Templates** - Auto-detects slide types (cover, content, data, closing)
- 📊 **Flexible Density** - Low-density (2-3 points) or high-density (4-6 points) content
- 🌍 **Multi-language** - Supports Chinese and English content
- 🚀 **4K Resolution** - Ultra-high detail (3840x2160)

## Quick Start

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Install required packages
pip install requests python-pptx markitdown[pptx]
```

### Environment Setup

Set your Gemini API key:

```bash
export GEMINI_API_KEY='your_api_key_here'
```

### Basic Usage

```bash
# 1. Create a plan file (ppt_plan.json)
# See "Plan File Format" section below

# 2. Generate slide images from plan
python scripts/ppt_img_gen.py workspace/ppt_plan.json workspace/output/images

# 3. Convert images to PowerPoint
python scripts/images2pptx.py workspace/output/images workspace/output/presentation.pptx
```

## Plan File Format

Create a `ppt_plan.json` file with the following structure:

```json
[
  {
    "slide_number": 0,
    "title": "Your Presentation Title",
    "content": [
      "Subtitle or tagline",
      "Date and author info"
    ],
    "image_concept": "Cover slide with large centered title, elegant abstract background with geometric shapes"
  },
  {
    "slide_number": 1,
    "title": "Key Insights",
    "content": [
      "Market size: $394B → $887.6B",
      "Annual growth: 15% CAGR",
      "Core challenge: ROI control"
    ],
    "image_concept": "Content slide with title at top left, three bullet points on left side, futuristic data visualization on right"
  },
  {
    "slide_number": 2,
    "title": "Thank You",
    "content": [
      "Your Company",
      "contact@yourcompany.com"
    ],
    "image_concept": "Closing slide with centered title, contact info below, subtle fade-out effect"
  }
]
```

### Plan File Guidelines

- **slide_number**: Sequential number starting from 0
- **title**: Slide title (in target language)
- **content**: Array of 2-6 bullet points (based on density preference)
- **image_concept**: Description of the complete slide in English
  - Describe text placement and visual elements
  - Be specific about layout and composition
  - AI will generate the complete slide with text embedded

## Architecture

```
pptx/
├── README.md              # This file
├── SKILL.md               # Detailed skill documentation
└── scripts/
    ├── gemini_api.py      # Shared Gemini API client
    ├── nano_banana.py     # Single image generation tool
    ├── ppt_img_gen.py     # Batch slide generation from plan
    └── images2pptx.py     # Images to PowerPoint converter
```

## Scripts Reference

### 1. `ppt_img_gen.py` - Generate Slide Images

Generate slide images from a plan file:

```bash
python scripts/ppt_img_gen.py <plan_file> <output_dir> [--delay SECONDS]
```

**Arguments:**
- `plan_file`: Path to the plan JSON file
- `output_dir`: Directory to save generated images
- `--delay`: Delay between API calls in seconds (default: 1.0)

**Example:**
```bash
python scripts/ppt_img_gen.py plan.json ./output/images --delay 1.5
```

**Output:**
- `slide_00.png` - Cover slide
- `slide_01.png` - First content slide
- `slide_02.png` - Second content slide
- ...
- `slide_N.png` - Closing slide

### 2. `images2pptx.py` - Create PowerPoint

Convert a directory of images to PowerPoint:

```bash
python scripts/images2pptx.py <image_dir> <output_file>
```

**Arguments:**
- `image_dir`: Directory containing slide images
- `output_file`: Output .pptx file path

**Example:**
```bash
python scripts/images2pptx.py ./output/images ./output/presentation.pptx
```

### 3. `nano_banana.py` - Single Image Generation

Generate a single image for testing:

```bash
python scripts/nano_banana.py --prompt "Test prompt" --output_dir ./output [--filename image.png]
```

**Arguments:**
- `--prompt`: Text prompt for image generation (required)
- `--output_dir`: Directory to save the image (required)
- `--filename`: Output filename (default: image.png)
- `--model`: Model name (default: models/gemini-3-pro-image-preview)

## Design System

### Visual Style

| Element | Specification |
|---------|---------------|
| **Style** | Linear-inspired, minimalist, dark mode |
| **Colors** | Charcoal (#1a1a1a → #0a0a0a), Accent #6B75FF |
| **Typography** | Bold sans-serif titles (white), regular content (90% white) |
| **Background** | Subtle tech grid (5% opacity) |
| **Elements** | Floating 3D shapes, abstract data viz |
| **Resolution** | 4K (3840x2160) |

### Slide Types

#### Cover Slides
- Centered or top-left composition
- Large title, smaller subtitle/date
- Minimal abstract background

#### Content Slides
- Left-right split layout (50/50)
- Title top-left, content left side
- Visuals right side

#### Data Slides
- Split-screen design (40/60)
- Title top-left, data left 40%
- Large 3D visualization right 60%

#### Closing Slides
- Centered composition
- Large title, contact info below
- Fade-out visual effect

## Content Density

### Low Density (Recommended)
- **Points per slide**: 2-3
- **Text length**: 5-10 words per point
- **Best for**: Executive presentations, pitches, overviews
- **Style**: Minimal text, maximum visual impact

**Example:**
```json
{
  "title": "Core Challenges",
  "content": [
    "ROI Uncertainty: 70% lead loss",
    "Data Silos: Fragmented information",
    "Decision Blindness: Lack of real-time intel"
  ]
}
```

### High Density (Detailed)
- **Points per slide**: 4-6
- **Text length**: 10-20 words per point
- **Best for**: Internal reports, documentation, analysis
- **Style**: Comprehensive details for self-reading

**Example:**
```json
{
  "title": "Core Challenges",
  "content": [
    "ROI Uncertainty: 70% of trade show leads lost within 7 days, unable to track conversion",
    "Data Silos: Exhibitor, organizer, service provider data scattered across platforms",
    "Decision Blindness: 87% of participation decisions based on past experience vs real-time intel",
    "Cost Opacity: Booth, setup, staffing costs unclear, difficult to optimize budgets"
  ]
}
```

## Language Support

### Chinese (中文)
- All `title` and `content` fields in Chinese
- `image_concept` always in English (for AI compatibility)

```json
{
  "title": "核心发现",
  "content": [
    "全球市场规模：$394B → $887.6B",
    "年增长率：15% CAGR"
  ],
  "image_concept": "Content slide with title at top left..."
}
```

### English
- All `title` and `content` fields in English
- `image_concept` in English

```json
{
  "title": "Key Insights",
  "content": [
    "Global market size: $394B → $887.6B",
    "Annual growth rate: 15% CAGR"
  ],
  "image_concept": "Content slide with title at top left..."
}
```

## Troubleshooting

### API Key Not Found
```
Error: GEMINI_API_KEY environment variable not set.
```

**Solution:**
```bash
export GEMINI_API_KEY='your_api_key_here'
```

### API Rate Limiting
If you encounter rate limiting, increase the delay:

```bash
python scripts/ppt_img_gen.py plan.json output --delay 2.0
```

### Image Generation Failures
- Check your internet connection
- Verify API key is valid
- Ensure plan.json is valid JSON format
- Try simpler `image_concept` descriptions

### Invalid JSON Format
```
Error: Invalid JSON in plan file
```

**Solution:**
- Validate JSON syntax with a linter
- Ensure no trailing commas
- Check all strings are properly quoted

## Advanced Usage

### Custom Prompts

Modify `GLOBAL_VISUAL_LANGUAGE` in `ppt_img_gen.py` to customize the visual style:

```python
GLOBAL_VISUAL_LANGUAGE = """
Your custom design system rules here...
"""
```

### Custom Slide Templates

Add new slide types to `PAGE_TEMPLATES` in `ppt_img_gen.py`:

```python
PAGE_TEMPLATES = {
    "cover": "...",
    "content": "...",
    "data": "...",
    "closing": "...",
    "custom": "Your custom template..."  # Add here
}
```

### Batch Processing

Process multiple presentations:

```bash
for plan in plans/*.json; do
  name=$(basename "$plan" .json)
  python scripts/ppt_img_gen.py "$plan" "output/$name/images"
  python scripts/images2pptx.py "output/$name/images" "output/$name.pptx"
done
```

## Reading Existing Presentations

Extract text from existing PowerPoint files:

```bash
python -m markitdown presentation.pptx
```

## Best Practices

1. **Plan First**: Always create a detailed plan file before generating images
2. **Test Single Slides**: Use `nano_banana.py` to test image concepts before batch generation
3. **Clear Image Concepts**: Be specific in your `image_concept` descriptions
4. **Consistent Density**: Keep content density consistent across slides
5. **Cover & Closing**: Always include slide_number 0 (cover) and N (closing)
6. **Rate Limiting**: Use appropriate delays to avoid API throttling

## Examples

### Example 1: Quick Pitch Deck (Low Density)

```json
[
  {
    "slide_number": 0,
    "title": "Product Launch 2026",
    "content": ["Your Company", "February 2026"],
    "image_concept": "Modern tech cover with title centered, minimal geometric shapes"
  },
  {
    "slide_number": 1,
    "title": "The Problem",
    "content": [
      "70% of users struggle with X",
      "Manual process takes 5+ hours",
      "$2B market opportunity"
    ],
    "image_concept": "Problem slide with bullet points left, frustrated user visualization right"
  },
  {
    "slide_number": 2,
    "title": "Our Solution",
    "content": [
      "AI-powered automation",
      "10x faster processing",
      "Easy integration"
    ],
    "image_concept": "Solution slide with features left, glowing product interface right"
  },
  {
    "slide_number": 3,
    "title": "Let's Talk",
    "content": ["contact@yourcompany.com"],
    "image_concept": "Clean closing slide with centered contact info"
  }
]
```

### Example 2: Detailed Report (High Density)

```json
[
  {
    "slide_number": 0,
    "title": "Q4 Market Analysis",
    "content": ["Internal Report", "December 2025"],
    "image_concept": "Professional cover with title, data flow background"
  },
  {
    "slide_number": 1,
    "title": "Market Dynamics",
    "content": [
      "Total addressable market expanded 23% YoY to $887.6B driven by digital transformation",
      "Key growth sectors: Enterprise SaaS (45%), AI/ML infrastructure (32%), Cybersecurity (28%)",
      "Regional performance: APAC +35%, North America +18%, EMEA +22%",
      "Competitive landscape intensified with 12 new entrants in Q3-Q4"
    ],
    "image_concept": "Data-rich slide with detailed bullet points left, 3D growth chart right"
  }
]
```

## Contributing

Contributions are welcome! Please ensure:
- Code follows existing style
- Error handling is robust
- Documentation is updated
- Examples are provided

## License

MIT License - See LICENSE file for details

## Support

For issues and questions:
- Check this README first
- Review SKILL.md for detailed documentation
- File an issue with reproduction steps

## Changelog

### v2.0.0 (2026-02-08)
- ✅ Removed hardcoded API keys
- ✅ Refactored to shared API client (DRY principle)
- ✅ Improved error handling and user feedback
- ✅ Simplified architecture (removed unused design_system.py)
- ✅ Updated documentation to match implementation

### v1.0.0 (2026-02-03)
- Initial release with AI-powered slide generation
- Linear design system
- Multi-language support
