---
name: social-media-strategy
description: "Social media strategy layer: decides what to post, on which platform, using which account, and why. Use this skill when planning social media content, choosing topics, converting blog posts to social media angles, or managing the content calendar. This skill produces Content Briefs that feed into the social-media-pipeline for execution."
---

# Social Media Strategy

Decides **what to post, where, with which account, and why** — the strategy brain for all social media content.

## When to Use

- Before writing any social media post, to choose the right topic and account
- When the social-media-pipeline reaches the Strategy phase
- When converting a blog post into social media content
- When planning a weekly or monthly social media calendar
- When auditing pillar coverage and content balance

## Dependencies

- `Skill/personal-brand/SKILL.md` — Personal account voice and pillars
- `Skill/lensmor-brand-guideline/SKILL.md` — Company account voice and positioning
- `Skill/social-media/social-media-strategy/references/social-content-pillars.md` — Pillar definitions for both accounts
- `workspace/social-media-calendar.md` — Persistent social media calendar (auto-created if missing)
- `workspace/social-media-analytics.md` — Performance data (if available, from analytics skill)

## Account Model

Two account types with different content directions:

| Dimension | Personal (Ivan) | Company (Lensmor) |
|-----------|----------------|-------------------|
| Brand source | `personal-brand/SKILL.md` | `lensmor-brand-guideline/SKILL.md` |
| Platforms | LinkedIn, Twitter/X, Jike | LinkedIn, Twitter/X |
| Voice | Conversational, personal stories, opinions | Professional, data-driven, results-focused |
| Pronouns | "I", "me", "my" | "Lensmor", "we", "our" (or no pronoun) |
| Content source | Personal experience, observations | Product value, industry data, customer stories |
| CTA style | Questions, invite discussion | Links to product, waitlist, blog |

### Account Selection Decision Tree

```
Is this about Lensmor's product, features, or company news?
  → Yes → Company account (Lensmor)

Is this industry data/insight that positions Lensmor's expertise?
  → Yes → Company account (Lensmor)
  → But told through personal founder experience? → Personal account (Ivan)

Is this a personal opinion, story, or experience?
  → Yes → Personal account (Ivan)

Is this for Jike?
  → Yes → Always personal account (Ivan), always Chinese

When unclear:
  → Default to personal account (Ivan) — personal content outperforms brand content for solo founders
```

## Content Source Types

| Source | Description | Typical Output |
|--------|-------------|---------------|
| **Original** | New idea, observation, or experience | 1 post |
| **Blog repurpose** | Extract angles from a published blog post | 3-5 posts across platforms |
| **Hot take / reaction** | Response to industry news or trending topic | 1-2 posts, fast turnaround |
| **Community interaction** | Contribute to ongoing discussions | 1 reply-style post |

## Topic Selection Process

### Step 1: Check Data

Read available performance data to understand what's working:

1. `workspace/social-media-analytics.md` — recent performance insights (if exists)
2. `workspace/social-media-calendar.md` — what's been posted recently, pillar coverage

If the analytics file doesn't exist, skip to Step 2. If the calendar doesn't exist, create one using the template in Calendar Management below.

Pay attention to:
- Which content pillars are over/under-represented
- Which post formats and topics performed best recently
- Any recommendations from the analytics skill

### Step 2: Check Calendar

Read `workspace/social-media-calendar.md` and assess:

| Dimension | Question |
|-----------|----------|
| **Pillar balance** | Which pillar has the fewest recent posts? Any pillar at 0 for the past 2 weeks? |
| **Account balance** | Is one account dominating? Personal and company should both have regular posts. |
| **Platform coverage** | Any platform neglected? |
| **Recency** | What was the last post on each platform? Gap > 5 days = attention needed. |

### Step 3: Generate Candidates

Based on data + calendar gaps, generate 3-5 candidate topics. Consider:
- User's input (if they have a specific idea or topic)
- Underserved pillars that need coverage
- Recent blog posts available for repurposing
- Industry news or trends worth reacting to
- Upcoming events or product milestones

### Step 4: Score and Rank

| # | Topic | Account | Platform | Pillar | Relevance (1-5) | Gap Fill (1-5) | Timeliness (1-5) | Growth Potential (1-5) | Total |
|---|-------|---------|----------|--------|-----------------|----------------|-------------------|----------------------|-------|
| 1 | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Scoring guide:**
- **Relevance (1-5)**: How well does this match the audience's current interests? 5 = burning topic.
- **Gap Fill (1-5)**: How much does this address a pillar or platform gap? 5 = severely underserved.
- **Timeliness (1-5)**: Is there a reason to post this now? 5 = today or never.
- **Growth Potential (1-5)**: Will this drive followers, engagement, or traffic? 5 = high viral/share potential.

### Step 5: Output Content Brief

For each approved topic, produce a Content Brief:

```
Topic: [specific post topic]
Account: Personal (Ivan) / Company (Lensmor)
Platform: LinkedIn / Twitter / Jike
Content Pillar: [pillar name from social-content-pillars.md]
Source Type: Original / Blog Repurpose / Hot Take / Community
Angle: [specific perspective or hook]
Growth Rationale: [why this post, why now — ties to data or gap]
Notes: [optional: reference material, blog URL, specific points to include]
```

**PAUSE**: Present the Content Brief to the user for approval before passing to the pipeline.

## Blog-to-Social Conversion

When repurposing a blog post into social media content:

### Process

1. **Read the full blog post** — understand the core argument, key data points, and unique angles
2. **Extract 3-5 distinct angles** — each angle should work as a standalone post, not a summary
3. **Assign each angle** to the best account + platform combination
4. **Ensure variety** — different hooks, different formats, different days

### Angle Extraction Framework

From one blog post, look for:

| Angle Type | What to Extract | Example |
|------------|----------------|---------|
| **Key insight** | The most surprising or contrarian finding | "We found that X is actually Y" |
| **Data point** | A specific statistic or number | "87% of exhibitors don't do pre-show research" |
| **Story/anecdote** | A narrative element from the post | "When we talked to [type of user], they said..." |
| **How-to** | An actionable process or framework | "3 steps to evaluate a trade show before committing" |
| **Contrarian take** | A perspective that challenges conventional wisdom | "Most companies measure event ROI wrong — here's why" |

### Assignment Rules

- **Data-heavy angles** → Company account (positions Lensmor as data authority)
- **Personal story angles** → Personal account (builds Ivan's thought leadership)
- **How-to angles** → Platform with most space (LinkedIn > Twitter)
- **Contrarian takes** → Twitter (thrives on sharp opinions)
- **Chinese adaptation** → Jike (personal account, culturally adapted, not translated)

### Spacing

- Don't post all repurposed content on the same day
- Space across 3-5 days minimum
- Vary platforms: don't hit the same platform 3 times in a row from the same blog

## Calendar Management

### Calendar Format

The social media calendar lives at `workspace/social-media-calendar.md`:

```markdown
# Social Media Calendar

Last updated: [date]

## Pillar Coverage (Rolling 30 Days)

### Personal Account
| Pillar | Target | Actual | Posts |
|--------|--------|--------|-------|
| AI Productivity | 35% | ...% | N |
| Enterprise AI | 25% | ...% | N |
| Global Marketing | 25% | ...% | N |
| Trade Show | 15% | ...% | N |

### Company Account
| Pillar | Target | Actual | Posts |
|--------|--------|--------|-------|
| Event Intelligence | 40% | ...% | N |
| Product Value | 25% | ...% | N |
| Customer Success | 20% | ...% | N |
| Thought Leadership | 15% | ...% | N |

## Upcoming (Planned)

| Date | Account | Platform | Topic | Pillar | Status |
|------|---------|----------|-------|--------|--------|
| ... | ... | ... | ... | ... | Planned/Draft/Ready |

## Published (Recent)

| Date | Account | Platform | Topic | Pillar | Performance |
|------|---------|----------|-------|--------|-------------|
| ... | ... | ... | ... | ... | [brief note] |
```

### Status Lifecycle

```
Planned → Draft → Ready → Published
```

- **Planned**: Content Brief approved, not yet written
- **Draft**: Post written, pending review
- **Ready**: Post reviewed and approved, waiting to publish
- **Published**: Live on platform

### Updating the Calendar

After each strategy session:
1. Add approved Content Briefs to the **Upcoming** section
2. Update pillar coverage counts
3. Move published posts from Upcoming to Published
4. Flag any pillar imbalances

## Cross-Platform Coordination Rules

1. **Same topic, different execution**: If covering the same theme on multiple platforms, each post must have a different hook, format, and angle. Never cross-post identical content.
2. **Stagger timing**: Same-topic posts across platforms should be 1-2 days apart minimum.
3. **Account separation**: Personal and company accounts should not post about the same specific topic on the same day.
4. **Platform-native content**: Each post must feel native to its platform. A LinkedIn post is not a long tweet. A tweet is not a compressed LinkedIn post.
5. **Jike is independent**: Jike content can overlap thematically with English platforms but should be culturally adapted, not translated.

## Integration with Social Media Pipeline

This skill is Phase 1 of the social-media-pipeline:

```
Phase 1: Strategy          →  THIS SKILL — decide what to post
Phase 2: Writing           →  Route to correct writer + brand
Phase 3: Quality Check     →  Verify brand, platform, growth intent
Phase 4: Output            →  Save to workspace, update calendar
```

**Handoff to pipeline**: Pass the Content Brief. The pipeline uses the Account + Platform fields to route to the correct writer skill and brand guideline.

## Error Handling

- **No analytics file**: Normal on first run. Focus on pillar balance and start with the most foundational topics.
- **No calendar file**: Create one using the template above. Start fresh with an empty Published section.
- **User has no topic idea**: Run the full 5-step selection process. Use pillar gaps and timeliness as primary drivers.
- **User has a specific topic**: Abbreviate Steps 1-3. Still produce a Content Brief to maintain structured handoff.
- **Conflicting account choice**: When a topic could work for either account, default to personal unless the content is specifically about Lensmor's product or company data.
