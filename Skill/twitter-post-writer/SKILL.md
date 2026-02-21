---
name: twitter-post-writer
description: Write high-engagement X (Twitter) posts optimized for the recommendation algorithm. Use when users want to create, draft, or improve Twitter/X posts, threads, or content strategy. Applies algorithm-backed best practices for maximizing reach, engagement, and impressions through understanding of ranking factors like interaction probability, user behavior patterns, and content optimization techniques.
---

# Twitter Post Writer

## Overview

This skill helps create X (Twitter) posts optimized for maximum engagement and algorithmic visibility. Based on understanding of the X recommendation algorithm (Home Mixer system), it guides the creation of content that maximizes impressions, interactions, and reach.

## ⚠️ CRITICAL REQUIREMENTS

### 1. Language Requirement
**ALL Twitter posts MUST be written in English**, regardless of the user's input language.

- If user provides content in Chinese or other languages, translate to English first
- Maintain the core message and tone while adapting to English Twitter conventions
- Use natural, native-level English phrasing

### 2. Visual Content Generation
When visual content would enhance engagement:

- Use **Gemini 3 Pro Image** API for image generation
- Optimize images for Twitter: 16:9 aspect ratio (recommended for maximum visibility)
- Alternative ratios: 1:1 (square) or 4:3 for specific use cases
- Run `scripts/generate_twitter_image.py` with appropriate prompt

**Image Generation Workflow**:
```bash
python3 scripts/generate_twitter_image.py "your image prompt" --aspect-ratio 16:9
```

The script will:
1. Load API key from `.env` (GEMINI_API_KEY)
2. Generate high-quality image using Gemini 3 Pro
3. Save to `twitter_image.png` in current directory
4. Provide image for attachment to tweet

## How X Algorithm Works

The "For You" feed uses a three-stage pipeline:

**1. Candidate Sourcing**
- **In-Network**: Recent posts from accounts you follow
- **Out-of-Network**: ML-discovered posts from across the platform

**2. Scoring (Phoenix Scorer)**
- Predicts interaction probabilities using Transformer models
- Evaluates: P(like), P(retweet), P(reply), P(click), P(dwell_time)
- Calculates weighted score: `Final Score = Σ (weight × P(action))`

**3. Filtering**
- Removes duplicates, viewed content, blocked/muted accounts
- Applies diversity scoring to prevent author repetition

### What Drives Rankings

✅ **Positive Signals** (increase ranking):
- Likes/favorites
- Retweets/reposts
- Replies
- Click-throughs
- Long dwell time (user stays on post)
- Profile clicks
- Video/photo views

❌ **Negative Signals** (decrease ranking):
- Blocks
- Mutes
- Reports
- "Not interested" clicks
- Quick scroll-past (low dwell time)

## Content Strategy Guidelines

### Core Principles

1. **Maximize Interaction Probability**: Content should naturally invite likes, retweets, or replies
2. **Avoid Negative Feedback**: Never create content that might trigger blocks, mutes, or reports
3. **Optimize Dwell Time**: Make content worth reading and re-reading
4. **Leverage Multimedia**: Videos and images have dedicated probability scores

### Writing Best Practices

**Hook Formula** (First Line Critical):
- Lead with the most compelling insight
- Use pattern interrupts: questions, bold claims, surprising facts
- Create curiosity gaps that require reading further

**Structure Patterns**:
- **Thread Format**: Break complex ideas into 3-7 connected posts
- **List Format**: "5 ways to..." or "3 reasons why..."
- **Story Format**: Problem → Insight → Solution
- **Controversial Take**: Strong opinion + supporting evidence

**Engagement Triggers**:
- Ask questions that invite replies
- Include "Reply with..." prompts
- Create shareable insights (quotable)
- Use save-worthy information (reference material)

**Multimedia Strategy**:
- Images: Use high-quality visuals, infographics, screenshots
- Videos: Short (<60s) with captions, hook in first 3 seconds
- Threads: Include visual breaks every 2-3 posts

### Content Types That Perform Well

1. **Educational**: How-to guides, tips, frameworks
2. **Controversial**: Well-reasoned contrarian views
3. **Inspirational**: Success stories, motivational insights
4. **Entertaining**: Humor, relatable observations
5. **News/Commentary**: Timely reactions with unique angles
6. **Resource**: Tools, links, recommendations (high save rate)

## Post Writing Workflow

### Step 1: Understand Intent & Language
Clarify the goal and translate if needed:
- **Identify Goal**: Brand awareness? Thought leadership? Product promotion? Community engagement?
- **Language Processing**: If user provides content in non-English language, translate to English while maintaining core message
- **Cultural Adaptation**: Adjust idioms, references, and tone for English-speaking Twitter audience

### Step 2: Choose Format
Select based on message complexity:
- **Single Post**: Simple insight, <280 characters (best for max reach)
- **Thread (3-5 tweets)**: Deep insights requiring multiple parts
- **Media Post**: Visual-first content with brief caption (consider using image generation)

**Thread Strategy Note**: Algorithm penalizes same-author repetition (Author Diversity Scorer). Keep threads short (3-5 tweets) and make each tweet independently valuable. First tweet performance determines entire thread visibility. See [references/thread-strategy.md](references/thread-strategy.md) for details.

### Step 3: Assess Visual Needs
Determine if an image would boost engagement:
- **Statistics/Data**: Charts, infographics strongly recommended
- **Product Announcements**: Product visuals highly effective
- **Educational Content**: Visual diagrams increase retention
- **News/Commentary**: Context images can boost clicks

If visual would help, use: `scripts/generate_twitter_image.py`

### Step 4: Draft Content (English Only)

**Single Post Template**:
```
[Hook - strong first line]

[Body - 2-3 lines of value]

[CTA - question or action prompt]
```

**Thread Template**:
```
1/ [Hook tweet - sets up the thread topic]

2/ [Context - why this matters]

3-5/ [Main content - insights, steps, or arguments]

N/ [Conclusion - summary + CTA]
```

### Step 5: Optimize for Algorithm

**Pre-publish Checklist**:
- ✅ **Language**: Written entirely in English
- ✅ **Hook**: First line grabs attention immediately
- ✅ **Engagement**: Invites at least one interaction type (like/reply/retweet)
- ✅ **Tone**: No elements that might trigger negative feedback
- ✅ **Visual**: Includes image if appropriate (use Gemini for generation)
- ✅ **Length**: Optimized (single: 100-280 chars, threads: 3-7 posts)
- ✅ **Quality**: Typo-free and professionally formatted
- ✅ **Translation**: If source was non-English, verify natural English phrasing

### Step 6: Timing Considerations
While not strictly algorithm-based, consider:
- Post when target audience is active
- Space out posts (avoid flooding)
- Consistency matters more than frequency

## Image Generation for Twitter

### When to Generate Images

Visual content significantly boosts engagement rates on Twitter. Generate images for:

1. **Data & Statistics**: Charts, graphs, infographics
2. **Product Announcements**: Screenshots, mockups, feature highlights
3. **Educational Threads**: Visual diagrams, flowcharts, concept illustrations
4. **News Commentary**: Context visuals, comparison graphics
5. **Quotes & Insights**: Text-on-image for shareable quotes

### Using the Image Generator

**Basic Usage**:
```bash
python3 scripts/generate_twitter_image.py "Modern infographic showing AI adoption trends in 2026"
```

**With Options**:
```bash
# Square format (1:1) for profile-optimized posts
python3 scripts/generate_twitter_image.py "Product feature comparison table" --aspect-ratio 1:1

# Standard format (4:3) for traditional composition
python3 scripts/generate_twitter_image.py "Data visualization chart" --aspect-ratio 4:3

# Custom output path
python3 scripts/generate_twitter_image.py "Team milestone celebration graphic" --output milestone.png
```

### Image Prompt Best Practices

**Good Prompts** (specific, descriptive):
- ✅ "Clean infographic showing 3-step process with icons, modern gradient background, professional design"
- ✅ "Product screenshot mockup on laptop screen, minimalist desk setup, natural lighting"
- ✅ "Data visualization comparing before/after metrics, bar chart style, corporate blue color scheme"

**Poor Prompts** (vague, ambiguous):
- ❌ "Nice image"
- ❌ "Something cool"
- ❌ "Picture for my tweet"

### Technical Specifications

- **API**: Gemini 3 Pro Image
- **Default Aspect Ratio**: 16:9 (optimal for Twitter timeline)
- **Quality**: 4K (high resolution for clarity)
- **Format**: PNG (transparent background support)
- **Generation Time**: 30-90 seconds

## Common Pitfalls to Avoid

❌ **Algorithm Killers**:
- Engagement baiting ("RT if you agree")
- Misleading clickbait
- Excessive hashtags (looks spammy)
- Overly promotional content
- Controversial without substance (triggers reports)
- Generic/bland observations

❌ **Negative Feedback Triggers**:
- Political extremism
- Harassment or attacks
- Misinformation
- Spam-like behavior
- Irrelevant tagging

## Examples

### Example 1: Educational Thread

```
1/ The biggest mistake in marketing? Treating attention like it's free.

Attention is the scarcest resource in 2026. Here's how to respect it:

2/ Most brands dump information. They explain every feature, every benefit, every reason.

But attention doesn't scale with information. It shrinks.

3/ Instead, use the "One Thing" rule:

Every piece of content should communicate ONE core insight. Not three. Not five. One.

4/ Why this works:

• Easier to remember
• Simpler to share
• Faster to consume
• Harder to misunderstand

5/ Example: Apple never lists 47 features. They show you ONE thing you couldn't do before.

The iPhone reveal? "This is your phone, iPod, and internet device. In one."

6/ Your action step:

Before publishing, ask: "What's the ONE thing I want them to remember?"

If you can't answer, you're not ready to publish.

7/ That's it. One insight. Respect attention, and it respects you back.

What's YOUR "one thing" this week? Reply below 👇
```

**Why this works**:
- Strong hook (mistake + promise)
- Each tweet delivers value
- Builds to actionable conclusion
- Ends with reply prompt
- High quote-tweet potential
- Educational (save-worthy)

### Example 2: Single Insight Post

```
The best marketing strategy?

Make people feel smart for choosing you.

Not "we're the best"—but "you're smart for seeing what others missed."

Positioning isn't about you. It's about them.
```

**Why this works**:
- Pattern interrupt opening
- Counter-intuitive insight
- Quotable format
- Fits in one read (high dwell time)
- Invites agreement (likes)

### Example 3: Visual + Commentary

```
This chart shows why most startups fail.

[Attach: Graph showing revenue expectations vs reality]

The gap between "we'll be profitable in 6 months" and reality is where dreams die.

Plan for 3x longer and 2x more expensive. Always.
```

**Why this works**:
- Visual element (high engagement)
- Clear takeaway
- Specific advice (actionable)
- Shareable insight

## Advanced Techniques

### Reply Strategy
Engaging in your own replies can:
- Extend thread visibility
- Add context without main post clutter
- Create conversation that boosts all signals

### Cross-Format Optimization
- Long-form content → Thread
- Visual data → Image post with takeaway
- Video content → Short clip with hook caption
- External link → Quote + insight (not just link)

### A/B Testing Concepts
- Test different hooks for same core message
- Experiment with thread length (3 vs 5 vs 7 posts)
- Try different media types
- Vary CTA styles (question vs action vs none)

## References

For detailed mechanics and additional guidance:
- [references/algorithm-deep-dive.md](references/algorithm-deep-dive.md) - Technical ranking system details
- [references/content-examples.md](references/content-examples.md) - Post examples by category
- [references/thread-strategy.md](references/thread-strategy.md) - Thread optimization and algorithm analysis

## Quick Reference

**Post Length**:
- Optimal: 100-280 characters (full tweet)
- Threads: 3-7 tweets maximum
- First tweet: Most critical, strongest hook

**Engagement Formula**:
Value + Clarity + CTA = High engagement

**Red Flags**:
- "RT if...", "Like if..." (engagement bait)
- All caps, excessive punctuation
- Too many hashtags (>3)
- Link dumps without context

---

**Write with intention. Optimize for value. Let the algorithm amplify.**
