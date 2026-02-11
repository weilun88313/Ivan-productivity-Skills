---
name: linkedin-post-writer
description: "Transform fragmented ideas or topics into engaging LinkedIn posts with accompanying images. Use this skill when the user wants to: (1) Convert scattered thoughts into a polished LinkedIn post, (2) Develop a topic into a full post with specific ideas and narrative, (3) Generate professional images for LinkedIn posts using Gemini API, (4) Create posts that align with a personal brand (approachable, AI/tech/product/entrepreneurship focused, 300-800 character medium-length posts). This skill helps maintain consistent voice, structure, and visual style across all LinkedIn content."
---

# LinkedIn Post Writer

Transform fragmented ideas into engaging LinkedIn posts with compelling visuals that match your personal brand.

## Overview

This skill helps you create LinkedIn posts in two primary scenarios:
1. **From Fragments to Post**: Convert scattered thoughts and bullet points into polished, engaging posts
2. **From Topic to Post**: Expand a general topic into specific ideas with a complete narrative

**CRITICAL Requirements**:
- All posts must be in **English**
- Images must be **16:9 aspect ratio**, **2K quality**
- Output directory: `/Users/ivan/Documents/Ivan_Skills/workspace`
- **Markdown output**: Only include post content, NO hashtags, NO metadata, NO file info
- Posts follow a consistent brand voice (approachable and friendly)
- AI-generated images reinforce the message

## Core Workflow

### Step 1: Understand the Input

Identify which scenario applies:

**Scenario A: User provides fragmented ideas**
- Bullet points or scattered thoughts
- Partial observations or experiences
- Rough notes or concepts

**Scenario B: User provides a topic/theme**
- General subject area (e.g., "product thinking", "AI in business")
- Broad concept without specific angle
- Request to "write about X"

### Step 2: Content Development

#### For Fragmented Ideas (Scenario A)

1. **Capture & Organize**
   - List all provided ideas
   - Group related thoughts together
   - Identify the central message

2. **Choose Structure**
   - Review templates in `references/post_templates.md`
   - Select structure that best fits the content type:
     - Personal Story → Insight
     - Observation → Analysis
     - Question → Exploration
     - Tip List → Value Delivery
     - Contrarian View → Debate

3. **Develop Post**
   - Expand ideas into coherent narrative
   - Add personal voice and examples
   - Ensure 300-800 character length
   - Follow brand guidelines in `references/brand_persona.md`

4. **Refine**
   - Check tone is conversational and approachable
   - Verify clear hook and engaging closing
   - Add appropriate emojis (1-3)
   - Include relevant hashtags (3-5)

#### For Topic Development (Scenario B)

1. **Explore the Topic**
   - If needed, ask clarifying questions:
     - What angle interests you most?
     - Any specific experience or example?
     - What should readers take away?
   - Identify personal connection or observation

2. **Find the Angle**
   - Connect topic to personal experience
   - Identify unique perspective or insight
   - Determine what makes this relevant to audience

3. **Build Content**
   - Create compelling hook (see templates)
   - Develop 2-3 key points with supporting details
   - Include examples or anecdotes
   - Balance insight with accessibility

4. **Add Engagement**
   - End with question or call to action
   - Invite discussion or sharing
   - Make it feel like starting a conversation

### Step 3: Generate Image

1. **Extract Visual Concept**
   - Identify the core message or metaphor
   - Determine appropriate image style:
     - Concept illustration (abstract ideas)
     - Data visualization (numbers/trends)
     - Scene composition (scenarios)
     - Icon-based (simple concepts)

2. **Create Image Prompt**
   - Use enhancement techniques from `scripts/generate_image.py`
   - Follow image guidelines in `references/brand_persona.md`:
     - Clean, modern, professional aesthetic
     - Vibrant but professional colors (blues, teals, oranges)
     - Minimal text overlay
     - Suitable for business social media
   - **CRITICAL**: Always include "high resolution, 2K quality, professional photography quality" in prompts

3. **Generate Image**
   - **Default Settings**:
     - Aspect Ratio: **16:9** (optimized for LinkedIn)
     - Output Directory: `/Users/ivan/Documents/Ivan_Skills/workspace`
     - Quality: 2K, high resolution

   - Run the image generation script:
     ```bash
     python scripts/generate_image.py --prompt "YOUR_PROMPT" \
       --enhance \
       --output_dir /Users/ivan/Documents/Ivan_Skills/workspace \
       --filename linkedin_post \
       --aspect-ratio 16:9
     ```
   - Or call the script with the post content to auto-enhance:
     ```bash
     python scripts/generate_image.py --prompt "POST_CONTENT" \
       --enhance \
       --style "modern, professional, tech-focused, high resolution, 2K quality" \
       --aspect-ratio 16:9 \
       --output_dir /Users/ivan/Documents/Ivan_Skills/workspace
     ```

4. **Review Image**
   - Ensure image aligns with message
   - Check visual quality and professionalism (2K quality)
   - Verify it matches brand aesthetic
   - Confirm 16:9 aspect ratio

### Step 4: Final Review & Output

Use the quality checklist from `references/brand_persona.md`:

- [ ] Tone is conversational and approachable
- [ ] Contains personal insight or experience
- [ ] Provides clear value or takeaway
- [ ] Length is 300-800 characters
- [ ] Opening hooks the reader
- [ ] Closing invites engagement (question or call to action)
- [ ] Language is accessible and relatable
- [ ] Image aligns with message and brand aesthetic
- [ ] Overall feel is authentic and genuine

**Output Format**:
- Save post content as `.md` file in `/Users/ivan/Documents/Ivan_Skills/workspace`
- **Include ONLY**: Post text content (with emojis if used)
- **Exclude**: Hashtags, image metadata, post metrics, generated timestamp
- Markdown file should be clean and copy-paste ready for LinkedIn

## Quick Reference

### Post Structure Patterns

See `references/post_templates.md` for detailed templates. Common patterns:

1. **Personal Story → Insight**: Share experience, extract lesson
2. **Observation → Analysis**: Notice pattern, provide interpretation
3. **Question → Exploration**: Pose question, explore perspectives
4. **Tip List → Value**: Share actionable advice with context
5. **Contrarian View → Debate**: Challenge assumption, invite discussion

### Tone Guidelines

**Do**:
- Use conversational language ("I recently discovered...", "Here's the thing...")
- Share personal experiences and observations
- Be authentic and show vulnerability
- Invite engagement with questions
- Use everyday language mixed with professional terms

**Don't**:
- Use overly formal or academic language
- Write purely promotional content
- Use excessive jargon without explanation
- Present only theory without practical application
- Write in a negative tone without constructive insight

### Image Generation

For image generation, the skill uses Gemini API through `scripts/generate_image.py`.

**Basic usage**:
```bash
python scripts/generate_image.py "your image description" -o output.png
```

**With LinkedIn enhancement**:
```bash
python scripts/generate_image.py "your post content" --enhance --style "professional, tech-focused"
```

**Environment setup**:
Set `GEMINI_API_KEY` environment variable or use `--api-key` flag.

## Resources

### References

- **`references/brand_persona.md`**: Complete brand voice, writing style, content themes, and quality standards
- **`references/post_templates.md`**: Detailed post structures, templates, examples, and engagement optimization techniques

### Scripts

- **`scripts/generate_image.py`**: Generate images using Gemini API with LinkedIn-specific enhancements

Load these references when you need:
- Detailed guidance on writing style and tone
- Specific post structure templates and examples
- Image generation patterns and prompts
- Quality assessment criteria
- Hashtag strategies and engagement techniques

## Examples

### Example 1: From Fragments to Post

**Input**:
```
- AI changes product design workflow
- Useful for brainstorming
- Can also analyze user interviews
- But can't completely rely on it
```

**Process**:
1. Core message: Practical AI use in product design
2. Template: Tip List → Value Delivery
3. Add personal context and examples
4. Create conversational flow
5. Generate relevant image

**Output**:
```
After using AI for product design for 6 months, here are my 3 most practical use cases:

1. Brainstorming phase
Not asking AI for answers, but letting it help you ask the right questions

2. User research analysis
Feed interview transcripts to AI, quickly identify common insights

3. Documentation writing
Generate framework quickly, then refine details manually

Key takeaway: AI isn't a replacement, it's an accelerator ✨

How are you using AI in your work? Any unique use cases?

#ProductDesign #AIApplications #ProductThinking
```

### Example 2: From Topic to Post

**Input**: "I want to write a post about team collaboration"

**Process**:
1. Explore: Ask what aspect of collaboration interests them
2. Find angle: Recent experience or observation
3. Choose structure: Personal Story → Insight
4. Develop narrative with specific example
5. Create image showing team/collaboration concept

**Output**:
```
An intern asked me a question last week that stopped the entire room.

"Why are we spending 3 weeks perfecting a feature only 2% of users will touch?"

That moment made me realize:
• We often chase perfection at the cost of priority
• Sometimes outside perspective beats internal experience
• Courage doesn't come from seniority—it comes from authenticity

The best teams aren't the ones where everyone says "yes."

They're the ones where people feel safe asking "why."

Ever had a moment like this on your team? 💭

#TeamManagement #ProductThinking #Entrepreneurship
```

## Notes

- Always consult `references/brand_persona.md` for voice consistency
- Use `references/post_templates.md` for structural guidance
- Prioritize authenticity and relatability over perfection
- Every post should either teach, inspire, or spark reflection
- Images should enhance the message, not distract from it
- When in doubt, choose conversational over formal
