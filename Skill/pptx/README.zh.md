[English](README.md) | [中文](README.zh.md)

---

# PPTX Skill - AI 驱动的演示文稿生成器

> 将文档转化为由 AI 生成的精美演示文稿

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 概述

使用 **Gemini 3 Pro** 进行 AI 驱动的演示文稿创建，生成带有嵌入文本的高质量幻灯片图像。遵循 Linear 风格设计，并采用深色模式美学。

### 主要特性

- 🎨 **AI 生成的幻灯片** - 带有文本和视觉效果的全出血图像
- 🌙 **Linear 设计系统** - 深色模式，#6B75FF 强调色
- 🧠 **智能模板** - 自动检测幻灯片类型
- 📊 **灵活密度** - 低（2-3 个要点）或高（4-6 个要点）内容
- 🌍 **多语言支持** - 支持中文和英文
- 🚀 **4K 分辨率** - 超高细节 (3840x2160)

## 快速开始

### 先决条件

```bash
pip install requests python-pptx markitdown[pptx]
export GEMINI_API_KEY='your_api_key_here'
```

### 使用方法

```bash
# 1. 创建计划文件 (ppt_plan.json)
# 2. 生成幻灯片图像
python scripts/ppt_img_gen.py workspace/ppt_plan.json workspace/output/images

# 3. 转换为 PowerPoint
python scripts/images2pptx.py workspace/output/images workspace/output/presentation.pptx
```

## 计划文件格式

创建 `ppt_plan.json`：

```json
[
  {
    "slide_number": 0,
    "title": "Your Title",
    "content": ["Subtitle", "Date"],
    "image_concept": "Cover slide with centered title, abstract background"
  },
  {
    "slide_number": 1,
    "title": "Key Points",
    "content": ["Point 1", "Point 2", "Point 3"],
    "image_concept": "Content slide with title top left, bullets left, visualization right"
  }
]
```

**指南：**
- **slide_number**：从 0 开始顺序编号
- **title**：幻灯片标题（目标语言）
- **content**：2-6 个要点
- **image_concept**：完整的幻灯片描述（英文）

## 脚本

### 生成幻灯片
```bash
python scripts/ppt_img_gen.py <plan_file> <output_dir> [--delay SECONDS]
```

### 创建 PowerPoint
```bash
python scripts/images2pptx.py <image_dir> <output_file>
```

### 测试单张图像
```bash
python scripts/nano_banana.py --prompt "Test" --output_dir ./output
```

## 设计系统

**视觉风格：**
- Linear 风格，极简深色模式
- 颜色：炭灰色 (#1a1a1a)，强调色 #6B75FF
- 4K 分辨率 (3840x2160)

**幻灯片类型：**
- **封面**：居中/左上角，大标题，极简背景
- **内容**：50/50 分割，标题/内容在左，视觉元素在右
- **数据**：40/60 分割，数据在左，3D 可视化在右
- **结束**：居中，标题 + 联系信息

## 内容密度

**低（推荐）**：2-3 个要点，每个 5-10 个词 - 最适合演示推介
**高（详细）**：4-6 个要点，每个 10-20 个词 - 最适合报告

## 故障排除

- **API 密钥错误**：`export GEMINI_API_KEY='your_key'`
- **速率限制**：使用 `--delay 2.0` 增加延迟
- **无效 JSON**：检查语法，移除末尾逗号

## 文件结构

```
pptx/
├── README.md              # 本文件
├── SKILL.md               # 详细文档
└── scripts/
    ├── gemini_api.py      # API 客户端
    ├── ppt_img_gen.py     # 幻灯片生成器
    └── images2pptx.py     # PowerPoint 转换器
```

## 资源

- [SKILL.md](SKILL.md) - 详细文档
- 读取现有 PPT：`python -m markitdown presentation.pptx`