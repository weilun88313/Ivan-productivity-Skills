---
name: content-strategy
description: "Content strategy layer: decides what to write and why, based on content pillars, gap analysis, and audience needs. Sits between CMS Review and Keyword Research."
---

# Content Strategy

Decides **what to write and why** by analyzing content gaps, pillar coverage, and audience needs. Content value first, SEO second.

## When to Use

- Before keyword research, to choose a topic with strategic intent
- When the content-pipeline reaches Phase 1
- When you need to audit content coverage across pillars
- When planning a content calendar or batch of articles

## Dependencies

- `Skill/website/webflow-blog-publisher/scripts/list_articles.py` — CMS data source
- `Skill/website/content-strategy/references/content-pillars.md` — pillar definitions
- `workspace/content-calendar.md` — persistent content calendar (auto-created)

## Topic Selection Process

### Step 1: Sync Calendar

Run the sync script to pull latest CMS data into the content calendar:

```bash
python Skill/website/content-strategy/scripts/sync_calendar.py
```

This updates the **Published** section and **Pillar Coverage** table in `workspace/content-calendar.md`. If the calendar doesn't exist, it creates one from the template.

### Step 2: Read Current State

Read both files to understand the landscape:

1. `workspace/content-calendar.md` — current coverage, backlog, and published articles
2. `Skill/website/content-strategy/references/content-pillars.md` — pillar definitions and topic directions

Pay attention to:
- Which pillars have the most/fewest articles
- Which funnel stages are underrepresented
- What's already in the backlog vs. published

### Step 3: Identify Content Gaps

Analyze gaps across three dimensions:

| Dimension | Question |
|-----------|----------|
| **Pillar balance** | Which pillar has the fewest articles? Is any pillar at 0? |
| **Funnel coverage** | Are we missing awareness, consideration, or decision content? |
| **Timeliness** | Any seasonal events, industry trends, or product launches to capitalize on? |

Also consider:
- What questions do the target personas ask that we haven't answered?
- What competitor content exists that we should counter?
- What internal links are missing that a new article could fill?

### Step 4: Score Candidates

Generate 3-5 candidate topics and score them:

| # | Topic | Pillar | Funnel Stage | Audience Need (1-5) | Content Gap (1-5) | Timeliness (1-5) | Total |
|---|-------|--------|-------------|---------------------|-------------------|-------------------|-------|
| 1 | ... | ... | ... | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... | ... | ... |

**Scoring guide:**
- **Audience Need (1-5)**: How much does the target persona care about this? 5 = burning pain point.
- **Content Gap (1-5)**: How underserved is this topic in our existing content? 5 = nothing published.
- **Timeliness (1-5)**: Is there a reason to publish this now? 5 = event/season/trend makes it urgent.

### Step 5: Choose Angle

For the top-scoring topic, define:

1. **Specific angle** — what's the unique take? (not just "guide to X")
2. **Content type** — how-to, list, comparison, or pillar content
3. **Differentiation** — how does this differ from existing articles in our CMS?
4. **Internal linking** — which existing articles should link to/from this one?

### Step 6: PAUSE — User Confirmation

Present the **Content Brief** (format below) to the user and wait for approval before proceeding to keyword research.

## Content Brief Format

Every topic decision produces a Content Brief that gets added to the calendar backlog and passed to downstream skills:

```
Topic: [specific article topic]
Angle: [unique perspective or approach]
Content Type: how-to / list / comparison / pillar
Target Persona: [who is this for]
Funnel Stage: awareness / consideration / decision
Content Pillar: [one of the 5 pillars]
Keyword Direction: [2-3 seed keyword directions for keyword-research to validate]
Rationale: [why this article, why now — ties back to gap analysis]
```

The **Keyword Direction** field is intentionally not final keywords — it gives the keyword-research skill starting points to find the best data-backed target keyword.

## Calendar Management Rules

### Adding to Backlog

When a Content Brief is approved:
1. Add it to the **Backlog** section of `workspace/content-calendar.md`
2. Assign priority: P1 (write next), P2 (write soon), P3 (future)
3. Set status to `Approved`
4. Update the **Pillar Coverage** table

### Status Lifecycle

```
Proposed → Approved → In Progress → Published
```

- **Proposed**: Topic scored but not yet confirmed by user
- **Approved**: User confirmed the Content Brief
- **In Progress**: Article is being written (Phase 2+)
- **Published**: Article live on CMS (auto-updated by sync script)

### Updating Existing Articles

When gap analysis reveals an existing article needs updating (not a new article):
1. Add an entry to the **Updates Log** section instead of Backlog
2. Note what needs changing and why
3. This does NOT go through keyword research — it goes directly to the writing phase

## Integration with Content Pipeline

This skill is Phase 1 of the content-pipeline:

```
Phase 0: CMS Review           →  Fetch existing articles
Phase 1: Content Strategy      →  THIS SKILL — decide what to write
Phase 2: Keyword Research      →  Validate keywords from Content Brief
Phase 3: Write Article
Phase 4: Generate Images
Phase 5: Quality Gate
Phase 6: Publish to Webflow
```

**Handoff to keyword-research**: Pass the Content Brief's `Keyword Direction` field. The keyword-research skill should enter **Focused Mode** using these seed directions instead of starting from scratch.

## Error Handling

- **sync_calendar.py fails**: Warn user that calendar may be stale, proceed with last-known data.
- **No content-pillars.md**: Cannot proceed — this file is required for gap analysis.
- **Empty calendar**: Normal on first run. Focus on pillar balance and start with the most foundational topics (awareness-stage pillar content).

## Related Skills

- [content-pipeline](../content-pipeline/) — Orchestrates the full workflow
- [keyword-research](../keyword-research/) — Validates keyword targets from Content Brief
- [blog-writer](../blog-writer/) — Writes the article
- [mycompany-brand-guideline](../mycompany-brand-guideline/) — Brand context for MyCompany content
