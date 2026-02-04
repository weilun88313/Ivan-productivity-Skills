---
name: pptx
description: "Presentation creation. When needs to work with presentations (.pptx files) for Creating new presentations, or any other presentation tasks"
---

# PPTX Creation with Nano Banana Pro

## Overview

This skill enables AI-powered presentation creation using the **Nano Banana Pro** (Gemini 3 Pro) API. The workflow emphasizes visual storytelling through high-quality AI-generated images that follow brand guidelines.

## Creating a New Presentation

### Interactive Planning Workflow

When the user requests a PPT, **DO NOT** immediately run generation scripts. Follow this 3-step protocol:

#### Step 1: Deep Understanding & Planning

**Your Role**: You are a world-class Presentation Designer, expert at transforming complex documents into logically clear, visually impactful PPT outlines.

**Your Task**:
1.  **Analyze the Input**: Thoroughly read the user's document.
2.  **Determine Slide Count**: Based on document length and complexity, recommend an appropriate number of **content slides** (excluding cover and closing):
    - Short summary: 5-8 content slides
    - Medium analysis: 8-12 content slides
    - Detailed report: 12-18 content slides
3.  **Propose Structure & Get Confirmation**:
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
4.  **Wait for Slide Count Confirmation**: User may approve or request adjustment (e.g., "make it 10 slides" or "add 2 more slides about X").

5.  **Ask for Information Density**:
    ```
    What information density would you prefer?
    
    📊 **Low Density** (Recommended for presentations):
    - 2-3 key points per slide
    - Minimal text, maximum visual impact
    - Clean, visual slides with key talking points to support you while you speak.
    - Best for: Executive presentations, pitches, overviews
    
    📚 **High Density** (For detailed reports):
    - 4-6 key points per slide
    - More detailed text descriptions
    - A comprehensive deck with full text and details, perfect for emailing or reading on its own.
    - Best for: Internal reports, documentation, comprehensive analysis
    
    Please choose: Low or High?
    ```
6.  **Wait for Density Confirmation**: User selects "Low" or "High".

7.  **Ask for Language Preference**:
    ```
    What language would you like for the presentation content?
    
    🇨🇳 **Chinese (中文)**:
    - All slide titles and content in Chinese
    - Best for: Domestic presentations, Chinese-speaking audiences
    
    🇺🇸 **English**:
    - All slide titles and content in English
    - Best for: International presentations, English-speaking audiences
    
    Please choose: Chinese or English?
    ```
8.  **Wait for Language Confirmation**: User selects "Chinese" or "English".

9.  **Proceed to Generation**: Only after all three confirmations (slide count, density, language), proceed to Step 2.

#### Step 2: Plan Generation (Agentic)
Once approved:
1.  **Create `ppt_plan.json`**: Construct a JSON file in the workspace with detailed content for each slide.
    
    *   **CRITICAL**: Always include a **cover slide** (slide_number: 0) and a **closing slide** (slide_number: N+1) automatically.
    
    *   **Information Density Rules**:
        - **Low Density**: 2-3 items in `content` array per slide, concise phrases (5-10 words each)
        - **High Density**: 4-6 items in `content` array per slide, detailed descriptions (10-20 words each)
    
    *   **Language Rules**:
        - **Chinese**: All `title` and `content` items must be in Chinese (中文)
        - **English**: All `title` and `content` items must be in English
        - **Note**: `image_concept` is ALWAYS in English for better AI model compatibility
    
    *   **Output Format** (strict JSON, no Markdown code blocks):
        ```json
        [
          {
            "slide_number": 0,
            "title": "[主题名称]",
            "content": [
              "副标题或简短描述",
              "日期/作者信息（可选）"
            ],
            "image_concept": "Minimalist cover design with the presentation title as the focal point, abstract geometric shapes or data visualization elements in background"
          },
          {
            "slide_number": 1,
            "title": "...",
            "content": ["..."],
            "image_concept": "..."
          },
          ...
          {
            "slide_number": N,
            "title": "Thank You / 谢谢",
            "content": [
              "联系方式（可选）",
              "公司/团队名称"
            ],
            "image_concept": "Clean closing slide design with thank you message, minimal abstract elements, professional and elegant"
          }
        ]
        ```
    
    *   **Cover Slide (slide_number: 0) Requirements**:
        - **title**: The main presentation topic
        - **content**: Subtitle, date, author, or brief description (1-2 lines max)
        - **image_concept**: Focus on title typography and minimal abstract background
        - Example: `"Elegant cover design with large title text, subtle geometric patterns, professional and clean"`
    
    *   **Closing Slide (slide_number: N) Requirements**:
        - **title**: "Thank You" or "谢谢" or custom closing message
        - **content**: Contact info, company name, or call-to-action (optional)
        - **image_concept**: Simple, elegant, minimal
        - Example: `"Minimalist thank you slide with centered text, subtle fade-out effect"`
    
    *   **Key Requirements for `image_concept`**:
        - **BACKGROUND VISUALS ONLY**: Describe abstract visual elements, NOT text or labels
        - **Focus on composition**: Describe objects, scenes, data visualizations, geometric patterns
        - **Reserve space for text**: Visuals should be designed knowing text will overlay on top
        - **Use English**: For better AI model compatibility
        - **Be specific**: "Floating 3D bar chart with two columns, taller on right, subtle glow" instead of "a chart"
        - **Think abstract**: Data visualization, geometric shapes, conceptual diagrams, not literal UI
    
    *   **Examples**:
        ```json
        {
          "slide_number": 0,
          "title": "海外展会行业深度解析",
          "content": [
            "Lensmor 内部报告",
            "2026年2月"
          ],
          "image_concept": "Elegant presentation cover with abstract data flow visualization, interconnected nodes forming a subtle background pattern"
        },
        {
          "slide_number": 1,
          "title": "核心发现",
          "content": [
            "全球市场规模：$394B → $887.6B",
            "年增长率：15% CAGR",
            "核心问题：ROI 不可控"
          ],
          "image_concept": "A futuristic global trade show center at night, holographic map with glowing connection lines between major cities, isometric view"
        },
        {
          "slide_number": 2,
          "title": "市场规模翻倍增长",
          "content": [
            "2023年：$394B",
            "2029年预测：$887.6B",
            "复合增长率：15%"
          ],
          "image_concept": "Two 3D bar columns rising from a digital floor, left column shorter, right column twice as tall, upward trending arrow between them"
        },
        {
          "slide_number": 10,
          "title": "谢谢",
          "content": [
            "Lensmor Team",
            "lensmor.com"
          ],
          "image_concept": "Clean minimalist closing slide with subtle fade-out data visualization elements, professional and elegant finish"
        }
        ```
    
    *   **Density Comparison Example**:
        
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
            "决策盲区：87%的参展决策基于历史经验而非实时市场情报",
            "成本黑箱：展位、搭建、人力成本不透明，难以优化预算",
            "竞争情报缺失：无法实时了解竞争对手的参展动态和策略"
          ]
        }
        ```
    
    *   **Language Comparison Example**:
        
        **Chinese (Low Density)**:
        ```json
        {
          "slide_number": 4,
          "title": "Lensmor 解决方案",
          "content": [
            "从数据到情报",
            "精准目标定位",
            "实时决策支持"
          ],
          "image_concept": "High-tech dashboard interface showing intelligence analytics, sniper scope targeting specific profiles"
        }
        ```
        
        **English (Low Density)**:
        ```json
        {
          "slide_number": 4,
          "title": "Lensmor Solution",
          "content": [
            "From Data to Intelligence",
            "Precision Targeting",
            "Real-time Decision Support"
          ],
          "image_concept": "High-tech dashboard interface showing intelligence analytics, sniper scope targeting specific profiles"
        }
        ```
        
        **English (High Density)**:
        ```json
        {
          "slide_number": 4,
          "title": "Lensmor Solution",
          "content": [
            "Intelligence Layer: Transform raw event data into actionable insights using AI",
            "Precision Targeting: Identify high-value prospects with 95% accuracy",
            "Real-time Analytics: Monitor competitor activities and market trends live",
            "ROI Tracking: Full attribution from booth visit to deal closure",
            "Predictive Modeling: Forecast event performance before committing budget"
          ],
          "image_concept": "High-tech dashboard interface showing intelligence analytics, sniper scope targeting specific profiles"
        }
        ```
    
    *   **Note**: The `image_concept` will be automatically enhanced with:
        - **Brand style**: Linear-inspired dark mode, #6B75FF accents, matte finish
        - **Layout zones**: Top 25% and left 50% reserved for text overlay
        - **4K resolution**: 3840x2160 ultra-high detail
        - **Text constraint**: NO text will be rendered in the image (added programmatically)
        
        Do NOT include style keywords (colors, resolution, brand) or text instructions in `image_concept`.

#### Step 3: Execution
1.  **Generate Background Images**:
    ```bash
    python Skill/pptx/scripts/ppt_img_gen.py workspace/ppt_plan.json workspace/project_name/images
    ```
    This script generates **background visuals only** with:
    - **Linear-Inspired Style**: Technical data visualization, dark mode, matte finish
    - **Color Palette**: Deep charcoal (#1a1a1a), #6B75FF violet-blue accents
    - **Layout Zones**: Top 25% clean for title, left 50% gradient for content
    - **Visual Structure**: Floating data clusters, interconnected nodes, abstract flow diagrams
    - **4K Resolution**: 3840x2160, ultra high detail, sharp and crisp rendering
    - **NO TEXT**: All text will be added programmatically in the next step

2.  **Compile Presentation with Text Overlay**:
    ```bash
    python Skill/pptx/scripts/images2pptx.py workspace/project_name/images workspace/ppt_plan.json workspace/project_name/presentation.pptx
    ```
    This script adds text programmatically with **pixel-perfect consistency**:
    - **Typography**: Segoe UI, 54pt titles, 28pt content, 1.5x line spacing
    - **Layout**: Precise positioning (0.6" top margin, 0.8" left margin)
    - **Slide Types**: Cover (centered, 72pt), Content (standard), Closing (centered, 60pt)
    - **Styling**: White titles, 90% white content, bullet points with consistent spacing

### Manual/Single Image Generation
For testing or single image generation:
```bash
python Skill/pptx/scripts/nano_banana.py --prompt "Test image" --output_dir "output"
```

## Design System

The PPT skill uses a centralized design system (`design_system.py`) to ensure **NotebookLM-level consistency** across all slides.

### Typography Standards

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| **Cover Title** | Segoe UI | 72pt | Bold | #FFFFFF (White) |
| **Cover Subtitle** | Segoe UI | 36pt | Regular | #B4B4B4 (Muted) |
| **Standard Title** | Segoe UI | 54pt | Bold | #FFFFFF (White) |
| **Standard Content** | Segoe UI | 28pt | Regular | #E6E6E6 (90% White) |
| **Closing Title** | Segoe UI | 60pt | Bold | #FFFFFF (White) |
| **Closing Content** | Segoe UI | 32pt | Regular | #E6E6E6 (90% White) |

**Line Spacing**: 1.5x for all content text (improves readability)

### Layout Standards (16:9 Slides)

**Standard Content Slides**:
- **Title**: 0.6" from top, 0.8" from left, 12" width
- **Content**: 2.2" from top, 0.8" from left, 6.5" width (left 50% of slide)
- **Visual Area**: Right 50% reserved for background visuals

**Cover Slides**:
- **Title**: Centered, 2.5" from top, 10.33" width
- **Subtitle**: Centered, 4.2" from top, 10.33" width

**Closing Slides**:
- **Title**: Centered, 2.8" from top, 10.33" width
- **Content**: Centered, 4.3" from top, 10.33" width

### Why This Matters

**Before** (AI-generated text in images):
- ❌ Font sizes vary (48pt, 52pt, 56pt...)
- ❌ Positioning inconsistent (0.5", 0.7", 0.9"...)
- ❌ Text quality unpredictable (blurry, pixelated)
- ❌ Style drift across slides

**After** (Programmatic text overlay):
- ✅ Pixel-perfect consistency (exactly 54pt, exactly 0.6")
- ✅ Crisp, readable text (native PowerPoint rendering)
- ✅ Unified visual language (NotebookLM quality)
- ✅ Easy to customize (change one constant, update all slides)

## Reading and Analyzing Presentations

### Text Extraction
To read the text contents of an existing presentation:
```bash
python -m markitdown path-to-file.pptx
```

## Dependencies

Required dependencies:
- **requests**: `pip install requests` (for API calls)
- **python-pptx**: `pip install python-pptx` (for PPTX compilation)
- **markitdown**: `pip install "markitdown[pptx]"` (for text extraction)

## Code Style Guidelines
When generating code for PPTX operations:
- Write concise code
- Avoid verbose variable names and redundant operations
- Minimize print statements