"""
Jike (即刻) specific prompt templates.

Social Chinese style optimized for Jike posts.
1:1 square format default, warm and approachable aesthetic.
"""

from .base import BasePrompts, PromptBuilder


class JikePrompts(BasePrompts):
    """Prompt templates for Jike (即刻) post images."""

    @classmethod
    def cover(cls, title):
        """
        Generate a cover-style image for Jike.

        Warm, approachable style suitable for Chinese social media.

        Args:
            title: Post title or topic

        Returns:
            Complete prompt for Jike cover image
        """
        style = "Clean, fresh, modern aesthetic for Chinese social media. Warm and approachable feel (not corporate)."
        colors = "Bright, warm color palette. Friendly, inviting tones."
        concept = f"Visual representation for social post about: {title}"
        keywords = "Minimal Chinese or English text. Clean typography."
        environment = "Bright, clean background."
        negative = "NO corporate feel, NO cold aesthetics."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def post(cls, content):
        """
        Generate a Jike post image prompt.

        Creates visually appealing images for Jike (即刻) posts.

        Args:
            content: Jike post content

        Returns:
            Complete prompt for Jike post image
        """
        # Truncate content if too long
        if len(content) > 200:
            content = content[:200] + "..."

        style = """Create a visually appealing image for a social media post.

Style requirements:
- Clean, fresh, modern aesthetic
- Warm and approachable feel (not corporate)
- High resolution, 2K quality
- 1:1 square format
- Minimal or no text overlay
- Bright, warm color palette
- Suitable for casual social media
- Illustration or photography style, avoid stock photo feel"""

        colors = "Warm, friendly colors. Not corporate blues—think warm yellows, oranges, soft greens."

        concept = f"Social media visual about: {content}"

        keywords = "Minimal text. Clean, friendly typography."

        environment = "Bright, clean, approachable background."

        negative = "NO stock photo look, NO corporate aesthetics, NO cold designs."

        return f"""{style}

Color Palette: {colors}

Concept: {concept}

Keywords Allowed: {keywords}

Environment: {environment}

Negative Constraints: {negative}"""

    @classmethod
    def inline(cls, content, keywords_allowed=None):
        """
        Generate an inline-style image for Jike.

        Args:
            content: Description of what to visualize
            keywords_allowed: Optional list of allowed keywords (can be Chinese)

        Returns:
            Prompt for Jike inline visualization
        """
        style = "Friendly, approachable diagram style. Not corporate or technical."
        colors = "Warm, inviting colors. Soft backgrounds."
        concept = f"Social-friendly visualization: {content}"

        if keywords_allowed:
            keywords = f"Friendly labels: {', '.join(keywords_allowed)}"
        else:
            keywords = "Minimal, friendly labels."

        environment = "Clean, bright background."
        negative = "NO technical diagrams, NO corporate look."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def discussion(cls, topic):
        """
        Generate a discussion-style image for Jike.

        Use for conversation starters, questions, etc.

        Args:
            topic: Discussion topic

        Returns:
            Prompt for Jike discussion image
        """
        style = "Conversation-starting visual. Friendly, inviting discussion."
        colors = "Warm, social colors. Encouraging tones."
        concept = f"Discussion prompt visual: {topic[:100]}"
        keywords = "Question or topic text allowed. Friendly typography."
        environment = "Inviting background that encourages engagement."
        negative = "NO intimidating, NO overly formal designs."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)
