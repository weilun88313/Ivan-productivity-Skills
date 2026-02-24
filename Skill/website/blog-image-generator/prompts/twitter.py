"""
Twitter/X-specific prompt templates.

High viral impact style optimized for Twitter posts.
Supports multiple aspect ratios: 16:9 (landscape), 1:1 (square), 4:3 (standard).
"""

from .base import BasePrompts, PromptBuilder


class TwitterPrompts(BasePrompts):
    """Prompt templates for Twitter/X post images."""

    @classmethod
    def cover(cls, title):
        """
        Generate a cover-style image for Twitter.

        High visual impact for attention-grabbing tweets.

        Args:
            title: Tweet topic or title

        Returns:
            Complete prompt for Twitter cover image
        """
        style = "Visually striking image optimized for Twitter/X social media. High visual impact and professional quality."
        colors = "Bold, attention-grabbing colors. High contrast for visibility in feed."
        concept = f"High-impact visual representation of: {title}"
        keywords = "Minimal to no text. Bold typography if any."
        environment = "Eye-catching background suitable for social media."
        negative = "NO low-quality elements, NO blurry content."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def tweet(cls, content, aspect_ratio="16:9"):
        """
        Generate a Twitter post image prompt.

        Creates visually striking images optimized for Twitter's feed.

        Args:
            content: Tweet content
            aspect_ratio: Image aspect ratio (16:9, 1:1, 4:3)

        Returns:
            Complete prompt for Twitter tweet image
        """
        # Truncate content if too long
        if len(content) > 200:
            content = content[:200] + "..."

        style = f"""Create a visually striking image optimized for Twitter/X social media.

Requirements:
- High visual impact and professional quality
- Clear, readable text if any text is included
- Suitable for social media sharing
- Modern, clean design aesthetic
- Optimized for {aspect_ratio} aspect ratio"""

        colors = "Vibrant colors that stand out in Twitter's feed. High contrast."

        concept = f"Context: {content}"

        keywords = "Minimal text. Clean, bold typography if needed."

        environment = "Eye-catching, suitable for social media feed."

        negative = "NO clutter, NO hard-to-read text."

        return f"""{style}

Color Palette: {colors}

Context: {concept}

Keywords Allowed: {keywords}

Environment: {environment}

Negative Constraints: {negative}

Generate the image with these specifications in mind."""

    @classmethod
    def inline(cls, content, keywords_allowed=None):
        """
        Generate an inline-style image for Twitter.

        Args:
            content: Description of what to visualize
            keywords_allowed: Optional list of allowed keywords

        Returns:
            Prompt for Twitter inline visualization
        """
        style = "Attention-grabbing data visualization. High contrast, bold colors."
        colors = "Bold, vibrant colors. High contrast for visibility."
        concept = f"Eye-catching visualization: {content}"

        if keywords_allowed:
            keywords = f"Bold labels: {', '.join(keywords_allowed)}"
        else:
            keywords = "Minimal bold labels."

        environment = "Clean background that makes content pop."
        negative = "NO subtle designs that get lost in feed."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def viral(cls, hook_text):
        """
        Generate a viral-style image for Twitter.

        Use for content designed to get engagement/retweets.

        Args:
            hook_text: Viral hook or headline

        Returns:
            Prompt for viral Twitter image
        """
        style = "High-impact viral content style. Bold, attention-grabbing, designed for engagement."
        colors = "Bold, contrasting colors. Stop-the-scroll aesthetics."
        concept = f"Viral-worthy visual: {hook_text[:100]}"
        keywords = "Bold, attention-grabbing headline text if needed."
        environment = "Eye-catching, scroll-stopping background."
        negative = "NO boring, NO subtle, NO low-energy designs."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def quote(cls, quote_text, attribution=None):
        """
        Generate a quote-style image for Twitter.

        Args:
            quote_text: The quote text
            attribution: Optional attribution/name

        Returns:
            Prompt for Twitter quote image
        """
        style = "Elegant quote card design. Professional, shareable, typography-focused."
        colors = "Clean, sophisticated colors. Good contrast for text readability."
        concept = f"Inspirational or informative quote: {quote_text[:100]}"
        keywords = f"Quote text allowed. Attribution: {attribution}" if attribution else "Quote text allowed."
        environment = "Clean, elegant background. Subtle texture or gradient."
        negative = "NO clutter, NO hard-to-read typography."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)
