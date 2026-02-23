"""
Blog-specific prompt templates.

Follows the Linear Dark Mode aesthetic with 5-paragraph template structure.
Based on blog-writer/references/visual-style-guide.md
"""

from .base import BasePrompts, PromptBuilder, BasePrompts


class BlogPrompts(BasePrompts):
    """Prompt templates for blog images (cover and inline)."""

    @classmethod
    def cover(cls, title):
        """
        Generate a cover image prompt.

        Cover images are purely abstract - NO text, NO UI, NO literal depictions.
        Translate the article's theme into visual metaphor.

        Args:
            title: Blog post title

        Returns:
            Complete 5-paragraph prompt for cover image
        """
        style = "Abstract high-tech cover art, inspired by \"Linear\" app design. Dark mode UI, minimalist, clean, futuristic."
        colors = f"Primary glowing light is hex code {BasePrompts.COLOR_ACCENT} (neon violet-blue indigo). Soft, diffused glow on deep charcoal background."
        concept = f"""Key content to be displayed: {title}

Do not render these words as text. Translate the meaning into glowing geometric data streams, interconnected nodes, floating frosted glass shapes, and abstract light trails. Composition representing data flow in a sophisticated system."""
        keywords = "NO TEXT, NO LETTERS, NO WORDS, NO CHARACTERS"
        environment = "Deep black void. Very subtle, barely visible isometric grid fading into darkness. Shallow depth of field with soft bokeh effects on distant pathway nodes."
        negative = "NO TEXT, NO LETTERS, NO WORDS, NO CHARACTERS, NO UI ELEMENTS, NO DASHBOARDS, NO CHARTS. Purely abstract visual shapes and light compositions."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def inline(cls, content, keywords_allowed=None, visualization_type="data"):
        """
        Generate an inline image prompt.

        Inline images visualize specific concepts within the article.
        More structured and informational than covers, but still abstract.

        Args:
            content: Description of what to visualize
            keywords_allowed: Optional list of allowed keywords/labels
            visualization_type: Type of visualization (data, flow, segmentation, temporal)

        Returns:
            Complete 5-paragraph prompt for inline image
        """
        # Style based on visualization type
        style_map = {
            "data": "Technical data visualization inspired by Linear design system. Dark mode, minimalist, clean conceptual schematic.",
            "flow": "Abstract real-time data flow visualization inspired by Linear aesthetic. Dark mode, dynamic, flowing composition.",
            "segmentation": "Conceptual segmentation schematic inspired by Linear design. Dark mode, structured but abstract.",
            "temporal": "Temporal data evolution visualization inspired by Linear aesthetic. Dark mode, flowing progression."
        }
        style = style_map.get(visualization_type, style_map["data"])

        colors = f"Deep charcoal background ({BasePrompts.COLOR_BG_DARK}), matte grey data structures, {BasePrompts.COLOR_ACCENT} (violet-blue) accent for active elements and connections."

        concept = f"Floating visualization of: {content}"

        if keywords_allowed:
            keywords = f"Simple labels only—{', '.join(keywords_allowed)}. Clean, legible sans-serif. NO paragraphs of text."
        else:
            keywords = "Minimal labels only. Clean, legible sans-serif. NO paragraphs of text."

        environment = f"Deep {BasePrompts.COLOR_BG_DARK} void with extremely subtle technical grid lines barely visible in background. No horizon line."

        negative = "NO product UI chrome, NO navigation bars, NO sidebars, NO browser frames, NO dashboard widgets, NO fake app interfaces."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def data_cluster(cls, description, labels=None):
        """
        Generate a data cluster visualization prompt.

        Use Case: Showing grouped information, data organization, categorization

        Args:
            description: Description of the data clusters
            labels: Optional list of cluster labels

        Returns:
            Prompt for data cluster visualization
        """
        return cls.inline(
            content=f"Floating clusters of {description}. Three distinct groups interconnected by thin glowing {BasePrompts.COLOR_ACCENT} lines showing data relationships. Each cluster contains stacked translucent information cards with minimal geometric icons.",
            keywords_allowed=labels or ["Data", "Analysis", "Insights"],
            visualization_type="data"
        )

    @classmethod
    def data_flow(cls, description, labels=None):
        """
        Generate a data flow visualization prompt.

        Use Case: Showing real-time processes, movement, dynamic systems

        Args:
            description: Description of the flow
            labels: Optional list of labels for the flow

        Returns:
            Prompt for data flow visualization
        """
        return cls.inline(
            content=f"Living data streams flowing from left to right across the frame—representing {description}. Multiple parallel streams of varying thickness, each stream composed of small geometric particles (circles, diamonds, hexagons) moving at different velocities. Key insight nodes pulse with {BasePrompts.COLOR_ACCENT} glow as data passes through them.",
            keywords_allowed=labels or ["Input", "Process", "Output"],
            visualization_type="flow"
        )

    @classmethod
    def segmentation(cls, description, labels=None):
        """
        Generate a segmentation/targeting visualization prompt.

        Use Case: Showing audience segments, categorization, targeting

        Args:
            description: Description of the segments
            labels: Optional list of segment labels

        Returns:
            Prompt for segmentation visualization
        """
        return cls.inline(
            content=f"Abstract representation of {description}—multiple distinct geometric clusters (circles within circles, nested hexagons) floating at different depths in dark space. Largest cluster at center glows with {BasePrompts.COLOR_ACCENT} representing high-value targets. Surrounding satellite clusters in matte grey represent different segments.",
            keywords_allowed=labels or ["High-Value", "Qualified", "Nurture"],
            visualization_type="segmentation"
        )

    @classmethod
    def temporal(cls, description, time_labels=None):
        """
        Generate a temporal/historical visualization prompt.

        Use Case: Showing trends over time, evolution, progression

        Args:
            description: Description of the evolution
            time_labels: Optional list of time period labels

        Returns:
            Prompt for temporal visualization
        """
        return cls.inline(
            content=f"Abstract representation of {description}—three to four vertical columns of stacked data nodes progressing from left (past) to right (present). Leftmost column: smaller, dimmer matte grey nodes loosely organized. Progressive columns: nodes grow larger, brighter, more organized, culminating in rightmost column glowing with {BasePrompts.COLOR_ACCENT}.",
            keywords_allowed=time_labels or ["Q1", "Q2", "Q3", "Q4"],
            visualization_type="temporal"
        )
