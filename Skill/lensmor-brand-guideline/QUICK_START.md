# Quick Start Guide - Lensmor Brand Guidelines

## 5-Minute Setup

Follow these steps to get your Lensmor brand guidelines skill ready to use:

### Step 1: Product Basics (2 minutes)

Open `SKILL.md` and fill in:

1. **Product description** (line ~28):
   ```markdown
   [TODO: Add a 2-3 sentence elevator pitch describing what Lensmor does and who it's for]
   ```
   Replace with your actual product description.

2. **Key features** (line ~34):
   ```markdown
   **Key Features:**
   [TODO: List 3-5 core features or capabilities]
   - Feature 1
   - Feature 2
   - Feature 3
   ```
   List your top 3-5 features.

### Step 2: Brand Colors (1 minute)

Find the "Brand Colors" section (line ~54) and add your hex codes:

```markdown
**Primary Colors:**
[TODO: Add hex codes and usage guidelines]
- Primary: `#______` - Used for [describe usage]
- Secondary: `#______` - Used for [describe usage]
```

Example:
```markdown
- Primary: `#007AFF` - Used for CTAs, links, and primary actions
- Secondary: `#34C759` - Used for success states and highlights
```

### Step 3: Brand Voice (1 minute)

Define your tone attributes (line ~149):

```markdown
**Tone Attributes:**
[TODO: Define 3-5 key tone attributes]
- [Attribute 1]: [Description and example]
```

Example:
```markdown
**Tone Attributes:**
- Professional yet approachable: We're experts, but we explain things clearly without jargon
- Empowering: We help users feel confident and capable
- Efficient: We respect users' time with concise, actionable information
```

### Step 4: Test It Out (1 minute)

Try using the skill:

```
Using the Lensmor brand guidelines, write a short product description
for our homepage.
```

Claude should apply the brand voice and information you've provided!

## What to Fill In Next

After the quick start, prioritize these sections:

### High Priority (Next 30 minutes)

1. **Writing Examples** in `SKILL.md`:
   - Add "good" and "avoid" examples for your brand
   - Include actual product copy

2. **Product Details** in `resources/product-details.md`:
   - Fill in detailed feature descriptions
   - Define user personas

3. **FAQ Responses** in `resources/faq-responses.md`:
   - Write actual responses to common questions
   - Customize questions for your product

### Medium Priority (Next hour)

4. **Visual Assets** in `resources/visual-assets.md`:
   - Complete color palette with all shades
   - Add typography specifications
   - Document spacing and component specs

5. **Competitor Positioning** in `resources/competitor-comparison.md`:
   - List main competitors
   - Define key differentiators
   - Add positioning statements

### Low Priority (When you have time)

6. **Advanced Guidelines**:
   - Detailed logo usage rules
   - Photography/illustration guidelines
   - Animation/motion principles
   - Accessibility standards

## Common Mistakes to Avoid

❌ **Too Vague**: "Our tone is friendly and professional"
✅ **Specific**: "We use contractions (we're, you're) to sound approachable, but avoid slang"

❌ **Just Listing**: "Colors: Blue, Green, Gray"
✅ **With Context**: "Primary Blue (#007AFF) for CTAs and links to drive action"

❌ **No Examples**: "Write in active voice"
✅ **With Examples**:
- Good: "Create your first project in minutes"
- Avoid: "Your first project can be created in minutes"

## Testing Your Brand Guidelines

Use these prompts to test your brand guidelines:

1. **Product Description Test**:
   ```
   Using the brand guidelines, write a 50-word product description for Lensmor.
   ```

2. **Feature Announcement Test**:
   ```
   Using the brand guidelines, announce our new [feature name] feature.
   ```

3. **Support Response Test**:
   ```
   Using the brand guidelines, respond to a user asking: "How does Lensmor work?"
   ```

4. **Competitor Comparison Test**:
   ```
   Using the brand guidelines, explain how Lensmor differs from [competitor name].
   ```

## Verification Checklist

Before considering your brand guidelines complete, verify:

- [ ] Product description is clear and compelling
- [ ] At least 3 key features are documented
- [ ] Primary brand colors are defined with hex codes
- [ ] Brand voice has 3+ specific attributes with examples
- [ ] At least 3 "good vs. avoid" writing examples are included
- [ ] Product name capitalization is specified
- [ ] Typography (font families) is documented
- [ ] At least 5 FAQ responses are filled in
- [ ] You've tested the skill and it produces brand-consistent content

## Getting Help

**If Claude isn't following your guidelines:**
- Check that you removed all `[TODO: ...]` markers
- Make guidelines more specific with concrete examples
- Add more "good vs. avoid" examples
- Test with simpler requests first

**If you're unsure what to include:**
- Look at your existing marketing materials
- Review your company's style guide (if you have one)
- Check competitor brand guidelines for inspiration
- Start simple and add detail over time

## Quick Reference: File Locations

- Main skill instructions: `SKILL.md`
- Product details: `resources/product-details.md`
- Design system: `resources/visual-assets.md`
- Competitor info: `resources/competitor-comparison.md`
- FAQ responses: `resources/faq-responses.md`

---

**Next Step:** Open `SKILL.md` and start filling in the `[TODO: ...]` sections!
