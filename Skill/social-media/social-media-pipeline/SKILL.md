---
name: social-media-pipeline
description: "End-to-end social media content pipeline: strategy → writing → quality check → output. Use when the user wants to plan and produce social media content in one workflow, convert a blog post into social posts, or batch-produce a week of social media content. Routes to the correct writer and brand based on the content brief."
---

# Social Media Pipeline

Orchestrates the full social media content workflow: strategy → writing → quality check → output. The social media equivalent of the website content-pipeline.

## When to Use

- User says "write a social media post" without specifying the platform/account
- User wants the full strategy-to-output workflow
- User wants to convert a blog post into social media content
- User wants to batch-produce multiple social media posts
- User invokes this skill directly

## Workflow

```
Phase 1: Strategy          →  Decide what to post (social-media-strategy skill)
Phase 2: Writing           →  Route to correct writer + brand
Phase 3: Quality Check     →  Verify brand, platform, growth intent
Phase 4: Output            →  Save to workspace, update calendar
```

## Phase 1: Strategy

**Use the social-media-strategy skill** (`Skill/social-media/social-media-strategy/SKILL.md`) to decide what to post and why.

1. Check analytics data and calendar for context
2. Generate and score topic candidates (or validate user's topic)
3. Produce a **Content Brief** with topic, account, platform, pillar, and angle

**Content Brief format**:
```
Topic: [specific post topic]
Account: Personal (Your Name) / Company (MyCompany)
Platform: LinkedIn / Twitter / Jike
Content Pillar: [pillar name]
Source Type: Original / Blog Repurpose / Hot Take / Community
Angle: [specific perspective or hook]
Growth Rationale: [why this post, why now]
Notes: [optional reference material]
```

**PAUSE**: Present the Content Brief to the user for approval.

If the user already knows exactly what they want (specific topic + platform + account), abbreviate this phase — but still produce a Content Brief to maintain the structured handoff.

## Phase 2: Writing

Route to the correct writer skill and brand guideline based on the Content Brief.

### Routing Table

| Account | Platform | Writer Skill | Brand Guideline |
|---------|----------|-------------|-----------------|
| Personal (Your Name) | LinkedIn | `social-media/linkedin-post-writer/SKILL.md` | `personal-brand/SKILL.md` |
| Company (MyCompany) | LinkedIn | `social-media/linkedin-post-writer/SKILL.md` (Company Mode) | `mycompany-brand-guideline/SKILL.md` |
| Personal (Your Name) | Twitter/X | `social-media/twitter-post-writer/SKILL.md` | `personal-brand/SKILL.md` |
| Company (MyCompany) | Twitter/X | `social-media/twitter-post-writer/SKILL.md` (Company Mode) | `mycompany-brand-guideline/SKILL.md` |
| Personal (Your Name) | Jike | `social-media/jike-post-writer/SKILL.md` | `personal-brand/SKILL.md` |

**Routing rules**:
- LinkedIn and Twitter writers both support Account Mode — pass the mode from the Content Brief
- Jike is always personal account, always Chinese — no company mode exists
- The writer skill handles all platform-specific formatting, length, and style requirements
- Pass the Content Brief's `Angle` and `Notes` fields as input context to the writer

### Writer Invocation

When calling the writer skill:
1. Load the correct brand guideline first
2. Set the account mode (Personal or Company)
3. Pass the topic, angle, and any reference material
4. Let the writer handle the rest (structure, hook, CTA, image generation)

## Phase 3: Quality Check

After the writer produces a draft, verify against this checklist before output.

### Quality Checklist

| # | Check | Pass Criteria | Action if Failed |
|---|-------|--------------|------------------|
| 1 | **Brand consistency** | Voice matches the account mode (personal vs company) | Rewrite sections that break voice |
| 2 | **Platform adaptation** | Format, length, and style fit the target platform | Adjust to platform norms |
| 3 | **Growth intent** | Post has a clear reason to exist (teaches, inspires, positions, drives traffic) | Add value or reconsider the topic |
| 4 | **No duplicate content** | Not a repeat of recent posts (check calendar) | Find a new angle or drop |
| 5 | **Pillar alignment** | Content matches the assigned pillar from the Content Brief | Realign or reassign pillar |
| 6 | **Cross-account check** | Personal and company not posting same topic on same day | Stagger by 1+ days |
| 7 | **Language correct** | English for LinkedIn/Twitter, Chinese for Jike | Fix language |
| 8 | **CTA appropriate** | Personal: discussion question / Company: link or value CTA | Adjust CTA style |
| 9 | **Image generated** | Visual matches account mode rules (company = Linear Dark Mode only) | Regenerate correct style |

- If **all checks pass**: proceed to Phase 4.
- If **any check fails**: fix in place. Only PAUSE for user input if the fix requires a content direction change.

## Phase 4: Output

### Save Content

Save the finished post to `workspace/social-media/`:

```
workspace/social-media/
├── [date]-[platform]-[account]-[topic-slug].md
├── [date]-[platform]-[account]-[topic-slug]_linear.png   (if image)
├── [date]-[platform]-[account]-[topic-slug]_photo.png    (if personal + LinkedIn)
└── ...
```

**File naming convention**: `YYYY-MM-DD-platform-account-topic.md`
- Example: `2026-02-24-linkedin-personal-ai-coding-tools.md`
- Example: `2026-02-24-twitter-mycompany-event-data-insight.md`

**File content**:
```markdown
# [Platform] Post — [Account]

**Date**: [date]
**Account**: Personal (Your Name) / Company (MyCompany)
**Platform**: LinkedIn / Twitter / Jike
**Pillar**: [pillar name]
**Status**: Ready

---

[Post content — copy-paste ready]

---

**Hashtags**: [if applicable]
**Image**: [filename if generated]
**Notes**: [any context for when publishing manually]
```

### Update Calendar

After saving, update `workspace/social-media-calendar.md`:
1. Add the post to the **Upcoming** section with status `Ready`
2. When the user confirms it's been published, move to **Published**
3. Update pillar coverage counts

### Report to User

Present the final output clearly:
- The post text (copy-paste ready)
- Image file paths (if generated)
- Which account and platform this is for
- Any notes for manual publishing

## Batch Mode

### Blog Repurpose (1 blog → 4-6 social posts)

When converting a blog post to social media:

1. **Phase 1 (Strategy)**: Use the blog-to-social conversion process from the strategy skill
   - Read the full blog post
   - Extract 3-5 distinct angles
   - Assign each to the best account + platform
   - Produce a Content Brief for each

2. **PAUSE**: Present all Content Briefs to user for approval (approve/modify/remove any)

3. **Phase 2-4**: Execute each approved brief sequentially
   - Route each to the correct writer
   - Run quality checks
   - Save all outputs

4. **Spacing recommendation**: Suggest a posting schedule that spaces content across 3-5 days

### Weekly Batch Plan

When planning a full week of social media:

1. **Phase 1 (Strategy)**: Run the full topic selection process with a weekly lens
   - Target: 5-8 posts across all platforms and accounts
   - Ensure pillar balance across the week
   - Mix content types and formats

2. **PAUSE**: Present the weekly plan as a table:

   | Day | Platform | Account | Topic | Pillar | Source |
   |-----|----------|---------|-------|--------|--------|
   | Mon | LinkedIn | Personal | ... | ... | Original |
   | Tue | Twitter | Personal | ... | ... | Blog repurpose |
   | Wed | LinkedIn | MyCompany | ... | ... | Original |
   | ... | ... | ... | ... | ... | ... |

3. **Phase 2-4**: Execute each approved brief

4. **Save all** to `workspace/social-media/` with proper naming

## Decision Points (Where to Pause)

| When | Question | Skip Condition |
|------|----------|----------------|
| After Phase 1 | "Approve this Content Brief?" | Never skip |
| After Phase 1 (batch) | "Approve these Content Briefs?" | Never skip |
| After Phase 3 (if quality issues) | "Quality check found issues. Fix or proceed?" | Skip if all checks pass |
| After Phase 4 | Report output and file paths | Never skip |

## Error Handling

- **Strategy skill not needed**: If the user provides a complete brief (topic + platform + account + angle), skip Phase 1 but still validate the brief format.
- **Writer skill produces off-brand content**: Re-invoke with explicit brand reminders. If persistent, flag to user.
- **Calendar file missing**: Create from template. Don't block the pipeline.
- **Image generation fails**: Continue without image. Note the failure in output and suggest retrying.
- **Jike in company mode requested**: Reject — Jike is always personal. Suggest Twitter or LinkedIn for company content.

## Related Skills

- [social-media-strategy](../social-media-strategy/) — Phase 1: topic selection and content briefs
- [social-media-analytics](../social-media-analytics/) — Data input for strategy decisions
- [linkedin-post-writer](../linkedin-post-writer/) — Phase 2: LinkedIn post writing
- [twitter-post-writer](../twitter-post-writer/) — Phase 2: Twitter post writing
- [jike-post-writer](../jike-post-writer/) — Phase 2: Jike post writing
- [personal-brand](../../personal-brand/) — Personal account brand definition
- [mycompany-brand-guideline](../../mycompany-brand-guideline/) — Company account brand definition
