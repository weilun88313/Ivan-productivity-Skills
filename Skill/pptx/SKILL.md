---
name: pptx
description: "Presentation creation. When needs to work with presentations (.pptx files) for creating new presentations, or any other presentation tasks"
---

# PPTX Creation with Gemini AI

## Overview

This skill enables AI-powered presentation creation using the **Gemini 3 Pro** API. The workflow emphasizes visual storytelling through high-quality AI-generated images with embedded text, following brand guidelines.

## Key Features

- **AI-Generated Slides**: Full-bleed slide images with text and visuals baked in
- **Linear Design System**: Dark mode, matte finish, #6B75FF accent color
- **Intelligent Templates**: Auto-detects slide types (cover, content, data, closing)
- **Flexible Density**: Low-density (2-3 points) or high-density (4-6 points) content
- **Multi-language**: Supports Chinese and English content

## Creating a New Presentation

### Interactive Planning Workflow

When the user requests a PPT, **DO NOT** immediately run generation scripts. Follow this 3-step protocol:

#### Step 1: Deep Understanding & Planning

**Your Role**: You are a world-class Presentation Designer, expert at transforming complex documents into logically clear, visually impactful PPT outlines.

**Your Task**:
1. **Analyze the Input**: Thoroughly read the user's document.
2. **Determine Slide Count**: Based on document length and complexity, recommend an appropriate number of **content slides** (excluding cover and closing):
   - Short summary: 5-8 content slides
   - Medium analysis: 8-12 content slides
   - Detailed report: 12-18 content slides

3. **Propose Structure & Get Confirmation**:
   ```
   I've analyzed your document. I recommend a presentation with:
   - **Cover slide** (1)
   - **Content slides** ([N]) covering:
     • Slide 1: [Topic]
     • Slide 2: [Topic]
     • ...
   - **Closing slide** (1)

   **Total: [N+2] slides**

   Does this slide count work for you, or would you prefer more/fewer slides?
   ```

4. **Wait for Slide Count Confirmation**: User may approve or request adjustment.

5. **Ask for Information Density**:
   ```
   What information density would you prefer?

   📊 **Low Density** (Recommended for presentations):
   - 2-3 key points per slide
   - Minimal text, maximum visual impact
   - Best for: Executive presentations, pitches, overviews

   📚 **High Density** (For detailed reports):
   - 4-6 key points per slide
   - More detailed text descriptions
   - Best for: Internal reports, documentation, analysis

   Please choose: Low or High?
   ```

6. **Wait for Density Confirmation**: User selects "Low" or "High".

7. **Ask for Language Preference**:
   ```
   What language would you like for the presentation content?

   🇨🇳 **Chinese (中文)**:
   - All slide titles and content in Chinese

   🇺🇸 **English**:
   - All slide titles and content in English

   Please choose: Chinese or English?
   ```

8. **Wait for Language Confirmation**: User selects "Chinese" or "English".

9. **Proceed to Generation**: Only after all three confirmations (slide count, density, language), proceed to Step 2.

#### Step 2: Plan Generation

Once approved:
1. **Create `ppt_plan.json`**: Construct a JSON file in the workspace with detailed content for each slide.

   **CRITICAL**: Always include a **cover slide** (slide_number: 0) and a **closing slide** (slide_number: N+1) automatically.

   **Information Density Rules**:
   - **Low Density**: 2-3 items in `content` array per slide, concise phrases (5-10 words each)
   - **High Density**: 4-6 items in `content` array per slide, detailed descriptions (10-20 words each)

   **Language Rules**:
   - **Chinese**: All `title` and `content` items must be in Chinese (中文)
   - **English**: All `title` and `content` items must be in English
   - **Note**: `image_concept` is ALWAYS in English for better AI model compatibility

   **Output Format** (strict JSON, no Markdown code blocks):
   ```json
   [
     {
       "slide_number": 0,
       "title": "[Presentation Title]",
       "content": [
         "Subtitle or brief description",
         "Date/Author (optional)"
       ],
       "image_concept": "Minimalist cover design with abstract geometric shapes or data visualization elements in background"
     },
     {
       "slide_number": 1,
       "title": "...",
       "content": ["...", "...", "..."],
       "image_concept": "..."
     },
     ...
     {
       "slide_number": N,
       "title": "Thank You / 谢谢",
       "content": [
         "Contact info (optional)",
         "Company/Team name"
       ],
       "image_concept": "Clean closing slide design with thank you message, minimal abstract elements"
     }
   ]
   ```

   **Cover Slide (slide_number: 0) Requirements**:
   - **title**: The main presentation topic
   - **content**: Subtitle, date, author, or brief description (1-2 lines max)
   - **image_concept**: Focus on title typography and minimal abstract background
   - Example: `"Elegant cover design with large title text, subtle geometric patterns, professional and clean"`

   **Closing Slide (slide_number: N) Requirements**:
   - **title**: "Thank You" or "谢谢" or custom closing message
   - **content**: Contact info, company name, or call-to-action (optional)
   - **image_concept**: Simple, elegant, minimal
   - Example: `"Minimalist thank you slide with centered text, subtle fade-out effect"`

   **Key Requirements for `image_concept`**:
   - **Describe the complete slide**: Include both text content and visual elements
   - **Specify text placement**: Where title and content should appear
   - **Describe visuals**: Abstract elements, data visualizations, geometric patterns
   - **Use English**: For better AI model compatibility
   - **Be specific**: "3D bar chart with two columns, taller on right" instead of "a chart"

   **Examples**:
   ```json
   {
     "slide_number": 0,
     "title": "海外展会行业深度解析",
     "content": [
       "Lensmor 内部报告",
       "2026年2月"
     ],
     "image_concept": "Cover slide with large centered title '海外展会行业深度解析', subtitle 'Lensmor 内部报告' and '2026年2月' below, abstract data flow visualization in background"
   },
   {
     "slide_number": 1,
     "title": "核心发现",
     "content": [
       "全球市场规模：$394B → $887.6B",
       "年增长率：15% CAGR",
       "核心问题：ROI 不可控"
     ],
     "image_concept": "Content slide with title '核心发现' at top left, three bullet points on left side, futuristic global trade show visualization on right with holographic connections"
   },
   {
     "slide_number": 10,
     "title": "谢谢",
     "content": [
       "Lensmor Team",
       "lensmor.com"
     ],
     "image_concept": "Closing slide with centered title '谢谢', 'Lensmor Team' and 'lensmor.com' below, subtle fade-out data visualization elements"
   }
   ```

   **Density Comparison Example**:

   **Low Density (2-3 points, concise)**:
   ```json
   {
     "slide_number": 3,
     "title": "行业核心痛点",
     "content": [
       "ROI 不可控：70%线索流失",
       "数据孤岛：信息碎片化",
       "决策盲区：缺乏实时情报"
     ]
   }
   ```

   **High Density (4-6 points, detailed)**:
   ```json
   {
     "slide_number": 3,
     "title": "行业核心痛点",
     "content": [
       "ROI 不可控：70%的展会线索在7天内流失，无法追踪转化效果",
       "数据孤岛：参展商、主办方、服务商数据分散，缺乏统一平台",
       "决策盲区：87%的参展��策基于历史经验而非实时市场情报",
       "成本黑箱：展位、搭建、人力成本不透明，难以优化预算",
       "竞争情报缺失：无法实时了解竞争对手的参展动态和策略"
     ]
   }
   ```

#### Step 3: Execution

1. **Generate Slide Images**:
   ```bash
   python Skill/pptx/scripts/ppt_img_gen.py workspace/ppt_plan.json workspace/project_name/images
   ```

   This script generates complete slide images with:
   - **Linear-Inspired Style**: Technical data visualization, dark mode, matte finish
   - **Color Palette**: Deep charcoal (#1a1a1a), #6B75FF violet-blue accents
   - **Typography**: Embedded in the image by AI
   - **4K Resolution**: 3840x2160, ultra-high detail
   - **Smart Templates**: Auto-detects cover/content/data/closing slide types

2. **Compile Presentation**:
   ```bash
   python Skill/pptx/scripts/images2pptx.py workspace/project_name/images workspace/project_name/presentation.pptx
   ```

   This script creates a PowerPoint file with images as full-bleed slides (16:9 format).

### Manual/Single Image Generation

For testing or single image generation:
```bash
python Skill/pptx/scripts/nano_banana.py --prompt "Test image concept" --output_dir "output" --filename "test.png"
```

## Design System

The PPT skill uses a centralized visual language to ensure **NotebookLM-level consistency** across all slides.

### Visual Style

| Element | Specification |
|---------|---------------|
| **Style** | Linear-inspired, minimalist, dark mode, matte finish |
| **Colors** | Deep charcoal (#1a1a1a → #0a0a0a), accent #6B75FF |
| **Typography** | Bold sans-serif titles (white), regular content (90% white) |
| **Background** | Subtle tech grid lines (5% opacity) |
| **Elements** | Floating 3D shapes, abstract data visualizations |
| **Resolution** | 4K (3840x2160) |

### Slide Types

**Cover Slides**:
- Centered or top-left composition
- Large title, smaller subtitle/date
- Minimal abstract background

**Content Slides**:
- Left-right split layout
- Title top-left, content left 50%
- Visuals right 50%

**Data Slides**:
- Split-screen design
- Title top-left, data left 40%
- Large 3D visualization right 60%

**Closing Slides**:
- Centered composition
- Large title, contact info below
- Fade-out visual effect

## Reading and Analyzing Presentations

### Text Extraction

To read the text contents of an existing presentation:
```bash
python -m markitdown path-to-file.pptx
```

## Dependencies

Required Python packages:
```bash
pip install requests python-pptx markitdown[pptx]
```

## Environment Setup

Set your Gemini API key:
```bash
export GEMINI_API_KEY='your_api_key_here'
```

## Architecture

```
scripts/
├── gemini_api.py        # Shared API client (DRY principle)
├── nano_banana.py       # Single image generation tool
├── ppt_img_gen.py       # Batch slide generation from plan
└── images2pptx.py       # Image folder → PowerPoint converter
```

## Code Style Guidelines

When generating code for PPTX operations:
- Write concise, readable code
- Use descriptive variable names
- Include error handling for API failures
- Provide clear user feedback
