---
name: content-pipeline
description: "End-to-end content pipeline: content strategy → keyword research → blog writing → image generation → Webflow publishing. Use when the user wants to research, write, and publish a blog post in one workflow."
---

# Content Pipeline

Orchestrates the full content workflow: CMS review → content strategy → keyword research → article writing → image generation → quality check → Webflow publishing.

## When to Use

- User says "write and publish a blog post"
- User wants the full keyword → article → publish flow
- User invokes this skill directly

## Workflow

```
Phase 0: CMS Review           →  Fetch existing articles, identify gaps
Phase 1: Content Strategy      →  Decide what to write and why (content-strategy skill)
Phase 2: Keyword Research      →  Validate keywords from Content Brief
Phase 3: Write Article         →  Save to workspace/blog/
Phase 4: Generate Images       →  Cover + inline (count based on article)
Phase 5: Quality Gate          →  Auto-check before publishing
Phase 6: Publish to Webflow
```

## Phase 0: CMS Review

**Always run this first.** Fetch existing published articles to prevent content overlap and SEO cannibalization.

```bash
python Skill/webflow-blog-publisher/scripts/list_articles.py --published-only
```

After fetching, build a mental map of:

1. **Existing primary keywords** — the script now shows each article's primary keyword in a dedicated column. This is the first keyword in the `primary-keywords` CMS field and must be unique across all articles.
2. **Content gaps** — what topics are missing from the current blog?
3. **Cannibalization risks** — which existing articles could compete with a new topic for the same search queries?

Keep this list available throughout Phase 1 and Phase 2. When proposing new topics, **cross-reference against existing articles' primary keywords** and flag any overlap.

### Keyword Convention

Each article's `**Primary Keywords**` field uses a comma-separated list with a strict convention:
- **First keyword** = the unique primary target keyword. This must not duplicate any existing article's primary keyword (the first keyword in their list).
- **Remaining keywords** = secondary/supporting keywords. These may overlap across articles within the same topic cluster.

### Cannibalization Rules

- **Same primary keyword**: Do NOT write a new article targeting the same primary keyword as an existing one. Either update the existing article or pick a different angle.
- **Same intent, different wording**: Two primary keywords that map to the same search intent count as a conflict (e.g., "trade show lead capture" vs "how to capture leads at trade shows"). Check by asking: would Google show the same results for both queries?
- **Overlapping secondary keywords**: Acceptable as long as the articles have clearly different primary keywords and search intents (e.g., existing = "what is X" informational, new = "X vs Y" commercial).
- **Same topic cluster**: New articles in the same cluster should link to existing ones as internal links and cover a distinct subtopic.

## Phase 1: Content Strategy

**Use the content-strategy skill** (`Skill/content-strategy/SKILL.md`) to decide what to write and why.

This phase ensures topic selection is driven by content gaps and audience needs, not just keyword opportunity.

1. Run `sync_calendar.py` to pull latest CMS data into the content calendar.
2. Analyze pillar coverage, funnel stage gaps, and timeliness opportunities.
3. Score 3-5 candidate topics and choose the best one.
4. Produce a **Content Brief** with topic, angle, content type, persona, funnel stage, pillar, and seed keyword directions.

**PAUSE**: Present the Content Brief to the user for approval. The brief's `Keyword Direction` field feeds directly into Phase 2.

If the user already has a specific topic in mind, this phase can be abbreviated — but still produce a Content Brief to maintain the structured handoff to keyword research.

## Phase 2: Keyword Research

**All keyword decisions must be data-driven.** Always use the **keyword-research** skill (`Skill/keyword-research/SKILL.md`) with Ahrefs MCP to get real search volume, difficulty, and traffic potential. Never rely on AI-estimated competition levels.

Choose scope based on context:

### With Content Brief from Phase 1 (default)

When Phase 1 produced a Content Brief, pass its `Keyword Direction` field to the keyword-research skill. This automatically triggers **Focused Mode** — the skill uses the brief's seed keyword directions instead of starting from scratch.

1. If the topic is Lensmor-related, read brand context:
   - `Skill/brand-guidelines/SKILL.md`
   - `Skill/brand-guidelines/resources/product-details.md`

2. Brainstorm 10-15 keyword variations around the Content Brief's keyword directions (core terms, problem/solution angles, long-tail, questions).

3. Query Ahrefs for each keyword to get Volume, KD, and Traffic Potential.

4. Present a **short table** of top 5-8 keyword candidates with real data:

   | # | Article Topic | Target Keyword | Volume | KD | Intent | GEO Potential | Overlap with Existing? |
   |---|--------------|----------------|--------|-----|--------|---------------|----------------------|
   | 1 | ... | ... | ... | ... | ... | Yes/No | None / [article title] |

### Exploratory Mode (no Content Brief)

Use when Phase 1 was skipped or the user wants to identify keyword opportunities before choosing a topic.

1. Run the full keyword-research skill workflow: broad seed generation → Ahrefs data → topic cluster organization.

2. Present results grouped by topic cluster with prioritized recommendations.

### If Ahrefs MCP is unavailable

Fall back to manual SERP checks and clearly label all metrics as estimates. Flag this limitation to the user so they can validate before committing to a topic.

### After either mode

**PAUSE**: Ask the user to:
1. Confirm the target keyword (or suggest their own)
2. Confirm the **content type** (if not already set in Content Brief):

   | Content Type | Word Count Target | Typical Structure |
   |-------------|-------------------|-------------------|
   | How-to guide | 2,000–2,500 | Numbered steps under H3 headers |
   | List article | 1,800–2,200 | Grouped items with narrative |
   | Comparison post | 2,200–2,800 | Side-by-side analysis + tables |
   | Pillar content | 2,800–3,000 | Comprehensive deep-dive |

If the chosen topic overlaps with an existing article, explicitly confirm with the user whether to:
- **Differentiate**: Write with a distinct angle/intent (explain the angle)
- **Update**: Revise the existing article instead of creating a new one

## Phase 3: Write Article

Follow the blog-writer guidelines (`Skill/blog-writer/SKILL.md`):

1. Write the article in markdown with this header format:
   ```
   # [Title]

   **Slug**: /blog/[category]/[keyword-slug]
   **Meta Description**: [150-160 chars]
   **Primary Keywords**: [primary keyword, secondary keyword, ...]
     ↑ First = unique primary target; rest = secondary (see Keyword Convention in Phase 0)
   **Reading Time**: [estimated minutes, number only]
   **Cover Image**:
   ![description](images/cover.png)

   ---

   [Article body]
   ```

2. Key requirements (adjusted by content type from Phase 2):
   - Word count within the target range for the chosen content type
   - 1+ comparison table
   - 3+ Pro Tips
   - Narrative paragraphs (avoid bullet lists)
   - If Lensmor-related: include waitlist CTA (`https://accounts.lensmor.com/waitlist`)
   - No fake links — only include real, verified URLs

3. **Content differentiation** (informed by Phase 0):
   - Do NOT reuse the same examples, statistics, or anecdotes as existing articles
   - If covering a related topic, take a different angle (different audience segment, different use case, different stage of the funnel)
   - Add internal links to related existing articles where natural

4. Add image placeholders (`![description](images/filename.png)`) where visuals would enhance the content. Place them based on article needs:
   - Short articles (< 2,200 words): cover + 1-2 inline
   - Medium articles (2,200-2,800 words): cover + 2-3 inline
   - Long articles (> 2,800 words): cover + 3-4 inline

5. Save to `workspace/blog/article.md` (relative to repository root).

**PAUSE (optional)**: If the user requested a review, or if the article topic is complex/sensitive, show a summary (title, structure outline, word count) and ask to confirm before generating images. Otherwise, continue directly.

## Phase 4: Generate Images

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

### Image differentiation

To avoid visual repetition across blog posts:
- **Vary the `--type`**: If a recent article used `data_cluster` + `data_flow`, try `segmentation` + `temporal` for the new one.
- **Vary the concept prompt**: Even for similar topics, describe different visual metaphors. E.g., for two articles about lead generation, one could visualize "funnel stages as layered geometric platforms" while another visualizes "network graph of interconnected prospect nodes."
- **Vary composition**: Alternate between horizontal flow layouts, radial/centered layouts, and layered depth layouts across articles.

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

## Phase 5: Quality Gate

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
| Content overlap | No major paragraph-level duplication with existing CMS articles | Flag overlapping sections |
| SEO cannibalization | Primary keyword is not the same as any existing article's target keyword | Warn user, suggest differentiating |
| List syntax | All `1.` / `-` lists have a blank line before and after; no inline `<br>-` patterns | Fix lists to use standard markdown syntax |
| Table syntax | All tables use pipe `\|` syntax with `\|---\|` header separator; no run-on text tables | Rebuild as proper markdown tables |
| Heading syntax | No per-word `**bold**` in headings (e.g. `### **How** **do**...` is wrong) | Remove bold wrapping from heading text |

- If **all checks pass**: proceed to Phase 6.
- If **any check fails**: report the failures and **PAUSE** for user decision (fix or publish anyway).

## Phase 6: Publish to Webflow

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

The sort field is automatically set to the number of published articles + 1.

## Decision Points (Where to Pause)

| When | Question | Skip Condition |
|------|----------|----------------|
| After Phase 0 | None — informational only | Never skip the review itself |
| After Phase 1 | "Approve this Content Brief?" | Never skip |
| After Phase 2 | "Confirm target keyword and content type?" | Never skip |
| After Phase 2 (if overlap) | "Differentiate or update existing?" | Skip if no overlap detected |
| After Phase 3 (optional) | "Article looks good? Continue to images?" | Skip unless user requested review or topic is sensitive |
| After Phase 5 (if failures) | "Quality checks failed. Fix or publish anyway?" | Skip if all checks pass |
| After Phase 6 | Report success/failure, share the result | Never skip |

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

- **CMS fetch fails**: Warn user that dedup check is unavailable, proceed with caution.
- **Ahrefs MCP unavailable**: Fall back to Quick Mode keyword research with qualitative estimates.
- **Image generation fails**: Log the error, continue with remaining images. Report failed images in Phase 5 quality gate.
- **Webflow publish fails**: Print error details (status code, response). Check API token/secrets. Do not retry automatically.
- **Brand guidelines not found**: Continue writing with general professional voice.
