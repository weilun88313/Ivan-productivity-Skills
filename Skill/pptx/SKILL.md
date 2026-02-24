---
name: pptx
description: "Create new PowerPoint presentations (.pptx) with AI-generated slide images"
---

# PPTX Creation with Gemini AI

## Overview

AI-powered presentation creation using **Gemini 3 Pro**. Generates 4K slide images with embedded text following a Linear-inspired dark mode design, then assembles them into a `.pptx` file.

## Workflow

When the user requests a PPT, follow this protocol strictly. **DO NOT** immediately run generation scripts.

### Step 1: Analyze & Propose (Single Confirmation)

**Your Role**: World-class Presentation Designer. Analyze the user's document, then present a **single combined proposal** for the user to confirm or adjust:

```
I've analyzed your document. Here's my recommended plan:

- **Slides**: 1 cover + [N] content + 1 closing = [N+2] total
  • Slide 1: [Topic]
  • Slide 2: [Topic]
  • ...
- **Information Density**: Low (2-3 points/slide, best for presentations)
- **Language**: [Chinese/English based on source document]

Would you like to adjust anything (slide count, density, language)?
```

**Slide count guidelines** (content slides only, excluding cover & closing):
- Short summary: 5-8
- Medium analysis: 8-12
- Detailed report: 12-18

**Density options**:
- **Low**: 2-3 items per slide, 5-10 words each (presentations, pitches)
- **High**: 4-6 items per slide, 10-20 words each (reports, analysis)

Proceed to Step 2 only after user confirms.

### Step 2: Generate Plan JSON

Create `ppt_plan.json` in the workspace. Strict JSON format:

```json
[
  {
    "slide_number": 0,
    "title": "Presentation Title",
    "content": ["Subtitle", "Date/Author"],
    "image_concept": "Cover slide with large centered title, abstract geometric background"
  },
  {
    "slide_number": 1,
    "title": "Section Title",
    "content": ["Point 1", "Point 2", "Point 3"],
    "image_concept": "Content slide with title top left, three key points on left, data visualization on right"
  },
  {
    "slide_number": N,
    "title": "Thank You / 谢谢",
    "content": ["Contact info", "Company name"],
    "image_concept": "Minimalist closing slide with centered thank you text, subtle fade-out elements"
  }
]
```

**Rules**:
- Always include cover (slide 0) and closing (last slide)
- `title` and `content`: in the user's chosen language
- `image_concept`: **always in English** for better AI compatibility
- `image_concept` must describe the complete slide: text placement, visual elements, and layout
- Be specific: "3D bar chart with two columns" not just "a chart"

### Step 3: Execute

1. **Generate slide images**:
   ```bash
   python Skill/pptx/scripts/ppt_img_gen.py workspace/ppt_plan.json workspace/project_name/images
   ```
   Options: `--retries 3` (default), `--delay 1.0` (seconds), `--parallel N` (concurrent workers)

2. **Assemble PowerPoint**:
   ```bash
   python Skill/pptx/scripts/images2pptx.py workspace/project_name/images workspace/project_name/presentation.pptx
   ```

## Reading Existing Presentations

```bash
python -m markitdown path-to-file.pptx
```

## Dependencies

```bash
pip install requests python-pptx markitdown[pptx]
```

## Environment

```bash
export GEMINI_API_KEY='your_api_key_here'
```
