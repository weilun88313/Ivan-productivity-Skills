---
name: keyword-research
description: Discovers high-value keywords with search intent analysis and content opportunity mapping. Essential for starting any SEO or GEO content strategy.
---

# Keyword Research

Brainstorm, classify, and prioritize keywords for SEO and GEO content strategies.

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

### 4. Assess Competition (Qualitative)

Without SEO tool data, assess difficulty qualitatively:
- **Low**: Long-tail, niche topics, few quality articles ranking
- **Medium**: Some competition, opportunities for better content
- **High**: Dominated by major brands and high-authority sites

Be honest: without tools like Ahrefs/SEMrush, these are estimates based on topic knowledge.

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

| # | Article Topic | Target Keyword | Intent | Competition | GEO Potential |
|---|--------------|----------------|--------|-------------|---------------|
| 1 | [title idea] | [keyword] | [type] | Low/Med/High | Yes/No |
| 2 | ... | ... | ... | ... | ... |

## Topic Clusters

### Cluster: [Theme]
- Pillar: [keyword]
- Supporting: [keyword 1], [keyword 2], [keyword 3]

## Full Keyword List

| Keyword | Intent | Competition | Notes |
|---------|--------|-------------|-------|
| ... | ... | ... | ... |
```

Focus the output on **actionable article recommendations** — the user's next step is picking a topic to write.

## Related Skills

- [blog-writer](../blog-writer/) — Write the article
- [brand-guidelines](../brand-guidelines/) — Product info for Lensmor content
- [webflow-blog-publisher](../webflow-blog-publisher/) — Publish to Webflow
- [content-pipeline](../content-pipeline/) — Run the full workflow end-to-end
