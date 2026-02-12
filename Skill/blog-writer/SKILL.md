---
name: Blog-writer
description: "Write high-ranking, SEO-friendly blog posts in professional blog style. Use when the user asks to write a blog post, draft an article, create marketing content, or produce educational content in a professional, actionable tone."
---

# Blog Writer

Create high-quality, actionable, and SEO-friendly blog posts with professional content structure and engaging visuals.

## Pre-Writing: Brand Check

**If the article mentions your product or features**, read your brand guidelines first.

**If industry thought leadership only** — skip brand guidelines, maintain professional voice.

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
Start with a relatable challenge or statistic that captures attention. Follow with the promise of what readers will learn, then provide a concise definition suitable for featured snippets.

### B. The "Why" (Importance)
Explain benefits through narrative paragraphs rather than bullet lists. Incorporate data and statistics naturally within flowing prose.

**Data-Driven Language:**
Use specific data points and concrete numbers, not vague claims.

### C. The "How-To" or "Examples" (The Meat)
Present information through narrative paragraphs and comparison tables. Avoid bullet lists where possible.

**⚠️ REQUIRED - Comparison Tables:**
Every article **MUST** include at least one comparison table:
- Traditional vs. Modern approach
- Feature comparison across methods/tools
- Before/After scenarios
- Cost/Benefit analysis

Use markdown tables for visual comparison.

**For Guides**: Write numbered steps as flowing paragraphs under H3 headers. Include `**Pro Tip**` callouts.

**For Explanatory Content**: Use narrative structure with comparison tables to illustrate differences.

### D. The Conclusion & CTA
Summarize key takeaways in 2-3 sentences. Include a relevant CTA if product-related.

## Formatting Rules

**Paragraph Structure**: Keep paragraphs concise (max 3-4 lines) and scannable. Bold key concepts for easy skimming.

**Headers**: Maintain clear H2/H3 hierarchy throughout the article.

**⚠️ AVOID BULLET LISTS**: Try not to use bullet/numbered lists. Instead, write information in flowing narrative paragraphs or use comparison tables for structured data.

**Visual Elements**: Include at least 3 high-quality images plus one cover image.

## Special Elements

**Pro Tips**: Include at least 3 pro tip callouts throughout the article using `**Pro Tip**: [Insider advice]` format.

**Comparison Tables (REQUIRED)**: Every article must include at least one markdown comparison table. Use tables to compare approaches, features, costs, or before/after scenarios.

**External Links**: Research and include 2-3 relevant external links using WebSearch to find authoritative sources.

**Internal Links**: Query Webflow CMS to find and link to 1-2 related existing articles on the site.

## Link Research and Integration

### External Links (Required: 2-3 per article)

**Process:**
1. Use WebSearch to find relevant, authoritative articles on the topic
2. Look for:
   - Industry publications (e.g., MarketingProfs, HubSpot Blog, Forrester)
   - Research studies with data
   - Government/industry association reports
   - Reputable B2B resources
3. Integrate links naturally within content paragraphs
4. Use descriptive anchor text (not "click here" or "this article")

**Example Integration:**
```
Research from the Content Marketing Institute shows that 73% of B2B marketers
now prioritize data-driven strategies over intuition-based decisions.
```

### Internal Links (Required: 1-2 per article)

**Process:**
1. Query Webflow CMS API to retrieve existing published articles
2. Find related articles by:
   - Topic relevance
   - Category match
   - Keyword overlap
3. Link naturally in context where it adds value
4. Use article titles or descriptive phrases as anchor text

**Webflow CMS Query:**
```python
# Read collection to get existing articles
GET /collections/{collection_id}/items
Filter: isDraft = false
Look for: slug, name (title), ref (category)
```

**Example Integration:**
```
Building on our previous discussion of trade show ROI metrics, this approach
takes event intelligence a step further.
```

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

Only replace `{BLOG_TITLE}` with the article title. Do NOT modify anything else:

```
Style: Abstract high-tech cover art, inspired by "Linear" app design. Dark mode UI, minimalist, clean, futuristic.

Color Palette: Primary glowing light is hex code #6B75FF (neon violet-blue indigo). Soft, diffused glow on deep charcoal background.

Key content to be displayed: {BLOG_TITLE}

Do not render these words as text. Translate the meaning into glowing geometric data streams, interconnected nodes, floating frosted glass shapes, and abstract light trails. Composition representing data flow in a sophisticated system.

Environment: Deep black void. Very subtle, barely visible isometric grid fading into darkness. Shallow depth of field with soft bokeh effects on distant pathway nodes.

Negative Constraints: NO TEXT, NO LETTERS, NO WORDS, NO CHARACTERS, NO UI ELEMENTS, NO DASHBOARDS, NO CHARTS. Purely abstract visual shapes and light compositions.
```

## Required Output Format

```markdown
# [Page Title]

**Slug**: /blog/[category]/[keyword-slug]
**Meta Description**: [150-160 chars, compelling summary with keyword]
**Cover Image**:
![Cover description](images/cover_image.png)

---

## [Hook Section]

[Opening paragraphs with data-driven language and problem statement]

[Data-driven insight with specific numbers].

## [Why Section]

[Narrative paragraphs explaining importance with flowing prose, NOT bullet lists]

According to [External Link: Industry Source](https://actual-url.com), this approach...

## [How-To Section]

[Content with comparison table - REQUIRED]

| Traditional Approach | Modern Approach |
|---------------------|-----------------|
| Manual research     | Automated intelligence |
| 10-15 hours         | 10 minutes      |
| Static data         | Real-time updates |

[More narrative content. Reference to internal article where relevant:]
As we discussed in [our previous article on event ROI](internal-slug), this strategy...

![Image Description](images/inline_image.png)

**Pro Tip**: [Insider advice that adds value]

## Conclusion

[2-3 sentence summary of key takeaways]

[If product-related, include relevant CTA]
```

## Pre-Publication Checklist

Before finalizing any blog post, verify:
- [ ] Includes 1+ comparison table (REQUIRED)
- [ ] Uses data-driven language with specific numbers
- [ ] 2-3 external links from WebSearch (real, authoritative)
- [ ] 1-2 internal links from Webflow CMS (if applicable)
- [ ] Minimal use of bullet lists (narrative paragraphs preferred)
- [ ] If product-related: includes relevant CTA
- [ ] 3+ Pro Tips included
- [ ] 3+ inline images + 1 cover image
