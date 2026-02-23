"""
LinkedIn-specific prompt templates.

LinkedIn posts support three visual styles:
1. Linear Dark Mode - For tech/AI/abstract concepts (default)
2. Professional Business - For traditional business content
3. Photo Infographic - High-impact style with person photo and data graphics
"""

from .base import BasePrompts, PromptBuilder


# Linear Design System Colors (import from styles if needed)
COLOR_ACCENT = "#6B75FF"  # Violet-blue
COLOR_BG_DARK = "#1a1a1a"  # Deep charcoal

# Photo Infographic Style Colors
INFO_HIGHLIGHT_RED = "#FF3B3B"
INFO_HIGHLIGHT_ORANGE = "#FF6B35"
INFO_HIGHLIGHT_GREEN = "#00E676"
INFO_HIGHLIGHT_YELLOW = "#FFD700"
INFO_BG_DARK = "#0D0D0D"


class LinkedInPrompts(BasePrompts):
    """Prompt templates for LinkedIn post images."""

    @classmethod
    def cover(cls, title):
        """
        Generate a cover-style image for LinkedIn.

        Uses Linear Dark Mode style for tech/AI content.

        Args:
            title: Post title or topic

        Returns:
            Complete prompt for LinkedIn cover image
        """
        style = "Abstract high-tech visualization inspired by Linear design. Dark mode UI, minimalist, clean, futuristic."
        colors = f"Primary glowing light is {COLOR_ACCENT} (violet-blue indigo). Soft, diffused glow on deep charcoal background."
        concept = f"Abstract representation of: {title}"
        keywords = "NO TEXT in cover images. Purely abstract visual shapes."
        environment = f"Deep black void with subtle isometric grid. Shallow depth of field with soft bokeh."
        negative = "NO TEXT, NO LETTERS, NO UI ELEMENTS, NO DASHBOARDS. Purely abstract shapes."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def post(cls, content):
        """
        Generate a LinkedIn post image prompt.

        Uses Linear Dark Mode inline style with labels.

        Args:
            content: LinkedIn post content (truncated to first 200 chars)

        Returns:
            Complete prompt for LinkedIn post image
        """
        # Truncate content if too long
        if len(content) > 200:
            content = content[:200] + "..."

        style = "Technical data visualization inspired by Linear design system. Dark mode, minimalist, clean conceptual schematic."

        colors = f"Deep charcoal background ({COLOR_BG_DARK}), matte grey structures, {COLOR_ACCENT} accent for active elements."

        concept = f"Abstract visualization: {content}"

        keywords = "Simple labels only. Clean, legible sans-serif. NO paragraphs of text."

        environment = f"Deep charcoal void with extremely subtle technical grid. No horizon line."

        negative = "NO product UI chrome, NO navigation bars, NO dashboards, NO fake app interfaces."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def inline(cls, content, keywords_allowed=None):
        """
        Generate an inline-style image for LinkedIn.

        Uses Linear Dark Mode style - same as blog inline.

        Args:
            content: Description of what to visualize
            keywords_allowed: Optional list of allowed keywords

        Returns:
            Prompt for LinkedIn inline visualization
        """
        style = "Technical data visualization inspired by Linear design system. Dark mode, minimalist, clean conceptual schematic."

        colors = f"Deep charcoal background ({COLOR_BG_DARK}), matte grey data structures, {COLOR_ACCENT} accent for active elements."

        concept = f"Floating visualization of: {content}"

        if keywords_allowed:
            keywords = f"Simple labels only—{', '.join(keywords_allowed)}. Clean, legible sans-serif."
        else:
            keywords = "Minimal labels only. Clean, legible sans-serif."

        environment = f"Deep charcoal void with extremely subtle technical grid. No horizon line."

        negative = "NO product UI chrome, NO navigation bars, NO sidebars, NO browser frames, NO dashboard widgets."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def professional(cls, content):
        """
        Generate a traditional professional business style image.

        Use this for non-tech business content (leadership, HR, traditional industries).

        Args:
            content: Description of what to visualize

        Returns:
            Prompt for professional business visualization
        """
        style = "Professional business visualization, clean corporate aesthetic. Modern, minimalist."

        colors = "Professional palette with blues, teals, and oranges. Clean background."

        concept = f"Professional visualization of: {content}"

        keywords = "Minimal text. Clean, professional sans-serif."

        environment = "Clean, uncluttered background with subtle depth."

        negative = "NO product UI chrome, NO dashboards, NO cluttered layouts."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def announcement(cls, announcement_text):
        """
        Generate an announcement-style image for LinkedIn.

        Uses Linear Dark Mode style.

        Args:
            announcement_text: Announcement message

        Returns:
            Prompt for LinkedIn announcement image
        """
        style = "Abstract high-tech announcement visualization inspired by Linear design. Dark mode, minimalist."

        colors = f"Deep charcoal background, {COLOR_ACCENT} accent highlights for celebration."

        concept = f"Abstract announcement visualization: {announcement_text[:100]}"

        keywords = "Short announcement text allowed. Clean, bold typography."

        environment = "Deep background with subtle celebratory light trails."

        negative = "NO clutter, NO confusing elements."

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def photo_infographic(cls, topic, emotion="thinking", labels=None, photo_url=None):
        """
        Generate a photo infographic style image for LinkedIn posts.

        Natural, authentic style with:
        - Person with expression matching the topic mood
        - Real-life background (office, home, cafe, outdoor)
        - Subtle text/graphics overlays
        - Natural lighting

        IMPORTANT: When photo_url is provided, use it as CHARACTER REFERENCE ONLY.
        The model CAN and SHOULD change: expression, pose, camera angle, shot distance.
        ONLY keep the person's identity/face consistent.

        Args:
            topic: The main topic or message to visualize (from post content)
            emotion: Facial expression matching topic (thinking, shocked, surprised, excited,
                     worried, confused, headache, etc.)
            labels: List of text labels for graphic elements (e.g., ['PRE-TRAINING', 'POST-TRAINING'])
            photo_url: Optional URL/path to user's photo as CHARACTER REFERENCE

        Returns:
            Prompt for photo infographic style image
        """
        # Default labels if not provided
        if not labels:
            labels = ["INSIGHT", topic[:10].upper()]

        emotion_descriptions = {
            "thinking": "deep in thought - finger on chin/temple, eyes looking upward, contemplative expression, naturally posed",
            "shocked": "genuinely shocked - wide eyes, jaw dropped, hands raised in surprise, authentic reaction",
            "surprised": "pleasantly surprised - eyebrows raised, leaning forward slightly with curiosity, genuine expression",
            "excited": "genuinely excited - warm enthusiastic smile, eyes bright, natural hand gestures, authentic energy",
            "worried": "thoughtfully concerned - genuine worried expression, hand near face, concerned but composed",
            "confused": "genuinely puzzled - squinting slightly, head tilted naturally, questioning expression",
            "headache": "tired from thinking - hand rubbing temples naturally, slight frown, eyes closed or looking down",
            "amazed": "genuinely amazed - eyes wide with wonder, mouth slightly open, hands framing face naturally"
        }

        emotion_desc = emotion_descriptions.get(emotion, emotion_descriptions["thinking"])

        if photo_url:
            # For image editing: photo is CHARACTER REFERENCE, not final pose
            style = f"""LinkedIn Post Photo Infographic: Use this photo as CHARACTER REFERENCE ONLY.

CHARACTER USAGE (CRITICAL):
- This photo shows the person's face/identity - keep their appearance consistent
- You ARE ALLOWED and ENCOURAGED to change: expression, pose, body language, camera angle, shot distance
- Recreate the person with {emotion_desc}
- Choose the best shot: full body, medium shot, or close-up - whichever looks most natural

BACKGROUND - REAL LIFE SCENE:
- Use a REAL, NATURAL background: modern minimalist office, clean home workspace, or bright neutral space
- Apple-style aesthetic: clean, uncluttered, lots of negative space
- Soft natural lighting - diffused window light or soft ambient light
- Background should feel calm and purposeful
- Subtle depth: background gently blurred

GRAPHICS - APPLE-STYLE MINIMALISM:
- Text labels should be PRECISE and REFINED
- Use SF Pro or similar clean sans-serif font
- Letter-spacing slightly increased for elegance
- Position text with generous whitespace around it
- Size: prominent but not overwhelming

Color strategy (Apple-inspired):
- Primary: crisp white text on dark overlay, OR dark text on light overlay
- Accent: single accent color used sparingly - either soft blue (#0071E3), warm orange (#FF6B35), or mint green (#00D68F)
- Semi-transparent backgrounds: white at 85-90% opacity with subtle blur, or black at 75-80%
- Ultra-thin dividing lines (0.5px) in light gray
- Small circular or square accent marks - geometric, precise

Layout approach:
- Large clean negative space
- Text aligned with precision (left-aligned or centered)
- One primary label, optional smaller secondary labels
- Think Apple product launch aesthetics

COMPOSITION:
- Generous negative space around all elements
- Person and graphics don't compete - they coexist harmoniously
- Clean horizontal or vertical lines to guide eye
- Balanced, breathing room throughout

INTEGRATION:
- Graphics feel like they BELONG in the photo, not added
- Subtle drop shadows (very soft, large spread)
- No hard edges - everything feathered naturally
- Color grading unifies photo and graphics

MOOD:
- Premium, intentional, confident
- Like Apple's "Behind the Mac" campaign
- Sophisticated without being pretentious"""

            colors = f"""Apple-inspired palette:
- Primary: pure white (#FFFFFF) on dark, or near-black (#1D1D1F) on light
- Accent blue: #0071E3 (Apple blue)
- Accent orange: #FF6B35
- Accent green: #00D68F
- Background overlays: white 90%, black 75%
- Lines: #E5E5E5 (ultra-light gray)
- Shadows: soft, multi-layered, natural"""

            concept = f"Create an Apple-style aesthetic LinkedIn post about {topic}. Use the reference photo for the person's identity. Premium, minimalist, precise."

            keywords = f"""Text labels: {', '.join(labels)}. Apple-style minimalism.
SF Pro font aesthetics. Generous negative space. Precise alignment.
Single accent color. Soft overlays. Premium feel.
Clean typography. Refined spacing."""

            environment = f"""Minimalist real-life setting:
1. Clean modern office with white walls and natural light
2. Uncluttered home workspace with neutral tones
3. Bright space with large windows and diffused light
4. Minimal desk setup with intentional props

Choose: clean, calm, purposeful environment."""

            negative = """NO neon. NO glow effects. NO gradient text.
NO multiple competing colors. NO crowded layouts.
NO heavy shadows. NO hard edges.
NO YouTube/Clickbait style.
Think Apple, not tech startup."""

        else:
            # For pure generation (no photo provided)
            person_element = f"Professional person with {emotion_desc}, wearing business casual attire, in a natural real-life setting"

            style = f"""LinkedIn Post Photo Infographic. Natural, authentic scene:
- Person: {person_element}
- Background: Real life setting (office, home, cafe) with natural lighting
- Subtle text overlays in empty spaces
- Documentary-style, candid feel
- Warm and approachable"""

            colors = f"""Natural warm tones. Muted accent colors.
Soft lighting. No harsh contrasts."""

            concept = f"Authentic photo about: {topic}"

            keywords = f"""Text labels: {', '.join(labels)}. Subtle overlays.
Natural setting. Professional LinkedIn style."""

            environment = f"Real background: office, home workspace, or cafe. Natural lighting."

            negative = """NO tech backgrounds. NO neon. NO studio feel.
Keep it natural and authentic."""

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)

    @classmethod
    def photo_info(cls, topic, photo_url=None, overlay_text=None):
        """
        Generate a photo + info elements style image.

        Uses a photo background with integrated informational elements.
        Good for personal, human-centric content.

        Args:
            topic: The topic or message to visualize
            photo_url: Optional URL/path to user's photo
            overlay_text: Optional text to overlay on image

        Returns:
            Prompt for photo + info style image
        """
        if photo_url:
            base_photo = f"Use photo from {photo_url} as background"
        else:
            base_photo = "Professional photo background, warm natural lighting"

        if overlay_text:
            text_element = f"Overlay text: '{overlay_text}' in clean white sans-serif with subtle shadow"
        else:
            text_element = "Minimal text overlay with topic highlights"

        style = f"""Photo + Info Elements style:
- Base: {base_photo}
- Overlay: Semi-transparent dark gradient at bottom
- Graphics: Simple icons or charts in corners, thin white lines
- Text: {text_element}
- Overall: Warm, approachable, authentic"""

        colors = "Warm palette with skin tones, white text on dark overlays, subtle accent colors."

        concept = f"Personal storytelling visual about: {topic}"

        keywords = "Short, legible text. Simple iconography. Clean graphic overlays."

        environment = "Natural lighting, shallow depth of field, authentic atmosphere."

        negative = """NO fake stock photos. NO overly busy graphics. NO hard-to-read text.
NO harsh filters. Keep it authentic and relatable."""

        return PromptBuilder.build(style, colors, concept, keywords, environment, negative)
