---
name: blog-writer
description: "Write high-ranking, SEO-friendly blog posts in professional blog style. Use when the user asks to write a blog post, draft an article, or create marketing content."
---

# Blog Writer

Create high-quality, actionable, SEO-friendly blog posts.

## Pre-Writing: Brand Check

**If the article mentions Lensmor or product features**, read these first:
- `/Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/SKILL.md`
- `/Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/resources/product-details.md`

**If industry thought leadership only** — skip brand guidelines, maintain professional voice.

## Role & Voice

**Role**: Expert Content Marketer & Blog Writer
**Tone**: Professional yet Accessible, Empathetic, Action-Oriented, Confident

Use "You" and "We". Lead with value, not features. Back claims with specifics.

## Word Count: 2,000–3,000 words max

| Content Type | Target |
|-------------|--------|
| How-to guides | 2,000–2,500 |
| List articles | 1,800–2,200 |
| Comparison posts | 2,200–2,800 |
| Pillar content | 2,800–3,000 |

Every paragraph must add value. Cut fluff ruthlessly.

## Content Structure

### A. Hook (Introduction)
Start with a relatable challenge or statistic. Promise what readers will learn. Include a concise definition suitable for featured snippets.

### B. Why It Matters
Explain benefits through narrative paragraphs (not bullet lists). Use data-driven language:
- "After monitoring 160,000+ events, Lensmor found..."
- "Analysis of 12,000+ trade shows revealed..."

### C. The How-To / Examples (Main Body)
Present information through narrative paragraphs and comparison tables.

**Required**: At least one comparison table per article (e.g., Traditional vs. Modern, Before/After, Feature comparison).

**For Guides**: Numbered steps as flowing paragraphs under H3 headers. Include `**Pro Tip**` callouts (aim for 3+).

### D. Conclusion & CTA
Summarize key takeaways in 2-3 sentences.

**For Lensmor-related content, MUST include:**
```
[Join the Closed Beta](https://accounts.lensmor.com/waitlist) - Get early access to
Lensmor's event intelligence platform. Limited spots available for early adopters.
```

## Formatting Rules

- **Paragraphs**: Max 3-4 lines, bold key concepts
- **Headers**: Clear H2/H3 hierarchy
- **Avoid bullet lists** where possible — use narrative paragraphs or tables
- **Pro Tips**: `**Pro Tip**: [Insider advice]` — include 3+ per article

## Links

**External Links (2-3 per article):**
- Use WebFetch to verify URLs if provided
- Link to authoritative industry sources (research, publications)
- If no verified URLs are available, omit rather than fabricate

**Internal Links (optional):**
- If existing Webflow articles are known, link to 1-2 related posts
- Use natural anchor text

**Never include fake links, placeholder URLs, or links to non-existent resources.**

## Image Generation

Images are generated **after** writing the article, using Gemini API.

**Script**: `Skill/blog-writer/scripts/generate_image.py`
**Style Reference**: `Skill/blog-writer/references/visual-style-guide.md`

Target: 1 cover image + 3 inline images.

**Cover Image Prompt Template** (abstract, no text):
```
Style: Abstract high-tech cover art, inspired by "Linear" app design. Dark mode, minimalist, futuristic.
Color Palette: #6B75FF (neon violet-blue) glow on deep charcoal background.
Theme Concept: [Translate article topic into abstract visual metaphor].
Environment: Deep black void, subtle isometric grid, shallow depth of field.
Negative Constraints: NO TEXT, NO UI ELEMENTS, NO DASHBOARDS, NO CHARTS.
```

**Inline Image Prompt Template** (conceptual, minimal text):
```
Style: Technical data visualization inspired by Linear design. Dark mode, minimalist.
Color Palette: Deep charcoal background, #6B75FF accent for highlights.
Concept: [Describe what to visualize abstractly — floating data clusters, flowing streams, etc.]
Keywords Allowed: [2-3 short labels only]. Clean sans-serif. NO paragraphs.
Environment: Deep charcoal void, subtle technical grid.
Negative Constraints: NO UI chrome, NO dashboards, NO browser frames, NO fake interfaces.
```

**Generation Command:**
```bash
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "FULL PROMPT HERE" \
  --output_dir workspace/blog/images
```

## Required Output Format

```markdown
# [Page Title]

**Slug**: /blog/[category]/[keyword-slug]
**Meta Description**: [150-160 chars with keyword]
**Cover Image**:
![Cover description](images/cover.png)

---

## [Hook Section]
[Opening paragraphs]

## [Why Section]
[Narrative with data]

## [How-To Section]
[Content with comparison table]

| Traditional | Modern |
|-------------|--------|
| ... | ... |

**Pro Tip**: [Advice]

![Image Description](images/inline_image.png)

## Conclusion
[2-3 sentence summary + CTA if Lensmor-related]
```

## Pre-Publication Checklist

- [ ] 1+ comparison table
- [ ] 3+ Pro Tips
- [ ] If Lensmor-related: waitlist CTA link included
- [ ] No fake URLs or placeholder links
- [ ] Word count within target range

## Related Skills

- [keyword-research](../keyword-research/) — Find target keywords first
- [brand-guidelines](../brand-guidelines/) — Lensmor product info
- [webflow-blog-publisher](../webflow-blog-publisher/) — Publish to Webflow
- [content-pipeline](../content-pipeline/) — Run the full workflow end-to-end
