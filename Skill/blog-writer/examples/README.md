# professional blog Blog Writer Examples

This directory contains example blog posts demonstrating the professional blog writing style and structure.

## Files

### `sample-blog-post.md`

**Topic**: Email Marketing Best Practices

**Type**: Listicle (10-point guide)

**Demonstrates**:
- ✅ Complete metadata block (title, slug, meta description, cover image)
- ✅ Hook-based introduction (problem → promise → definition)
- ✅ "Why" section with data points
- ✅ Numbered list format with H2 headers
- ✅ "Why this works" explanations
- ✅ Pro Tips throughout (minimum 3)
- ✅ Image placeholders with descriptions
- ✅ Clear CTA in conclusion
- ✅ Short paragraphs (3-4 lines max)
- ✅ Scannable formatting with bold and bullets

**Key Metrics**:
- **Word Count**: ~2,400 words
- **Read Time**: ~12 minutes
- **Pro Tips**: 10
- **Image Placeholders**: 6
- **SEO**: Keyword-optimized for "email marketing best practices"

## Using These Examples

### For Learning

Study the structure and tone:
```bash
# Read the example
cat sample-blog-post.md

# Note the sections:
# 1. Metadata block
# 2. Hook introduction
# 3. "What is" definition
# 4. "Why it matters"
# 5. Numbered list of practices
# 6. Action-oriented conclusion
```

### For Templates

Copy and adapt:
```bash
# Copy as starting point
cp examples/sample-blog-post.md workspace/my-new-post.md

# Modify for your topic
# - Update metadata (title, slug, meta)
# - Rewrite intro with your hook
# - Replace numbered items
# - Update image placeholders
# - Adjust Pro Tips
```

### For Testing

Test the publishing workflow:
```bash
# 1. Copy example
cp examples/sample-blog-post.md workspace/test-post.md

# 2. Generate placeholder images
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Abstract email marketing visualization" \
  --output_dir workspace/images

# 3. Update image paths in markdown
# Edit workspace/test-post.md to point to generated images

# 4. Publish to Webflow (if configured)
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/test-post.md \
  --category strategy
```

## Content Analysis

### Tone & Voice

```markdown
✅ Professional yet accessible
   "We know that standing out in a crowded inbox can feel like..."

✅ Empathetic
   "Despite the rise of social media and messaging apps..."

✅ Action-oriented
   "Here's how to do it: Use double opt-in to confirm..."

✅ Confident
   "A list of 1,000 engaged subscribers will outperform 10,000..."
```

### Structure Pattern

```
Introduction (Problem-Promise-Definition)
    ↓
Why It Matters (Benefits + Data)
    ↓
Main Content (Numbered List or Steps)
│
├─ Item 1: [Descriptive Title]
│  ├─ Why this works
│  ├─ How to do it
│  ├─ Pro Tip
│  └─ Image
│
├─ Item 2: [Descriptive Title]
│  └─ ...
│
└─ Item N: [Descriptive Title]
    ↓
Conclusion (Summary + Action Plan + CTA)
```

### SEO Elements

| Element | Example | Purpose |
|---------|---------|---------|
| **Title** | "10 Email Marketing Best Practices to 3x Your ROI in 2026" | Includes number, keyword, benefit, year |
| **Slug** | `/blog/strategy/email-marketing-best-practices-2026` | Keyword-rich, readable URL |
| **Meta** | "Learn 10 proven email marketing strategies that top brands use..." | 155 chars, keyword + benefit |
| **H2 Headers** | "Build a Quality Email List", "Segment Your Audience" | Keyword variations, descriptive |
| **Alt Text** | Images describe content (for accessibility & SEO) | "Email list building funnel diagram" |

### Formatting Best Practices

**Paragraphs**:
- Max 3-4 lines
- One idea per paragraph
- Mix short and medium lengths

**Lists**:
- Bullets for non-sequential items
- Numbers for steps or rankings
- Bold the first few words of each item

**Emphasis**:
- **Bold** for key concepts
- *Italic* for quotes or emphasis (sparingly)
- `Code blocks` for technical terms or examples

**Pro Tips**:
```markdown
**Pro Tip**: [Actionable insider advice]
```
- Minimum 3 per article
- Placed after explaining a concept
- Specific, actionable advice

## Image Prompts Used

These are example prompts for generating the images:

### Cover Image
```
Abstract email marketing visualization with flowing data connections,
interconnected network nodes, email envelopes transforming into engagement
metrics, Linear dark mode aesthetic, deep charcoal background, violet-blue
accent colors (#6B75FF), minimalist modern design, high-tech visualization
```

### Inline Images

**List Building Diagram**:
```
Email list building funnel diagram, stages from lead magnet to signup to
confirmation, clean flow chart, dark mode interface, Linear style, sharp
lines, violet connectors, professional business visualization
```

**Segmentation Visualization**:
```
Audience segmentation visualization, multiple customer groups represented
as distinct clusters, data points grouped by behavior, clean infographic
style, dark background, colored segments, Linear aesthetic
```

**Personalization Dashboard**:
```
Personalized email dashboard interface, dynamic content blocks highlighted,
user profile data feeding into email template, wireframe mockup, dark mode
UI, violet accent highlights, professional SaaS interface design
```

**Timing Heatmap**:
```
Email timing heatmap visualization, week view with hours and days, color
gradient showing optimal send times, data visualization, dark grid
background, violet-to-blue color scale, clean analytical design
```

**Analytics Dashboard**:
```
Email analytics dashboard showing key performance metrics, open rate
graphs, click-through rate charts, conversion funnel, clean data
visualization, dark mode interface, professional metrics display
```

**Deliverability Checklist**:
```
Email deliverability checklist visualization, authentication setup steps,
SPF DKIM DMARC configuration diagram, technical workflow, dark mode,
clean system architecture illustration
```

## Creating Your Own Examples

To add new examples to this directory:

1. **Write following the structure**:
   - Start with metadata block
   - Follow Hook → Why → How → CTA
   - Include Pro Tips
   - Add image placeholders

2. **Name descriptively**:
   - `[topic]-[type].md`
   - Example: `seo-guide-howto.md`, `content-calendar-listicle.md`

3. **Document in this README**:
   - Add to Files section
   - Note what it demonstrates
   - Include key metrics

4. **Test the workflow**:
   - Generate images
   - Verify publishing (if possible)
   - Note any issues or improvements

## Resources

- [Main README](../README.md) - Complete user guide
- [SKILL.md](../SKILL.md) - AI writing instructions
- [Visual Style Guide](../references/visual-style-guide.md) - Image generation guidelines
- [Blog Workflow](../../BLOG_WORKFLOW.md) - End-to-end publishing process

---

**Need more examples?** Check the main README for prompt examples and content type templates.
