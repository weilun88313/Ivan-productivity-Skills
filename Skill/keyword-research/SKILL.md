---
name: keyword-research
description: Discovers high-value keywords with search intent analysis and content opportunity mapping. Essential for starting any SEO or GEO content strategy.
---

# Keyword Research

Brainstorm, classify, and prioritize keywords for SEO and GEO content strategies.

**🔥 Powered by Ahrefs**: This skill uses the Ahrefs MCP to get real keyword data (search volume, difficulty, traffic potential) instead of estimates.

## Instructions

### 1. Gather Context

If not already provided, ask the user:
- Topic / product / service
- Target audience
- Business goal (traffic, leads, sales)
- Content language

### 2. Generate Seed Keywords

Brainstorm keywords across these angles:
- **Core terms**: Direct product/service descriptors
- **Problem keywords**: What pain points does the audience search for?
- **Solution keywords**: How does the product/service solve those pains?
- **Comparison keywords**: "[product] vs [alternative]", "best [category]"
- **Question keywords**: "how to...", "what is...", "why..."

Expand each seed with modifiers: `best`, `top`, `how to`, `[year]`, `for [audience]`, `vs [alternative]`, `guide`, `examples`.

### 3. Classify Search Intent

| Intent | Signals | Content Type |
|--------|---------|--------------|
| Informational | what, how, why, guide | Blog posts, guides |
| Commercial | best, review, vs, compare | Comparison posts |
| Transactional | buy, price, pricing, signup | Product/pricing pages |

### 4. Get Keyword Metrics from Ahrefs

**CRITICAL: Use Ahrefs MCP tools to get real data:**

For each promising keyword, query Ahrefs to get:
- **Search Volume**: Monthly search volume
- **Keyword Difficulty (KD)**: 0-100 score (lower = easier to rank)
- **Traffic Potential**: Estimated traffic if you rank #1
- **SERP Overview**: Current ranking pages and their metrics

**Interpreting KD scores:**
- **0-30**: Low difficulty - good for new/small sites
- **31-60**: Medium difficulty - need quality content + some backlinks
- **61-100**: High difficulty - very competitive, need strong domain authority

**If Ahrefs MCP is not available**, assess difficulty qualitatively based on topic knowledge and manually check SERPs.

### 5. Identify GEO Opportunities

Flag keywords likely to trigger AI-generated answers:
- Question formats: "What is...", "How does..."
- Definition queries, comparison queries, list queries
- How-to queries with clear step-by-step answers

### 6. Group into Topic Clusters

Organize keywords into 2-4 clusters, each with:
- **Pillar topic**: Broad, high-volume keyword
- **Cluster articles**: 3-5 specific subtopics that link back to the pillar

### 7. Output Format

```markdown
# Keyword Research: [Topic]

**Date**: [date]
**Audience**: [audience]
**Goal**: [goal]

## Recommended Article Topics (Priority Order)

| # | Article Topic | Target Keyword | Volume | KD | Intent | GEO Potential |
|---|--------------|----------------|--------|-------|--------|---------------|
| 1 | [title idea] | [keyword] | [monthly searches] | [0-100] | [type] | Yes/No |
| 2 | ... | ... | ... | ... | ... | ... |

## Topic Clusters

### Cluster: [Theme]
- Pillar: [keyword]
- Supporting: [keyword 1], [keyword 2], [keyword 3]

## Full Keyword List

| Keyword | Volume | KD | Intent | Traffic Potential | Notes |
|---------|--------|-----|--------|------------------|-------|
| ... | ... | ... | ... | ... | ... |
```

Focus the output on **actionable article recommendations** — the user's next step is picking a topic to write.

## Related Skills

- [blog-writer](../blog-writer/) — Write the article
- [brand-guidelines](../brand-guidelines/) — Product info for Lensmor content
- [webflow-blog-publisher](../webflow-blog-publisher/) — Publish to Webflow
- [content-pipeline](../content-pipeline/) — Run the full workflow end-to-end
