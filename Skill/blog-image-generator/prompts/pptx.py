"""
PowerPoint specific prompt templates.

Chinese language, Linear presentation style for PPT slides.
Based on pptx/scripts/ppt_img_gen.py
"""

from .base import BasePrompts, PromptBuilder


class PPTPrompts(BasePrompts):
    """Prompt templates for PowerPoint slide images."""

    # Global visual language for PPT slides
    GLOBAL_VISUAL_LANGUAGE = """
你是一位专家级演示设计师，请生成16:9高保真演示文稿幻灯片。

全局视觉规范：
- 风格：Linear技术美学，极简主义，深色模式，哑光质感
- 配色：深炭黑渐变背景(#1a1a1a到#0a0a0a)，紫蓝色强调(#6B75FF)用于高亮和连接
- 材质：哑光表面，无光泽，技术感
- 光照：柔和环境光，微妙的光线追踪反射
- 背景：极其微妙的技术网格线(5%不透明度)
- 留白：保持大量留白，避免拥挤，呼吸感强

文字排版规则：
- 标题：粗体现代无衬线字体，纯白色(#FFFFFF)，醒目
- 内容：常规字重，90%白色(#E6E6E6)，清晰易读，自然段落排版
- 行间距：内容行间距1.5倍，确保可读性
- 对齐：标题和内容左对齐（封面和结束页居中）
- 分隔：使用空行或视觉元素分隔不同要点，不使用项目符号

视觉元素规则：
- 几何形状：浮动的立方体、球体、六边形，抽象数据结构
- 连接线：细线条，#6B75FF颜色，微妙发光效果
- 数据可视化：3D柱状图、环形图、网络节点图
- 状态指示：紫色光点表示活跃/重要元素
- 深度感：柔和阴影，营造浮动悬停感

渲染质量：超高细节，锐利清晰"""

    @classmethod
    def cover(cls, title, subtitle=""):
        """
        Generate a cover slide prompt.

        Args:
            title: Slide title
            subtitle: Optional subtitle/date

        Returns:
            Complete prompt for cover slide
        """
        slide_content = f"""请生成封面页。

构图：中心对称构图或偏左上构图
视觉元素：抽象的{title}概念可视化
标题："{title}" - 超大粗体，居中或偏左上，醒目
副标题：
{subtitle}
- 中等字号，标题下方
背景：深空背景，微妙网格，延伸的抽象数据流"""

        return f"{cls.GLOBAL_VISUAL_LANGUAGE}\n\n{slide_content}"

    @classmethod
    def slide(cls, title, content, image_concept="", slide_type="content"):
        """
        Generate a content slide prompt.

        Args:
            title: Slide title
            content: List of content points or string
            image_concept: Visual concept description
            slide_type: Type of slide (cover, content, data, closing)

        Returns:
            Complete prompt for content slide
        """
        # Format content as natural paragraphs
        if isinstance(content, list):
            content_text = "\n\n".join(content)
        else:
            content_text = str(content)

        if slide_type == "cover":
            return cls.cover(title, content_text)

        elif slide_type == "data":
            return cls.data_slide(title, content_text, image_concept)

        elif slide_type == "closing":
            return cls.closing(title, content_text)

        else:  # content
            return cls.content_slide(title, content_text, image_concept)

    @classmethod
    def content_slide(cls, title, content, image_concept=""):
        """Generate a content slide prompt."""
        slide_content = f"""请生成内容页。

构图：自由创意布局，让文字与视觉元素自然融合
标题："{title}" - 粗体醒目，位置灵活（可以左上、居中或右上，根据视觉需求）
内容：以下内容需要融入画面，使用自然段落排版（不使用项目符号）：
{content}

视觉设计：{image_concept or "抽象数据可视化"}
设计原则：
- 文字不是孤立的文本块，而是视觉设计的一部分
- 可以让视觉元素环绕文字，或让文字嵌入视觉元素中
- 文字可以有渐变、发光、阴影等效果，与背景融合
- 背景和前景应该协调统一，形成整体画面
- 使用空行或视觉元素自然分隔不同要点"""

        return f"{cls.GLOBAL_VISUAL_LANGUAGE}\n\n{slide_content}"

    @classmethod
    def data_slide(cls, title, data_content, image_concept=""):
        """Generate a data slide prompt."""
        slide_content = f"""请生成数据页或总结页。

构图：数据驱动的创意布局，让数字与视觉叙事融为一体
标题："{title}" - 粗体醒目，位置灵活
内容：以下数据内容需要融入数据可视化中（不使用项目符号）：
{data_content}

视觉设计：{image_concept or "抽象数据可视化"}
数据呈现原则：
- 数字和文字应该成为视觉元素的一部分，不是单独的文本块
- 可以让数据标签直接标注在图表上，融入3D可视化中
- 使用#6B75FF高亮关键数据，让数字本身发光
- 让文字、数字、图表形成统一的视觉故事
- 避免生硬的左右分栏，追求有机的整体构图
- 使用空行或视觉元素自然分隔不同数据点"""

        return f"{cls.GLOBAL_VISUAL_LANGUAGE}\n\n{slide_content}"

    @classmethod
    def closing(cls, title, content=""):
        """Generate a closing slide prompt."""
        slide_content = f"""请生成结束页。

构图：居中对称构图
标题："{title}" - 超大粗体，居中
内容：
{content}
- 中等字号，居中，标题下方
视觉：淡出效果，分散粒子，优雅收尾
背景：极简，微妙渐变，干净专业"""

        return f"{cls.GLOBAL_VISUAL_LANGUAGE}\n\n{slide_content}"

    @classmethod
    def inline(cls, content, keywords_allowed=None):
        """
        Generate an inline-style image (not typically used for PPT).

        Args:
            content: Description of what to visualize
            keywords_allowed: Optional list of allowed keywords

        Returns:
            Prompt for inline visualization
        """
        return cls.content_slide("Visualization", content, keywords_allowed or "")

    @classmethod
    def from_slide_dict(cls, slide, total_slides):
        """
        Generate prompt from slide dictionary.

        Detects slide type based on position and title.

        Args:
            slide: Dictionary with slide_number, title, content, image_concept
            total_slides: Total number of slides

        Returns:
            Complete prompt for the slide
        """
        slide_number = slide.get("slide_number", 0)
        title = slide.get("title", "")
        content = slide.get("content", [])
        image_concept = slide.get("image_concept", "")

        # Detect page type
        if slide_number == 0:
            page_type = "cover"
        elif slide_number == total_slides - 1:
            page_type = "closing"
        elif any(keyword in title for keyword in ['数据', '统计', '对比', '总结', '分析', 'Data', 'Summary', 'Analysis']):
            page_type = "data"
        else:
            page_type = "content"

        return cls.slide(title, content, image_concept, page_type)
