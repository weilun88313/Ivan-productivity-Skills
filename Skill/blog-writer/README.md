[English](README.md) | [中文](README.zh.md)

---


# professional blog Blog Writer

> Create high-ranking, SEO-friendly blog posts in professional professional blog style

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

The **professional blog Blog Writer** skill helps you create professional, actionable, and SEO-optimized blog posts following the professional blog Blog's proven content formula. It combines expert content structure with AI-generated visual assets to produce publish-ready articles.

### Key Features

- ✍️ **professional blog-Style Content** - Professional, actionable, empathetic tone
- 📊 **SEO-Optimized** - Structured for search engine visibility
- 🎨 **AI-Generated Illustrations** - High-quality 16:9 images with Linear dark mode style
- 📝 **Structured Format** - Hook → Why → How → CTA framework
- 💡 **Pro Tips** - Insider advice callouts throughout
- 🎯 **Ready for Publishing** - Compatible with Webflow Blog Publisher

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

**Step 0: Brand Compliance Check (If Product-Related)**

If your blog post will mention Lensmor or product features, read brand guidelines first:

```bash
# Read for latest product information:
- /Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/SKILL.md
- /Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/resources/product-details.md

# Verify:
- Product features are current
- Value proposition is accurate
- Terminology is correct
- Competitive positioning is up-to-date
```

**Step 1: Request a Blog Post**

```
"Write a blog post about email marketing best practices"
```

**Step 2: Generate Images**

```bash
# Cover image
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Abstract email marketing data visualization, flowing connections, Linear dark mode aesthetic" \
  --output_dir workspace/blog/images \
  --filename cover

# Inline images (repeat 3-5 times)
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Email inbox interface wireframe, clean UI mockup, dark mode" \
  --output_dir workspace/blog/images \
  --filename inline_1
```

**Step 3: Review and Publish**

The output includes a properly formatted markdown file ready for publishing with [webflow-blog-publisher](../webflow-blog-publisher).

## Content Structure

### The professional blog Formula

```
┌─────────────────────────────────────┐
│ 1. Hook (Introduction)              │
│    - The Problem                    │
│    - The Agitation (optional)       │
│    - The Promise                    │
│    - The "What is" (definition)     │
├─────────────────────────────────────┤
│ 2. The "Why" (Importance)           │
│    - Benefits in bullet points      │
│    - Data and statistics            │
├─────────────────────────────────────┤
│ 3. The "How-To" (The Meat)          │
│    - Step-by-step guide OR          │
│    - Listicle format                │
│    - Pro Tips throughout            │
├─────────────────────────────────────┤
│ 4. Conclusion & CTA                 │
│    - Key takeaways                  │
│    - Encouraging closing            │
│    - Clear call-to-action           │
└─────────────────────────────────────┘
```

### Output Format

Every blog post includes this metadata block:

```markdown
# [Engaging Title with Keywords]

**Slug**: /blog/[category]/[keyword-slug]
**Meta Description**: [150-160 chars SEO summary]
**Cover Image**:
![Description](images/cover.png)

---

[Article content starts here]
```

## Tone & Voice

### Professional yet Accessible
- Write like a knowledgeable colleague
- Use "You" and "We" pronouns
- Avoid jargon without explanation

### Empathetic
- Acknowledge reader pain points
- *"We know that X can be daunting..."*
- Show understanding before solutions

### Action-Oriented
- Every section provides value
- No fluff or filler content
- Specific, actionable steps

### Confident
- Authoritative but humble
- Backed by data when possible
- Helpful, not preachy

## Formatting Standards

### Paragraphs
- **Maximum 3-4 lines** per paragraph
- Short sentences for readability
- One idea per paragraph

### Headers
- **H2** for main sections
- **H3** for subsections
- Clear, descriptive titles
- Action verbs when appropriate

### Lists
- Bullet points for 3+ related items
- Numbered lists for sequential steps
- **Bold key concepts** for scanning

### Pro Tips
Minimum 3 per article:

```markdown
**Pro Tip**: Use personalization tokens to increase open rates by up to 26%.
```

### Tables
Use markdown tables for comparisons:

```markdown
| Feature | Basic | Premium |
|---------|-------|---------|
| Sends   | 1000  | 50000   |
| Price   | $9    | $49     |
```

## Image Generation

### ⚠️ CRITICAL: Use Complete 5-Paragraph Prompt Template

**All image generation MUST use the full structured template from visual-style-guide.md.**

Do NOT use simplified prompts. The 5-paragraph template ensures:
- ✅ Consistent Linear dark mode aesthetic
- ✅ Accurate #6B75FF color usage
- ✅ Elimination of UI elements and dashboards
- ✅ Proper abstract vs. literal balance
- ✅ High-quality, publication-ready results

**Template Structure** (required for ALL images):
1. **Style**: Define the visual approach
2. **Color Palette**: Specify exact colors (#6B75FF, #1a1a1a)
3. **Concept**: Detailed abstract description
4. **Keywords Allowed**: Minimal text specification
5. **Environment**: Background and depth details
6. **Negative Constraints**: Explicit prohibitions

### Visual Style Guide

All images follow the **Linear dark mode aesthetic**:

- **Style**: Minimalist, technical, modern, abstract
- **Colors**: Deep charcoal backgrounds (#1a1a1a), violet-blue accents (#6B75FF)
- **Elements**: Abstract shapes, data visualizations, geometric forms (NO UI mockups)
- **Quality**: 16:9 aspect ratio, high resolution (2K+)
- **Text**: Minimal keywords only (NO paragraphs or detailed text)

**See**: [references/visual-style-guide.md](references/visual-style-guide.md) for complete 5-paragraph templates and examples

### Image Requirements

#### Cover Image (Required)
- **Purpose**: Header image for the article
- **Style**: Purely abstract — NO text, NO UI, NO literal depictions
- **Prompt Template**: Use complete 5-paragraph template from visual-style-guide.md
  ```
  Style: Abstract high-tech cover art, inspired by "Linear" app design...

  Color Palette: Primary glowing light is hex code #6B75FF...

  Theme Concept: [Translate article topic into abstract visual metaphor]...

  Environment: Deep black void. Very subtle isometric grid...

  Negative Constraints: NO TEXT, NO LETTERS, NO UI ELEMENTS...
  ```
- **Example**: See visual-style-guide.md section "Cover Image Example" for Event Intelligence blog

#### Inline Images (Minimum 3)
- **Purpose**: Support content sections visually with abstract conceptual illustrations
- **Types** (all must be abstract):
  - Data cluster visualizations (floating information cards)
  - Data flow visualizations (particle streams)
  - Segmentation visualizations (geometric clusters)
  - Temporal visualizations (evolution progression)

- **Prompt Template**: Use complete 5-paragraph template from visual-style-guide.md
  ```
  Style: [Visualization type] inspired by Linear design system...

  Color Palette: Deep charcoal background (#1a1a1a), #6B75FF accents...

  Concept: [Detailed abstract description with geometric elements]...

  Keywords Allowed: [Minimal labels only]...

  Environment: Deep [void type] with [depth cues]...

  Negative Constraints: NO UI chrome, NO dashboards, NO [specific]...
  ```

**❌ Do NOT use**:
- Simplified 1-paragraph prompts
- Dashboard or interface terminology
- UI mockups or chrome elements
- Traditional charts (pie, bar, line)

**✅ Always use**:
- Complete 5-paragraph structured template
- Abstract geometric descriptions
- Exact #6B75FF color specification
- Explicit negative constraints

### Generation Script

```bash
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Your detailed prompt here" \
  --output_dir "path/to/output" \
  --filename "image_name"
```

**Options**:
- `--prompt` (required): Detailed image description
- `--output_dir` (optional): Output directory (default: current)
- `--filename` (optional): Filename prefix (default: blog_image)

**Output**: `{filename}_{timestamp}.png`

## Content Types

### How-To Guides

**Structure**:
```markdown
## Step 1: [Action Verb Title]

Brief explanation of the step.

**Pro Tip**: Insider advice for this step.

![Relevant diagram](images/step1.png)
```

**Example Topics**:
- "How to Build an Email Marketing Strategy"
- "How to Optimize Your Landing Pages"
- "How to Conduct Keyword Research"

### Listicles

**Structure**:
```markdown
## 1. [Item Name/Concept]

Description of the item and why it matters.

**Why this works**: Explanation of effectiveness.

![Illustration](images/item1.png)
```

**Example Topics**:
- "10 Email Marketing Best Practices"
- "7 Content Marketing Trends in 2026"
- "15 SEO Tools Every Marketer Needs"

### Thought Leadership

**Structure**:
- Controversial or contrarian hook
- Data-backed argument
- Industry insights
- Future predictions
- Actionable takeaways

**Example Topics**:
- "Why Traditional Marketing is Dead (And What's Next)"
- "The Future of Content Marketing"
- "What Most Marketers Get Wrong About SEO"

## SEO Best Practices

### Title Optimization
- **Length**: 50-60 characters
- **Format**: [Number] + [Adjective] + [Keyword] + [Promise]
- **Example**: "10 Proven Email Marketing Strategies to 3x Your ROI"

### Meta Description
- **Length**: 150-160 characters
- **Include**: Primary keyword, benefit, call-to-action
- **Example**: "Learn 10 proven email marketing strategies that top brands use to triple their ROI. Actionable tips inside."

### Slug Structure
- **Format**: `/blog/[category]/[keyword-slug]`
- **Category**: strategy, playbooks, or teardowns
- **Slug**: Lowercase, hyphens, keyword-rich
- **Example**: `/blog/strategy/email-marketing-best-practices`

### Keyword Integration
- **Primary keyword**: In title, H2, first paragraph, meta
- **Secondary keywords**: In H3 headers, throughout content
- **Natural usage**: Write for humans first, search engines second
- **Density**: 1-2% is ideal, avoid keyword stuffing

### Internal Linking
- Link to related articles (when publishing)
- Use descriptive anchor text
- 2-3 internal links per article

## Example Prompts

### For AI Assistant

**Basic Request**:
```
Write a blog post about [topic]
```

**Detailed Request**:
```
Write a comprehensive how-to guide about email marketing automation for small businesses.
Include 8-10 steps, focus on practical implementation, and target beginners.
Tone: friendly but professional. Include data points where relevant.
```

**Listicle Request**:
```
Write a listicle: "15 Content Marketing Tools Every Startup Needs".
Low density (2-3 points per tool), include pricing tiers, and why each tool matters.
```

### For Image Generation

**⚠️ Important**: Always use complete 5-paragraph templates. Examples below are abbreviated for readability — see visual-style-guide.md for full templates.

**Cover Image Example** (Event Intelligence):
```bash
--prompt "Style: Abstract high-tech cover art, inspired by \"Linear\" app design. Dark mode UI, minimalist, clean, futuristic.

Color Palette: Primary glowing light is hex code #6B75FF (neon violet-blue indigo). Soft, diffused glow on deep charcoal background.

Theme Concept: Scattered event data signals—exhibitor profiles, attendee behavior patterns, competitive intelligence fragments—flowing as glowing particle streams from all directions, converging into a central crystalline intelligence hub. The hub emanates organized insight pathways radiating outward to strategic decision nodes. Translate this into glowing geometric data streams, interconnected nodes pulsing with #6B75FF light, floating frosted glass prismatic shapes representing crystallized insights, and abstract light trails showing data transformation. Composition representing raw chaos organizing into actionable intelligence.

Environment: Deep black void. Very subtle, barely visible isometric grid fading into darkness. Shallow depth of field with soft bokeh effects on distant data streams.

Negative Constraints: NO TEXT, NO LETTERS, NO WORDS, NO CHARACTERS, NO UI ELEMENTS, NO DASHBOARDS, NO CHARTS. Purely abstract visual shapes and light compositions."
```

**Inline Image Example** (Data Flow):
```bash
--prompt "Style: Abstract real-time data flow visualization inspired by Linear aesthetic. Dark mode, dynamic, flowing composition.

Color Palette: Deep charcoal background, flowing data streams in matte grey with #6B75FF highlights for high-priority signals.

Concept: Living data streams flowing from left to right across the frame—representing real-time event intelligence. Multiple parallel streams of varying thickness, each stream composed of small geometric particles (circles, diamonds, hexagons) moving at different velocities. Key insight nodes pulse with #6B75FF glow as data passes through them. Thin connecting lines branch off from main streams to floating analysis nodes. Create sense of continuous information flow and pattern recognition happening in real-time.

Keywords Allowed: Minimal labels—\"Foot Traffic\", \"Engagement\", \"Leads\". Tiny, clean text integrated into the flow.

Environment: Deep black background with subtle motion blur on particles suggesting speed. No grid—pure void emphasizing movement.

Negative Constraints: NO UI elements, NO charts with axes, NO dashboard frames, NO static graphs. Pure flowing abstract visualization."
```

**More Examples**: See [references/visual-style-guide.md](references/visual-style-guide.md) for:
- Data cluster visualizations
- Segmentation schematics
- Temporal evolution diagrams
- Complete prompt library

## Workflow Integration

This skill works seamlessly with [webflow-blog-publisher](../webflow-blog-publisher):

```bash
# 1. Write blog post (using AI)
# Output: workspace/blog/article.md

# 2. Generate images
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "..." \
  --output_dir workspace/blog/images

# 3. Publish to Webflow
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

See [BLOG_WORKFLOW.md](../BLOG_WORKFLOW.md) for complete end-to-end guide.

## Troubleshooting

### Image Generation Fails

**Error**: `GEMINI_API_KEY not found`

**Solution**:
```bash
# Option 1: Environment variable
export GEMINI_API_KEY='your_key'

# Option 2: Secrets file
echo '{"NANO_API_KEY": "your_key"}' > ~/.claude/lensmor_secrets.json
```

**Error**: `Request timed out`

**Solution**:
- Simplify your prompt (fewer details)
- Check internet connection
- Try again in a few minutes (API may be busy)

**Error**: `No image data found in response`

**Solution**:
- Your prompt may violate content policy
- Avoid brand names, copyrighted content
- Use generic descriptions

### Content Quality Issues

**Problem**: Content is too generic

**Solution**:
- Provide more specific topic details
- Include target audience information
- Reference specific pain points
- Request data points or statistics

**Problem**: Tone is too formal/informal

**Solution**:
- Explicitly request tone adjustment
- Reference style: "Write in professional blog Blog style"
- Provide tone examples

**Problem**: Content is too long/short

**Solution**:
- Specify word count: "Write a 2000-word guide"
- Specify sections: "Include 8 main sections"
- Request density: "High density" or "Low density"

## Best Practices

### Content Strategy
1. **Brand Compliance First**: If writing about Lensmor/product, read brand-guidelines/SKILL.md for latest product info
2. **Research First**: Understand your topic deeply
3. **Know Your Audience**: Write for specific reader personas
4. **Data-Driven**: Include statistics and research
5. **Actionable**: Every section should provide value
6. **SEO-Conscious**: But write for humans first

### Image Strategy
1. **Consistent Style**: Use the same visual language throughout
2. **Relevant Visuals**: Images should support content, not distract
3. **High Quality**: Never compromise on image resolution
4. **Descriptive Alt Text**: For accessibility and SEO
5. **Strategic Placement**: Break up long text sections

### Publishing Strategy
1. **Draft First**: Always review before publishing live
2. **Peer Review**: Get feedback from colleagues
3. **SEO Check**: Verify keyword usage and meta data
4. **Mobile Preview**: Test on mobile devices
5. **Performance Track**: Monitor analytics after publishing

## Architecture

```
hubspot-blog-writer/
├── README.md                  # This file
├── SKILL.md                   # AI workflow instructions
├── scripts/
│   ├── gemini_api.py         # Shared API client
│   └── generate_image.py     # Image generation tool
└── references/
    └── visual-style-guide.md # Detailed visual guidelines
```

## Version History

### v2.1.0 (2026-02-09)
- ✅ **BREAKING**: Mandated complete 5-paragraph prompt template for all images
- ✅ Updated visual-style-guide.md with detailed templates and examples
- ✅ Added 4 inline image category templates (data cluster, flow, segmentation, temporal)
- ✅ Enhanced README with template usage guidance and quality requirements
- ✅ Eliminated simplified prompts to ensure consistent quality

### v2.0.0 (2026-02-08)
- ✅ Refactored image generation to use shared API module
- ✅ Improved error handling and user feedback
- ✅ Added comprehensive README documentation
- ✅ Cleaner code architecture (106 → 85 lines)

### v1.0.0 (2026-02-07)
- Initial release with professional blog-style content structure
- AI-powered image generation
- Linear dark mode visual aesthetic

## Resources

- [SKILL.md](SKILL.md) - Detailed AI instructions and content guidelines
- [Visual Style Guide](references/visual-style-guide.md) - Image generation guidelines
- [Webflow Blog Publisher](../webflow-blog-publisher) - Publishing integration
- [Blog Workflow Guide](../BLOG_WORKFLOW.md) - End-to-end process

## Contributing

Improvements welcome! Focus areas:
- Additional content templates
- Enhanced image prompts
- SEO optimization techniques
- Style guide updates

## License

Proprietary - For internal use

## Support

For issues or questions:
1. Check this README
2. Review SKILL.md for AI-specific guidance
3. Consult Blog Workflow Guide for integration
4. Test image generation independently

---

**Happy Writing!** 📝✨
