[English](README.md) | [中文](README.zh.md)

---


# Lensmor Brand Guidelines Skill

A comprehensive brand guidelines skill for Lensmor that provides brand context, visual design rules, writing style guidelines, and product information to ensure brand consistency across all content and communications.

## What This Skill Does

This skill teaches Claude about Lensmor's brand identity, including:

- **Product positioning and value proposition** - Core messaging about what Lensmor does and who it's for
- **Visual design system** - Colors, typography, logo usage, and visual elements
- **Writing style and tone** - Brand voice, content templates, and messaging guidelines
- **Competitive positioning** - How to position Lensmor against competitors
- **Standard responses** - Pre-approved answers to common questions

## When to Use This Skill

Use this skill whenever you're:
- Creating marketing materials or product documentation
- Writing feature announcements or user communications
- Designing visual assets or UI components
- Responding to customer questions or support inquiries
- Developing content that needs to maintain brand consistency

## How to Use This Skill

1. **Activate the skill** by mentioning it in your request:
   - "Using the brand guidelines skill, create a feature announcement for..."
   - "Help me write a product description following Lensmor's brand guidelines"

2. **The skill will automatically**:
   - Apply brand voice and tone to all written content
   - Use correct terminology and product naming
   - Follow visual design specifications
   - Maintain consistency with established brand standards

## Customizing This Skill

This skill comes with template files that need to be filled with your actual brand information:

### Core Files

- **`SKILL.md`** - Main skill instructions and guidelines
  - Product overview and positioning
  - Visual design specifications (colors, typography, logo)
  - Writing style and tone guidelines
  - Content templates and examples

### Resource Files (in `resources/` directory)

- **`product-details.md`** - Detailed product specifications, features, and personas
- **`visual-assets.md`** - Complete design system with colors, fonts, spacing, and assets
- **`competitor-comparison.md`** - Competitive positioning and battle cards
- **`faq-responses.md`** - Standard responses to common questions

### Filling in Your Brand Information

Look for `[TODO: ...]` markers throughout the files and replace them with your actual brand information:

1. **Start with `SKILL.md`**:
   - Add product description and core features
   - Define your color palette (hex codes)
   - Specify typography (font families and usage)
   - Document your brand voice attributes
   - Add writing examples (good vs. avoid)

2. **Fill in `resources/product-details.md`**:
   - Detailed feature descriptions
   - User personas
   - Technical specifications
   - Pricing information

3. **Complete `resources/visual-assets.md`**:
   - Add paths to logo files
   - Define complete color system with CSS variables
   - Document spacing, borders, shadows
   - Link to design templates

4. **Update `resources/competitor-comparison.md`**:
   - List main competitors
   - Define key differentiators
   - Add positioning statements
   - Create objection handling responses

5. **Customize `resources/faq-responses.md`**:
   - Fill in actual FAQ responses
   - Adjust questions to match common customer inquiries
   - Add product-specific information

## File Structure

```
brand-guidelines/
├── README.md                           # This file
├── SKILL.md                           # Main skill instructions
└── resources/
    ├── product-details.md             # Product specs and features
    ├── visual-assets.md               # Design system documentation
    ├── competitor-comparison.md       # Competitive positioning
    └── faq-responses.md              # Standard FAQ responses
```

## Tips for Effective Brand Guidelines

1. **Be Specific**: Vague guidelines lead to inconsistent results. Provide concrete examples.

2. **Show, Don't Just Tell**: Include both good and bad examples to illustrate your points.

3. **Keep It Updated**: Review and update brand guidelines regularly as your brand evolves.

4. **Include Context**: Explain *why* certain choices were made, not just *what* they are.

5. **Make It Practical**: Focus on guidelines that will actually be used day-to-day.

## Using This Skill in Claude Code

After customizing the files:

1. Ensure this skill is in your Claude Code skills directory
2. The skill will be automatically available when marketplace is configured
3. Reference it naturally: "Use the brand guidelines to write..."

## Using This Skill in Claude.ai

1. Upload the `brand-guidelines` folder to Claude.ai
2. Claude will load the skill and apply it to your conversations
3. The skill remains active throughout your conversation

## Maintenance

**Regular Reviews:**
- Review brand guidelines quarterly
- Update after major product releases
- Refresh competitor information regularly
- Add new FAQ responses as they emerge

**Version Control:**
- Track changes to brand guidelines over time
- Document major brand updates
- Maintain changelog for significant revisions

## Questions or Issues?

If you need help customizing this skill or have questions about best practices for brand guidelines, refer to:
- [Creating Custom Skills Documentation](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Agent Skills Specification](../../spec/)

---

**Note:** This skill template is designed to be comprehensive. Feel free to remove sections that don't apply to your brand or add additional sections that are important for your specific use case.
