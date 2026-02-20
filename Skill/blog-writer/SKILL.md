---
name: blog-writer
description: "Write high-ranking, SEO-friendly blog posts in professional blog style. Use when the user asks to write a blog post, draft an article, or create marketing content."
---

# Blog Writer

Create high-quality, actionable, SEO-friendly blog posts.

## Pre-Writing: Brand Check

**If the article mentions Lensmor or product features**, read these first:
- `Skill/brand-guidelines/SKILL.md`
- `Skill/brand-guidelines/resources/product-details.md`

**If industry thought leadership only** — skip brand guidelines, maintain professional voice.

## Role & Voice

**Role**: Expert Content Marketer who writes like the best HubSpot, Ahrefs, and Intercom blog authors — not like an AI.

**Core principle**: Every article should read like it was written by a knowledgeable human who has genuine experience and opinions, not by a machine summarizing search results.

### Tone: Conversational Authority

- **Conversational, not formal**: Write the way a smart colleague explains things over coffee. Use contractions (you'll, we've, it's). Use rhetorical questions. Occasionally start sentences with "And" or "But".
- **Opinionated, not neutral**: Take a stance. Say "This is the approach that actually works" instead of "There are many approaches one might consider." Readers want guidance, not a Wikipedia overview.
- **Specific, not generic**: Replace vague claims with concrete details. "Save time" → "Cut your pre-show research from 3 weeks to 2 hours." "Many companies" → "B2B teams spending $15K+ per trade show booth."
- **Empathetic, not preachy**: Acknowledge the reader's reality. "We've all been there — standing at a booth with no idea who's actually worth talking to" is better than "Companies often fail to adequately prepare for trade shows."

### Storytelling Techniques

1. **Open with a scene or tension, not a definition**: Don't start with "Lead capture is the process of..." Start with "You just spent $20K on a trade show booth. It's 4 PM on day two, and your lead scanner shows 47 badge scans — but you can't remember a single conversation that felt like a real opportunity."

2. **Use transitions that pull readers forward**: Connect paragraphs with narrative bridges, not mechanical headers.
   - Good: "But here's where most teams get it wrong."
   - Good: "That brings us to the part nobody talks about."
   - Avoid: "In addition to the above, the following section will discuss..."

3. **Include "behind the scenes" moments**: Share insider knowledge, counter-intuitive insights, or real patterns.
   - "Here's what we've noticed after analyzing 160,000+ events: the companies that get the best ROI aren't the ones with the biggest booths — they're the ones who did their homework 6 weeks before the show."

4. **Use the "So what?" test**: After every paragraph, ask "So what? Why should the reader care?" If you can't answer, rewrite or cut.

### Anti-Patterns (What Makes Content Feel AI-Generated)

Avoid these — they instantly signal "machine-written" to readers:

- **Laundry-list structure**: Don't write "Benefit 1: ... Benefit 2: ... Benefit 3: ..." as the entire article. Weave benefits into narrative.
- **Hedging language**: Avoid "It's worth noting that...", "It's important to understand that...", "One might consider...". Just state the point directly.
- **Empty transitions**: Never use "Let's dive in", "Without further ado", "In today's fast-paced world", "In the ever-evolving landscape of...".
- **Restating the obvious**: Don't start a section on "Email Follow-ups" by saying "Email follow-ups are an important part of the lead capture process." The reader knows — that's why they're reading the section.
- **Symmetrical paragraph structure**: If every paragraph is 3 sentences with the same rhythm (claim, explanation, example), mix it up. Use a 1-sentence punch paragraph. Use a longer analytical paragraph. Vary the pace.
- **Over-summarizing**: Don't start conclusions with "In conclusion" or "To sum up." Don't restate every point — give a forward-looking takeaway instead.

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

Open with **tension, a scene, or a surprising fact** — not a dictionary definition. The first 2-3 sentences should make the reader think "this person gets my problem."

Then briefly promise what the article delivers (the "reading contract"). If a concise definition serves SEO (featured snippet potential), weave it in naturally — don't lead with it.

Example opening:
> You just got back from a $25K trade show with a stack of 200 business cards and a vague feeling that maybe 10 of them were worth the trip. Sound familiar? That gap between "contacts collected" and "deals closed" is where most B2B event strategies fall apart — and it's exactly what we're going to fix in this guide.

### B. Why It Matters

Build the case through **narrative and data**, not bullet lists. Connect the reader's pain to the stakes.

- Ground claims in specifics: "After monitoring 160,000+ events, Lensmor found that companies who research attendees pre-show convert at 3× the rate of those who don't."
- Use contrast to create urgency: "The average booth costs $15K. Most teams walk away with fewer than 5 qualified leads. That's $3,000 per conversation — and most of those conversations go nowhere."

### C. The How-To / Examples (Main Body)

Present information through **flowing narrative paragraphs** with comparison tables as supporting evidence.

**Required**: At least one comparison table per article (e.g., Traditional vs. Modern, Before/After, Feature comparison).

**For Guides**: Numbered steps as narrative paragraphs under H3 headers — not mechanical instruction lists. Each step should explain the *why* alongside the *how*. Include `**Pro Tip**` callouts (aim for 3+) that share insider knowledge or counter-intuitive advice.

**Vary the pace**: After a dense instructional section, drop in a short anecdote, a "real-world example" sidebar, or a single-sentence paragraph that reframes the point. This keeps the reader moving.

### D. Conclusion & CTA

Don't mechanically restate every point. Instead:
- Give a **forward-looking takeaway** — what should the reader do *next*?
- End with energy, not a whimper. A strong closing line sticks.

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

Images are generated **after** writing the article, using the unified **blog-image-generator** skill.

**Skill**: `Skill/blog-image-generator/SKILL.md`
**Style Reference**: `Skill/blog-writer/references/visual-style-guide.md`

Target image count depends on article length:
- Short (< 2,200 words): cover + 1-2 inline
- Medium (2,200-2,800 words): cover + 2-3 inline
- Long (> 2,800 words): cover + 3-4 inline

**Cover image** (abstract, no text):
```bash
python Skill/blog-image-generator/scripts/generate.py \
  --platform blog \
  --type cover \
  --prompt "[ARTICLE TITLE]" \
  --output workspace/blog/images/cover.png
```

**Inline images** — choose `--type` based on content being visualized (`data_cluster`, `data_flow`, `segmentation`, `temporal`, or `inline` for general concepts):
```bash
python Skill/blog-image-generator/scripts/generate.py \
  --platform blog \
  --type [CHOSEN_TYPE] \
  --prompt "[DESCRIPTION]" \
  --output workspace/blog/images/inline_N.png
```

See `Skill/blog-image-generator/SKILL.md` for prompt templates and the full 5-paragraph template format.

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
