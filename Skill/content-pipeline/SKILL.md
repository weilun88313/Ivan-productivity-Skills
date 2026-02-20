---
name: content-pipeline
description: "End-to-end content pipeline: keyword research → blog writing → image generation → Webflow publishing. Use when the user wants to research, write, and publish a blog post in one workflow."
---

# Content Pipeline

Orchestrates the full content workflow: keyword research → article writing → image generation → quality check → Webflow publishing.

## When to Use

- User says "write and publish a blog post"
- User wants the full keyword → article → publish flow
- User invokes this skill directly

## Workflow

```
Phase 1: Keyword Research    →  User picks a topic + content type
Phase 2: Write Article       →  Save to workspace/blog/
Phase 3: Generate Images     →  Cover + inline (count based on article)
Phase 4: Quality Gate        →  Auto-check before publishing
Phase 5: Publish to Webflow
```

## Phase 1: Keyword Research

Choose the appropriate depth based on context:

### Quick Mode (user already has a topic direction)

Do this inline when the user has a clear topic in mind.

1. If the topic is Lensmor-related, read brand context:
   - `Skill/brand-guidelines/SKILL.md`
   - `Skill/brand-guidelines/resources/product-details.md`

2. Brainstorm 15-20 keywords across:
   - Core terms, problem keywords, solution keywords
   - Comparison keywords ("X vs Y"), question keywords ("how to...")
   - Long-tail variations

3. Present a **short table** of top 5-8 article topic recommendations:

   | # | Article Topic | Target Keyword | Intent | Competition |
   |---|--------------|----------------|--------|-------------|
   | 1 | ... | ... | ... | Low/Med/High |

### Deep Mode (starting from scratch or SEO-critical content)

Invoke the **keyword-research** skill (`Skill/keyword-research/SKILL.md`) for real data:

1. Run keyword research with Ahrefs MCP to get:
   - Real search volume, Keyword Difficulty (KD 0-100), Traffic Potential
   - GEO opportunity flags (queries likely to trigger AI-generated answers)
   - Topic cluster organization (pillar + supporting articles)

2. Present results in the keyword-research output format:

   | # | Article Topic | Target Keyword | Volume | KD | Intent | GEO Potential |
   |---|--------------|----------------|--------|-----|--------|---------------|
   | 1 | ... | ... | ... | ... | ... | Yes/No |

If Ahrefs MCP is unavailable, fall back to Quick Mode with qualitative estimates.

### After either mode

**PAUSE**: Ask the user to:
1. Pick a topic (or suggest their own)
2. Confirm the **content type**:

   | Content Type | Word Count Target | Typical Structure |
   |-------------|-------------------|-------------------|
   | How-to guide | 2,000–2,500 | Numbered steps under H3 headers |
   | List article | 1,800–2,200 | Grouped items with narrative |
   | Comparison post | 2,200–2,800 | Side-by-side analysis + tables |
   | Pillar content | 2,800–3,000 | Comprehensive deep-dive |

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

2. Key requirements (adjusted by content type from Phase 1):
   - Word count within the target range for the chosen content type
   - 1+ comparison table
   - 3+ Pro Tips
   - Narrative paragraphs (avoid bullet lists)
   - If Lensmor-related: include waitlist CTA (`https://accounts.lensmor.com/waitlist`)
   - No fake links — only include real, verified URLs

3. Add image placeholders (`![description](images/filename.png)`) where visuals would enhance the content. Place them based on article needs:
   - Short articles (< 2,200 words): cover + 1-2 inline
   - Medium articles (2,200-2,800 words): cover + 2-3 inline
   - Long articles (> 2,800 words): cover + 3-4 inline

4. Save to `workspace/blog/article.md` (relative to repository root).

**PAUSE (optional)**: If the user requested a review, or if the article topic is complex/sensitive, show a summary (title, structure outline, word count) and ask to confirm before generating images. Otherwise, continue directly.

## Phase 3: Generate Images

Use the unified **blog-image-generator** skill for all image generation.

All commands below use paths relative to the repository root.

### Cover image (abstract, no text)

```bash
python Skill/blog-image-generator/scripts/generate.py \
  --platform blog \
  --type cover \
  --prompt "[ARTICLE TITLE]" \
  --output workspace/blog/images/cover.png
```

### Inline images

Scan the article for `![description](images/...)` placeholders and generate one image per placeholder.

Choose the image `--type` that best matches the content being visualized:

| Type | Best For |
|------|----------|
| `data_cluster` | Grouped information, categorization, data organization |
| `data_flow` | Processes, pipelines, real-time systems, movement |
| `segmentation` | Audience segments, targeting, categorization |
| `temporal` | Trends over time, evolution, progression |
| `inline` | General concepts that don't fit above categories |

```bash
python Skill/blog-image-generator/scripts/generate.py \
  --platform blog \
  --type [CHOSEN_TYPE] \
  --prompt "[DESCRIPTION FROM PLACEHOLDER ALT TEXT OR SURROUNDING CONTENT]" \
  --output workspace/blog/images/inline_N.png
```

### Batch generation (alternative for multiple images)

```bash
# Create prompts.json:
{
  "images": [
    {"type": "cover", "prompt": "[ARTICLE TITLE]", "output": "cover.png"},
    {"type": "[chosen_type]", "prompt": "[CONCEPT 1]", "output": "inline_1.png"},
    {"type": "[chosen_type]", "prompt": "[CONCEPT 2]", "output": "inline_2.png"}
  ]
}

# Run batch:
python Skill/blog-image-generator/scripts/batch.py \
  --platform blog \
  --prompts prompts.json \
  --output_dir workspace/blog/images
```

After generating, update image paths in the markdown file to match actual filenames.

## Phase 4: Quality Gate

Before publishing, automatically verify these checks against the article:

| Check | Rule | Action if Failed |
|-------|------|------------------|
| Word count | Within target range for content type | Warn user, suggest expanding/trimming |
| Comparison table | At least 1 table present | Warn user |
| Pro Tips | At least 3 `**Pro Tip**` callouts | Warn user |
| Meta description | 150-160 characters | Warn user, suggest revision |
| Image files | All `![...](images/...)` paths resolve to existing files | List missing images |
| CTA (Lensmor only) | Waitlist link present if article is Lensmor-related | Warn user |
| No fake links | All URLs are real (verified via WebFetch if needed) | Flag suspicious URLs |

- If **all checks pass**: proceed to Phase 5.
- If **any check fails**: report the failures and **PAUSE** for user decision (fix or publish anyway).

## Phase 5: Publish to Webflow

```bash
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category [CATEGORY]
```

Add `--publish` flag only if user confirms they want to go live immediately. Default is draft.

The `--category` value is resolved dynamically against Webflow CMS. If the provided category doesn't match, the script lists all available categories. Common categories include `strategy`, `playbooks`, `teardowns`, but check Webflow for the current list.

Optional flags:
- `--writer [NAME]` — assign a specific writer persona (random if omitted)
- `--collection_id [ID]` — override the default blog collection

## Decision Points (Where to Pause)

| When | Question | Skip Condition |
|------|----------|----------------|
| After Phase 1 | "Which topic and content type?" | Never skip |
| After Phase 2 (optional) | "Article looks good? Continue to images?" | Skip unless user requested review or topic is sensitive |
| After Phase 4 (if failures) | "Quality checks failed. Fix or publish anyway?" | Skip if all checks pass |
| After Phase 5 | Report success/failure, share the result | Never skip |

## File Structure

```
workspace/blog/
├── article.md          # Blog content with metadata
└── images/
    ├── cover_*.png     # Cover image
    ├── inline_1_*.png  # Inline images (count varies by article)
    ├── inline_2_*.png
    └── ...
```

## Error Handling

- **Ahrefs MCP unavailable**: Fall back to Quick Mode keyword research with qualitative estimates.
- **Image generation fails**: Log the error, continue with remaining images. Report failed images in Phase 4 quality gate.
- **Webflow publish fails**: Print error details (status code, response). Check API token/secrets. Do not retry automatically.
- **Brand guidelines not found**: Continue writing with general professional voice.
