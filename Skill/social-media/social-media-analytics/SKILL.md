---
name: social-media-analytics
description: "Social media analytics and data operations: analyzes performance data, produces growth insights, and drives strategy adjustments. Use this skill when reviewing social media performance, diagnosing growth issues, running content experiments, or generating weekly/monthly reports. Outputs insights to workspace/social-media-analytics.md for the strategy skill to consume."
---

# Social Media Analytics

Analyzes performance data, produces growth insights, and drives strategy adjustments. The data layer that makes the strategy skill smarter over time.

## When to Use

- Weekly quick review of social media performance
- Monthly deep-dive analysis
- When diagnosing growth stalls or engagement drops
- When evaluating content experiments
- When the strategy skill needs performance context for topic selection

## Dependencies

- `Skill/social-media/social-media-analytics/references/platform-benchmarks.md` — Baseline metrics for context
- `workspace/social-media-calendar.md` — Published content history (from strategy skill)
- `workspace/social-media-analytics.md` — Output file for insights (auto-created)

## Data Input Methods

Performance data can come from multiple sources. Use whichever is available:

### 1. User Manual Input

The user provides numbers directly:
```
LinkedIn post "AI tools" — 2,500 impressions, 89 likes, 12 comments, 5 shares
```

Parse into structured format and ask clarifying questions if data is incomplete.

### 2. Screenshot Analysis

The user shares a screenshot of platform analytics. Extract:
- Post-level metrics (impressions, engagement, clicks)
- Profile-level metrics (follower count, growth, profile views)
- Time-series data (if visible)

When reading screenshots, acknowledge any numbers that are unclear and confirm with the user.

### 3. Batch Data

The user provides a spreadsheet or structured list of multiple posts. Process in bulk and generate comparative analysis.

### 4. Ahrefs MCP (for traffic correlation)

Use Ahrefs tools to correlate social media efforts with website traffic:
- `site-explorer-metrics-history` — Track organic traffic trends alongside social posting cadence
- `site-explorer-referring-domains` — Check if social posts drive backlinks
- `web-analytics-source-channels` — See social media as a traffic channel (if Ahrefs Web Analytics is configured)
- `web-analytics-referrers` — Identify specific social posts driving traffic

This is supplementary data — not all social media posts aim for traffic. Use when evaluating the Global Marketing & Growth pillar specifically.

## Metrics Framework

Metrics organized by growth objective, not by platform.

### Tier 1: Audience Growth

| Metric | What It Measures | Where to Find |
|--------|-----------------|---------------|
| Follower count | Total audience size | Profile page |
| Follower growth rate | Speed of audience growth | (This week - Last week) / Last week |
| Profile views | Discovery and curiosity | Platform analytics |
| Follow-to-impression ratio | Conversion of views to followers | New followers / Total impressions |

**Healthy signals**: Steady week-over-week growth, profile views increasing proportionally with impressions.

### Tier 2: Engagement Quality

| Metric | What It Measures | Where to Find |
|--------|-----------------|---------------|
| Engagement rate | Overall content resonance | (Likes + Comments + Shares) / Impressions |
| Comment-to-like ratio | Discussion depth vs passive engagement | Comments / Likes |
| Save/bookmark rate | Content value (reference-worthy) | Saves / Impressions |
| Reply rate (Twitter) | Conversation generation | Replies / Impressions |
| Average dwell time | Content holding attention | Twitter analytics (if available) |

**Healthy signals**: Engagement rate above platform benchmark, comment-to-like ratio > 1:5, saves increasing over time.

### Tier 3: Traffic & Conversion

| Metric | What It Measures | Where to Find |
|--------|-----------------|---------------|
| Link clicks | Traffic generation | Platform analytics |
| CTR (click-through rate) | Content driving action | Clicks / Impressions |
| Website sessions from social | Actual traffic delivered | Ahrefs Web Analytics or GA |
| Waitlist signups from social | Bottom-funnel conversion | CRM / product analytics |

**Healthy signals**: Posts with links consistently get > 1% CTR, social referral traffic trending up.

### Tier 4: Brand Influence

| Metric | What It Measures | Where to Find |
|--------|-----------------|---------------|
| Mentions & tags | Others talking about you | Platform search / notifications |
| Reposts/Retweets by others | Content amplification | Platform analytics |
| DM inquiries | Direct interest | Inbox |
| Speaking/collaboration invites | Authority recognition | Inbox |

**Healthy signals**: Increasing organic mentions, quality DMs from target audience.

## Analysis Workflows

### Weekly Quick Review (~5 minutes)

Run this every week to stay on track.

**Input needed**: Last 7 days of post metrics (user provides or extracted from screenshots).

**Process**:

1. **List all posts from the past week** with key metrics:

   | Date | Platform | Account | Topic | Impressions | Engagement | Rate |
   |------|----------|---------|-------|-------------|------------|------|
   | ... | ... | ... | ... | ... | ... | ...% |

2. **Identify Top 3 performers** — Why did they work? Look for patterns in:
   - Topic/pillar
   - Format (story, list, data, opinion)
   - Hook style
   - Time of posting
   - Image vs. no image

3. **Identify Bottom 1-2 underperformers** — Why didn't they work? Consider:
   - Weak hook
   - Wrong audience/platform fit
   - Timing
   - Oversaturated topic

4. **Output 2-3 actionable adjustments** for next week:
   - e.g., "Double down on [topic type] — all 3 top posts were in this area"
   - e.g., "Try posting threads on Twitter — single tweets underperformed this week"
   - e.g., "Lensmor account needs more posts — only 1 this week vs. 5 personal"

5. **Write to `workspace/social-media-analytics.md`** (see Output Format below)

### Monthly Deep Dive (~15 minutes)

Run this at month's end for strategic adjustments.

**Input needed**: Full month of post metrics + follower/growth data.

**Process**:

1. **Pillar Performance Analysis**

   For each account (personal + company), calculate:

   | Pillar | Posts | Avg Engagement Rate | Avg Impressions | Best Performer |
   |--------|-------|--------------------|-----------------|----|
   | ... | ... | ...% | ... | [topic] |

   Flag any pillar with < 2 posts or significantly below-average engagement.

2. **Account Comparison**

   | Metric | Personal (Ivan) | Company (Lensmor) |
   |--------|----------------|-------------------|
   | Total posts | ... | ... |
   | Avg engagement rate | ...% | ...% |
   | Follower growth | +... | +... |
   | Best performing post | ... | ... |

3. **Format Analysis**

   Which content formats performed best this month?

   | Format | Count | Avg Engagement | Trend vs Last Month |
   |--------|-------|---------------|---------------------|
   | Personal story | ... | ... | ↑/↓/→ |
   | Data/insight | ... | ... | ↑/↓/→ |
   | How-to/tip | ... | ... | ↑/↓/→ |
   | Thread | ... | ... | ↑/↓/→ |

4. **Growth Trend**

   Plot or describe growth trajectory:
   - Follower count start → end of month
   - Is growth accelerating, steady, or decelerating?
   - Any spikes? What caused them?

5. **3 Strategic Recommendations** — specific, actionable, tied to data:
   - e.g., "Pillar X is underserved but high-performing — allocate 2 more posts next month"
   - e.g., "Company account engagement is below benchmark — test more data-driven content"
   - e.g., "Twitter threads outperform single tweets by 3x — shift to 60% thread format"

6. **Write full report to `workspace/social-media-analytics.md`**

### Content Experiment Tracking

For testing specific hypotheses about what works.

**Experiment Format**:

```
## Experiment: [Name]

**Hypothesis**: [What you expect to happen]
**Test**: [What you'll do differently]
**Duration**: [How long / how many posts]
**Metrics**: [What you'll measure]
**Control**: [What you're comparing against]

### Results

| Metric | Control | Test | Delta |
|--------|---------|------|-------|
| ... | ... | ... | +/-...% |

### Conclusion
[What we learned. Keep, stop, or modify?]

### Next Action
[What changes based on this experiment]
```

**Example experiments**:
- "Do posts with images get 2x more engagement than text-only on LinkedIn?"
- "Does posting at 8 AM vs 12 PM affect Twitter impressions?"
- "Do data-first hooks outperform story-first hooks for Lensmor's account?"

Track active experiments in the analytics file. Max 2 concurrent experiments to keep things manageable.

## Growth Diagnostics

When something isn't working, use these diagnostic paths.

### Follower Growth Stalled

```
Check → Impression volume
  ├─ Low impressions → Content not reaching new people
  │   ├─ Are you posting consistently? (< 3x/week is too low)
  │   ├─ Are you engaging with others' content? (Algorithm rewards reciprocity)
  │   └─ Are topics too niche? (Try broader pillar content)
  │
  └─ High impressions, low follows → Content reaches people but doesn't convert
      ├─ Is your profile/bio clear and compelling?
      ├─ Do posts demonstrate consistent expertise? (One-off viral ≠ followers)
      └─ Is there a clear "reason to follow"? (What value do I get over time?)
```

### Engagement Rate Dropping

```
Check → Has posting frequency changed?
  ├─ Posting more → Algorithm may be suppressing due to saturation
  │   └─ Reduce frequency, increase quality per post
  │
  └─ Same frequency → Content quality or relevance issue
      ├─ Check pillar mix — are you over-indexing on one topic?
      ├─ Check format — have you stopped doing what worked?
      ├─ Check hooks — are openings getting stale?
      └─ Check audience — has your follower base shifted?
```

### Low Traffic from Social

```
Check → Are you including links?
  ├─ No → Can't drive traffic without links. Add CTAs to 20-30% of posts.
  │
  └─ Yes, but low clicks → Link presentation issue
      ├─ Is the value proposition clear before the link?
      ├─ Are you using link-in-bio vs. inline links?
      ├─ Is the linked content actually valuable?
      └─ Platform-specific: LinkedIn suppresses posts with links in body
          └─ Try link in first comment instead
```

### Company Account Underperforming

```
This is expected. Company accounts get 30-60% lower organic reach.

Mitigation strategies:
1. Personal account amplification — Ivan shares/comments on Lensmor posts
2. Data-first content — company accounts perform best with unique data
3. Employee advocacy — team members reshare company content
4. Lower expectations — benchmark against company-page metrics, not personal
```

## Output Format

All analytics output is written to `workspace/social-media-analytics.md` for the strategy skill to consume.

**File structure**:

```markdown
# Social Media Analytics

Last updated: [date]
Review type: Weekly / Monthly

## Quick Summary

- **Period**: [date range]
- **Total posts**: [N] (Personal: [N], Company: [N])
- **Avg engagement rate**: [N]% (benchmark: [N]%)
- **Follower growth**: +[N] across all platforms
- **Top performer**: "[topic]" on [platform] — [key metric]

## Top Insights

1. [Insight with supporting data]
2. [Insight with supporting data]
3. [Insight with supporting data]

## Recommendations for Next Period

1. [Specific, actionable recommendation]
2. [Specific, actionable recommendation]
3. [Specific, actionable recommendation]

## Active Experiments

[Experiment tracking if any]

## Detailed Data

[Post-by-post breakdown tables]
```

## Related Skills

- [social-media-strategy](../social-media-strategy/) — Consumes analytics output for topic selection
- [social-media-pipeline](../social-media-pipeline/) — Orchestrates the full content workflow
- [personal-brand](../../personal-brand/) — Personal account brand definition
- [lensmor-brand-guideline](../../lensmor-brand-guideline/) — Company account brand definition
