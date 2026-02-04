
import os
import argparse
import requests
import base64
import time
import json
import sys

# Default API Key (User provided)
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyC7mreVvH_q7djnEO4MWlP94QaMEKmmz2Y")

# Model
MODEL_NAME = "models/gemini-3-pro-image-preview"

# Global Visual Language - Shared by all pages
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
- 内容：常规字重，90%白色(#E6E6E6)，清晰易读
- 项目符号：使用 • 符号，与内容文字对齐
- 行间距：内容行间距1.5倍，确保可读性
- 对齐：标题和内容左对齐（封面和结束页居中）

视觉元素规则：
- 几何形状：浮动的立方体、球体、六边形，抽象数据结构
- 连接线：细线条，#6B75FF颜色，微妙发光效果
- 数据可视化：3D柱状图、环形图、网络节点图
- 状态指示：紫色光点表示活跃/重要元素
- 深度感：柔和阴影，营造浮动悬停感

渲染质量：超高细节，锐利清晰
"""

# Page Type Templates
PAGE_TEMPLATES = {
    "cover": """
请生成封面页。

构图：中心对称构图或偏左上构图
视觉元素：{image_concept}
标题："{title}" - 超大粗体，居中或偏左上，醒目
副标题/日期：
{content}
- 中等字号，标题下方
背景：深空背景，微妙网格，延伸的抽象数据流
""",
    
    "content": """
请生成内容页。

构图：左右分栏布局
标题："{title}" - 粗体，左上角，留出充足顶部空间
内容：左侧50%区域排版以下内容，项目符号列表：
{content}

视觉：右侧50%区域，{image_concept}
背景：左侧深色渐变利于文字阅读，右侧可有更丰富视觉元素
""",
    
    "data": """
请生成数据页或总结页。

构图：分屏设计
标题："{title}" - 粗体，左上角
内容：左侧40%区域排版以下文字和数据：
{content}

视觉：右侧60%区域，大型3D数据可视化，{image_concept}
强调：数据图表要醒目，使用#6B75FF高亮关键数据
""",
    
    "closing": """
请生成结束页。

构图：居中对称构图
标题："{title}" - 超大粗体，居中
内容：
{content}
- 中等字号，居中，标题下方
视觉：{image_concept}，淡出效果，分散粒子，优雅收尾
背景：极简，微妙渐变，干净专业
"""
}

def detect_page_type(slide_number, total_slides, title):
    """Detect page type based on slide position and title keywords"""
    if slide_number == 0:
        return "cover"
    elif slide_number == total_slides - 1:
        return "closing"
    elif any(keyword in title for keyword in ['数据', '统计', '对比', '总结', '分析', 'Data', 'Summary', 'Analysis']):
        return "data"
    else:
        return "content"

def generate_image(prompt, output_dir, filename_prefix="image"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Prompt is already complete from DESIGN_SYSTEM_TEMPLATE
    print(f"Generating: {filename_prefix}...")


    headers = {"Content-Type": "application/json"}
    url = f"https://generativelanguage.googleapis.com/v1beta/{MODEL_NAME}:generateContent?key={API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {
                "aspectRatio": "16:9",
                "imageSize": "4K"
            }
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            return

        result = response.json()
        
        if "candidates" in result:
            for i, cand in enumerate(result.get('candidates', [])):
                for part in cand.get('content', {}).get('parts', []):
                    inline_data = part.get('inline_data') or part.get('inlineData')
                    if inline_data:
                        save_image(inline_data.get('data'), output_dir, filename_prefix)
                        return
                    
        print(f"No image data found for {filename_prefix}")
        # print(result) # Silent failure preferred to reduce noise, enable if debugging needed

    except Exception as e:
        print(f"Exception: {e}")

def save_image(b64_data, output_dir, filename_prefix):
    try:
        img_data = base64.b64decode(b64_data)
        # Use simple numeric ordering if possible, or prefix
        filepath = os.path.join(output_dir, f"{filename_prefix}.png")
        with open(filepath, "wb") as f:
            f.write(img_data)
        print(f"Saved: {filepath}")
    except Exception as e:
        print(f"Error saving image: {e}")

def main():
    parser = argparse.ArgumentParser(description="Generate PPT images from a Plan JSON")
    parser.add_argument("plan_file", help="Path to the parameters/plan JSON file")
    parser.add_argument("output_dir", help="Directory to save images")
    
    args = parser.parse_args()
    
    with open(args.plan_file, 'r', encoding='utf-8') as f:
        plan = json.load(f)
        
    print(f"Loaded plan with {len(plan)} slides.")
    
    for slide in plan:
        # New format: {"slide_number": 1, "title": "...", "content": [...], "image_concept": "..."}
        # Legacy format: {"id": "slide_1", "prompt": "..."}
        
        slide_number = slide.get("slide_number")
        title = slide.get("title", "")
        content = slide.get("content", [])
        image_concept = slide.get("image_concept")
        
        # Fallback to legacy format if new format not found
        if not image_concept:
            image_concept = slide.get("prompt", "")
            slide_id = slide.get("id", f"slide_{slide_number}")
            full_prompt = image_concept  # Legacy: use as-is
        else:
            slide_id = f"slide_{slide_number:02d}"
            
            # Detect page type based on position and title
            page_type = detect_page_type(slide_number, len(plan), title)
            
            # Format content as bullet points or plain text
            if content:
                content_text = "\n".join([f"• {item}" for item in content])
            else:
                content_text = ""
            
            # Get page-specific template
            page_template = PAGE_TEMPLATES[page_type]
            
            # Build page-specific prompt
            page_prompt = page_template.format(
                title=title,
                content=content_text,
                image_concept=image_concept
            )
            
            # Combine global visual language + page-specific prompt
            full_prompt = GLOBAL_VISUAL_LANGUAGE + "\n\n" + page_prompt

        
        if full_prompt:
            print(f"\n{'='*60}")
            print(f"Generating slide {slide_number:02d}: {title} [{page_type if image_concept else 'legacy'}]")
            print(f"{'='*60}")
            generate_image(full_prompt, args.output_dir, slide_id)
            time.sleep(1) # Rate limit courtesy
        else:
            print(f"Warning: No image_concept or prompt found for slide {slide_number or slide.get('id')}")




if __name__ == "__main__":
    main()
