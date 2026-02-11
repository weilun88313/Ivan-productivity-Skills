---
name: content-pipeline
description: "End-to-end content pipeline: keyword research → blog writing → image generation → Webflow publishing. Use when the user wants to research, write, and publish a blog post in one workflow."
---

# Content Pipeline

Orchestrates the full content workflow: keyword research → article writing → image generation → Webflow publishing.

## When to Use

- User says "write and publish a blog post"
- User wants the full keyword → article → publish flow
- User invokes this skill directly

## Workflow

```
Phase 1: Keyword Research  →  User picks a topic
Phase 2: Write Article     →  Save to workspace/blog/
Phase 3: Generate Images   →  Cover + 3 inline
Phase 4: Publish to Webflow
```

## Phase 1: Quick Keyword Research

**Do this inline** — no need to invoke the keyword-research skill separately.

1. If the topic is Lensmor-related, read brand context:
   - `/Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/SKILL.md`
   - `/Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/resources/product-details.md`

2. Brainstorm 15-20 keywords across:
   - Core terms, problem keywords, solution keywords
   - Comparison keywords ("X vs Y"), question keywords ("how to...")
   - Long-tail variations

3. Present a **short table** of top 5-8 article topic recommendations:

   | # | Article Topic | Target Keyword | Intent | Competition |
   |---|--------------|----------------|--------|-------------|
   | 1 | ... | ... | ... | Low/Med/High |

4. **PAUSE**: Ask user to pick a topic (or suggest their own).

## Phase 2: Write Article

Follow the blog-writer guidelines (`Skill/blog-writer/SKILL.md`):

1. Write the article in markdown with this header format:
   ```
   # [Title]

   **Slug**: /blog/[category]/[keyword-slug]
   **Meta Description**: [150-160 chars]
   **Cover Image**:
   ![description](images/cover.png)

   ---

   [Article body]
   ```

2. Key requirements:
   - 2,000-3,000 words
   - 1+ comparison table
   - 3+ Pro Tips
   - Narrative paragraphs (avoid bullet lists)
   - If Lensmor-related: include waitlist CTA (`https://accounts.lensmor.com/waitlist`)
   - No fake links — only include real, verified URLs

3. Save to `workspace/blog/article.md` (relative to Ivan_Skills root).

4. Add image placeholders like `![description](images/filename.png)` where visuals would enhance the content.

## Phase 3: Generate Images

Use Gemini API via the blog-writer image script.

**Working directory**: `/Users/ivan/Documents/Ivan_Skills`

**Cover image** (abstract, no text):
```bash
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "Style: Abstract high-tech cover art, Linear app design. Dark mode, minimalist, futuristic. Color: #6B75FF glow on deep charcoal. Theme: [ABSTRACT METAPHOR FOR ARTICLE TOPIC]. Environment: Deep black void, subtle grid, shallow depth of field. Negative: NO TEXT, NO UI, NO DASHBOARDS, NO CHARTS." \
  --output_dir workspace/blog/images \
  --filename cover
```

**Inline images** (conceptual, minimal labels):
```bash
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "Style: Technical data visualization, Linear design. Dark mode, minimalist. Color: Charcoal background, #6B75FF accent. Concept: [DESCRIBE WHAT TO VISUALIZE]. Keywords: [2-3 SHORT LABELS ONLY]. Environment: Deep charcoal void. Negative: NO UI chrome, NO dashboards, NO browser frames." \
  --output_dir workspace/blog/images \
  --filename inline_N
```

After generating, update image paths in the markdown file to match actual filenames.

## Phase 4: Publish to Webflow

```bash
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy
```

Add `--publish` flag only if user confirms they want to go live immediately. Default is draft.

**Categories**: `strategy`, `playbooks`, `teardowns`

## Decision Points (Where to Pause)

Only pause for user input at these moments:
1. **After Phase 1**: "Which topic would you like to write about?"
2. **After Phase 4**: Report success/failure, share the result.

Phases 2 and 3 should run without interruption once the topic is confirmed.

## File Structure

```
workspace/blog/
├── article.md          # Blog content with metadata
└── images/
    ├── cover_*.png     # Cover image
    ├── inline_1_*.png  # Inline image 1
    ├── inline_2_*.png  # Inline image 2
    └── inline_3_*.png  # Inline image 3
```

## Error Handling

- **Image generation fails**: Continue with remaining images. Article can publish without images (Webflow strips missing image references).
- **Webflow publish fails**: Check API token/secrets. Print error. Do not retry automatically.
- **Brand guidelines not found**: Continue writing with general professional voice.
