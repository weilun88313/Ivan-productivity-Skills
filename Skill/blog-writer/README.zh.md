[English](README.md) | [中文](README.zh.md)

---

# 博客文章撰写器

> 使用AI生成的视觉内容创作高排名、SEO友好的博客文章

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 概述

遵循经验证的内容公式，创作专业、可操作且经过SEO优化的博客文章。结合专家级内容结构与AI生成的视觉素材，产出可直接发布的文章。

### 主要功能

- ✍️ **专业内容** - 具有清晰结构、可操作且富有同理心的语气
- 📊 **SEO优化** - 为搜索引擎可见性而结构化
- 🎨 **AI生成插图** - 高质量16:9图像，采用Linear暗黑模式风格
- 📝 **结构化格式** - 钩子 → 原因 → 方法 → CTA框架
- 💡 **专业提示** - 全文穿插内幕建议
- 🎯 **可供发布** - 兼容Webflow博客发布器

## 快速开始

### 前提条件

```bash
# Install dependencies
pip install requests

# Set up API keys — copy .env.example to .env and fill in your keys
cp .env.example .env
# Edit .env:
#   GEMINI_API_KEY=your_api_key_here
```

### 基本用法

**请求一篇博客文章**

```
"Write a blog post about email marketing best practices"
```

**生成图片**

```bash
# Cover image
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Abstract email marketing data visualization, flowing connections, Linear dark mode aesthetic" \
  --output_dir workspace/blog/images \
  --filename cover

# Inline images (repeat 3-5 times)
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Email inbox interface wireframe, clean UI mockup, dark mode" \
  --output_dir workspace/blog/images \
  --filename inline_1
```

## 内容结构

文章遵循经验证的公式：

1.  **钩子** - 问题、痛点、承诺
2.  **原因** - 益处和数据
3.  **方法** - 逐步指南或列表形式
4.  **结论** - 关键要点和CTA

### 输出格式

```markdown
# [Engaging Title with Keywords]

**Slug**: /blog/[category]/[keyword-slug]
**Meta Description**: [150-160 chars SEO summary]
**Cover Image**:
![Description](images/cover.png)

---

[Article content starts here]
```

## 格式标准

-   **段落**：最多3-4行，每段一个想法
-   **标题**：H2用于主要部分，H3用于子部分
-   **列表**：步骤使用项目符号或编号列表
-   **专业提示**：每篇文章至少3个
-   **表格**：使用Markdown表格进行比较

## 图片生成

### 视觉风格

所有图片均遵循**Linear暗黑模式美学**：

-   **风格**：极简、技术、现代、抽象
-   **颜色**：深炭灰色背景（#1a1a1a），紫蓝色调（#6B75FF）
-   **元素**：抽象形状、数据可视化、几何图形
-   **质量**：16:9宽高比，高分辨率（2K+）
-   **文本**：仅限少量关键词

### 图片要求

-   **封面图片**：具有Linear美学的抽象标题图
-   **内联图片**：每篇文章至少3张，支持内容部分

使用[references/visual-style-guide.md](references/visual-style-guide.md)中完整的5段结构化模板

### 生成脚本

```bash
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Your detailed prompt here" \
  --output_dir "path/to/output" \
  --filename "image_name"
```

## SEO最佳实践

-   **标题**：50-60个字符，富含关键词
-   **Meta描述**：150-160个字符，包含益处和CTA
-   **Slug**：`/blog/[category]/[keyword-slug]`
-   **关键词**：主要关键词出现在标题/H2/第一段，密度1-2%
-   **内部链接**：每篇文章2-3个相关文章链接

## 工作流集成

与[webflow-blog-publisher](../webflow-blog-publisher)无缝协作：

```bash
# 1. Write blog post (using AI)
# 2. Generate images
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "..." \
  --output_dir workspace/blog/images

# 3. Publish to Webflow
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

## 故障排除

### API密钥未找到

```bash
# Option 1: Add to .env in repository root
# GEMINI_API_KEY=your_key

# Option 2: Environment variable
export GEMINI_API_KEY='your_key'
```

### 图片生成失败

-   如果发生超时，请简化提示
-   检查互联网连接
-   避免使用品牌名称或受版权保护的内容

### 内容质量

-   指定字数和目标受众
-   请求特定语气：“以专业博客风格撰写”
-   包含数据点和统计信息

## 文件结构

```
blog-writer/
├── README.md                  # This file
├── SKILL.md                   # AI workflow instructions
├── scripts/
│   ├── gemini_api.py         # Shared API client
│   └── generate_image.py     # Image generation tool
└── references/
    └── visual-style-guide.md # Detailed visual guidelines
```

## 资源

-   [SKILL.md](SKILL.md) - 详细的AI指令
-   [视觉风格指南](references/visual-style-guide.md) - 图片模板
-   [Webflow博客发布器](../webflow-blog-publisher) - 发布集成

---

**写作愉快！** 📝✨

---