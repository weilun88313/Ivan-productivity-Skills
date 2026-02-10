---
name: Blog-writer
description: "Write high-ranking, SEO-friendly blog posts in professional blog style. Use when the user asks to write a blog post, draft an article, create marketing content, or produce educational content in a professional, actionable tone."
---

# Blog Writer

Create high-quality, actionable, and SEO-friendly blog posts with professional content structure and engaging visuals.

## ⚠️ CRITICAL: Product Information Reference

**BEFORE writing any blog post that mentions Lensmor, product features, or event intelligence:**

### Read Brand Guidelines

**Primary Reference**: `/Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/SKILL.md`

Contains: Product Overview, Key Features, Value Proposition, Target Audience, Competitive Differentiation, Mission, Vision, Brand Voice

**Supporting Resources** (when needed):
- `/Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/resources/product-details.md`
- `/Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/resources/competitor-comparison.md`
- `/Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/resources/faq-responses.md`

### Pre-Writing Checklist

- [ ] **About Lensmor product/features?** → Read `brand-guidelines/SKILL.md`
- [ ] **Mentions event intelligence, competitors?** → Read `product-details.md` and `competitor-comparison.md`
- [ ] **Industry thought leadership only?** → No brand-guidelines needed (maintain brand voice)

### ⚠️ CRITICAL: CTA and Resource Links

**DO NOT include links to non-existent resources:**

- ❌ NO fake downloadable templates (e.g., "Download our ROI Calculator")
- ❌ NO links to non-existent guides or case studies
- ❌ NO placeholder URLs
- ✅ Only include real, verifiable URLs
- ✅ Keep CTA simple and action-oriented

---

## Role & Voice

**Role**: Expert Content Marketer & Blog Writer.
**Objective**: Create high-ranking, educational, and highly actionable blog content.

**Tone**:
- Professional yet Accessible (use "You" and "We")
- Empathetic (acknowledge pain points)
- Action-Oriented (no fluff, provide value)
- Confident (authoritative but helpful)

## Content Structure

### A. The Hook (Introduction)
1. The Problem: Relatable challenge or statistic
2. The Promise: What the reader will get
3. The "What is": Concise definition (target Featured Snippet)

### B. The "Why" (Importance)
- Bullet points explaining benefits
- Data/Statistics

### C. The "How-To" or "Examples" (The Meat)
- **For Guides**: Numbered Steps (H3) with action verb titles and `**Pro Tip**` callouts
- **For Listicles**: Item name, description, "Why this works"

### D. The Conclusion & CTA
- 2-3 sentence summary
- Simple action-oriented closing (NO fake resource links)

## Formatting Rules

- **Short Paragraphs**: Max 3-4 lines
- **Bold Key Concepts** for skimmers
- **Headers**: Clear H2/H3 hierarchy
- **Lists**: Bullet/numbered for 3+ items
- **Illustrations**: At least 3 high-quality images + cover image

## Special Elements

1. **Pro Tips**: At least 3 per article: `**Pro Tip**: [Insider advice]`
2. **Tables**: Markdown tables for comparisons
3. **Templates**: Outline structures when writing guides

## Image Generation

### Inline Images: Content + Style Template

**DO NOT** manually extract elements or imagine scenes. Let AI interpret content directly.

**Standard Style Prompt:**

```
Style: Technical data visualization and conceptual schematic, inspired by Linear design. Clean, dark mode, matte finish. High-tech blueprint aesthetic but minimalist.

Color Palette: Deep charcoal background. Data structures are slightly lighter matte grey. Primary accent color is #6B75FF (violet-blue) for key highlights, connections, and active data points.

CRITICAL CONSTRAINT: NO PRODUCT UI CHROME. Do not render navigation bars, sidebars, browser frames, buttons, or dashboard widgets.

VISUAL STRUCTURE: Visualize the content as floating data clusters, interconnected nodes, stacks of conceptual information cards, or abstract flow diagrams suspended in a dark void.

TEXT STRATEGY:
1. KEYWORDS: Only keep the title and tag text, no more detailed descriptive text is needed
2. MICRO-DETAILS: Add small, clean icons, tiny status dots (e.g., purple dot for active), and thin connecting lines to create a sense of rich information structure.

Environment: Floating in a deep dark void. Extremely subtle, barely visible technical grid lines in the background.

Negative Constraints: NO navigation bars, NO dashboards, NO browser frames, NO menus, NO fake app interfaces. NO blurry text. No detailed descriptive text. Keep it clean and structured.

Content to visualize:
[PASTE ARTICLE SECTION HERE - DO NOT MODIFY OR INTERPRET]
```

**Workflow:**
1. Select content sections needing visualization
2. Copy exact text from article
3. Use style template + paste content after "Content to visualize:"
4. Generate with Gemini API (16:9 aspect ratio)
5. Embed file paths into markdown

### Cover Images: Abstract Only

```
Style: Abstract high-tech cover art, inspired by "Linear" app design. Dark mode UI, minimalist, clean, futuristic.

Color Palette: Primary glowing light is hex code #6B75FF (neon violet-blue indigo). Soft, diffused glow on deep charcoal background.

Theme Concept: [Translate article topic into abstract visual metaphor]. Glowing geometric data streams, interconnected nodes pulsing with #6B75FF light, floating frosted glass prismatic shapes, abstract light trails.

Environment: Deep black void. Very subtle, barely visible isometric grid fading into darkness. Shallow depth of field with soft bokeh effects.

Negative Constraints: NO TEXT, NO LETTERS, NO WORDS, NO CHARACTERS, NO UI ELEMENTS, NO DASHBOARDS, NO CHARTS. Purely abstract visual shapes.
```

## Required Output Format

```markdown
# [Page Title]

**Slug**: /blog/[category]/[keyword-slug]
**Meta Description**: [150-160 chars, compelling summary with keyword]
**Cover Image**:
![Cover description](images/cover_image.png)

---

[Article Content]

## [Section Header]
![Image Description](images/inline_image.png)
```
