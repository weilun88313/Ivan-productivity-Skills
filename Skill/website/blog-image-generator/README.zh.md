# 博客图片生成器

**统一 AI 图片生成服务，适用于所有平台** - 独立技能，为博客文章、社交媒体和演示文稿生成高质量、风格一致的图片。

## 概述

此技能将多个技能（blog-writer、linkedin-post-writer、twitter-post-writer、jike-post-writer、pptx）的图片生成功能整合到一个统一的服务中。

### 核心特性

- **多 API 支持**: Gemini（主要）配合 Fal.ai 自动备用
- **平台特定样式**: 为每个平台优化的提示词
- **Linear 深色模式美学**: 所有图片保持一致的视觉风格
- **CLI 和 Python API**: 可独立使用或导入其他技能
- **批量生成**: 一次生成多张图片

## 安装

1. 将此技能克隆到 `Skill/` 目录：
```bash
cd /Users/ivan/Documents/Ivan_Skills/Skill/website/blog-image-generator
```

2. 安装依赖：
```bash
pip install requests
```

3. 配置 API 密钥 — 将 `.env.example` 复制为 `.env` 并填入密钥：
```bash
cp .env.example .env
# 编辑 .env：
#   GEMINI_API_KEY=你的-gemini-api-密钥
#   FAL_KEY=你的-fal-ai-密钥
```

## 使用方法

### 命令行界面

生成单张图片：
```bash
python scripts/generate.py \
  --platform blog \
  --type cover \
  --prompt "邮件营销最佳实践" \
  --output cover.png
```

批量生成：
```bash
python scripts/batch.py \
  --platform blog \
  --prompts prompts.json \
  --output_dir images/
```

### Python API

```python
from Skill.blog_image_generator.scripts.image_generator import ImageGenerator
from Skill.blog_image_generator.prompts import BlogPrompts, LinkedInPrompts

# 初始化生成器
gen = ImageGenerator()

# 生成博客封面图片
prompt = BlogPrompts.cover("邮件营销最佳实践")
image = gen.generate(prompt, style="blog", aspect_ratio="16:9")
gen.save(image, "cover.png")

# 生成 LinkedIn 帖子图片
prompt = LinkedInPrompts.post("很高兴宣布我们的新产品发布！")
image = gen.generate(prompt, style="linkedin", aspect_ratio="16:9")
gen.save(image, "linkedin_post.png")
```

## 平台支持

| 平台 | 宽高比 | 样式 | 用途 |
|------|--------|------|------|
| `blog` | 16:9 | Linear 深色模式 | 博客封面/内文图片 |
| `linkedin` | 16:9 | 专业商务风格 | LinkedIn 帖子 |
| `twitter` | 16:9, 1:1, 4:3 | 病毒式高冲击力 | Twitter/X 推文 |
| `jike` | 1:1 | 社交中文风格 | 即刻帖子 |
| `pptx` | 16:9 | Linear 演示风格 | PowerPoint 幻灯片 |

## 提示词模板

### 博客图片

```python
from Skill.blog_image_generator.prompts import BlogPrompts

# 封面图片 - 纯抽象
cover_prompt = BlogPrompts.cover("你的博客标题")

# 内文图片 - 概念可视化
inline_prompt = BlogPrompts.inline("显示用户旅程的数据流可视化")
```

### 社交媒体图片

```python
from Skill.blog_image_generator.prompts import LinkedInPrompts, TwitterPrompts, JikePrompts

# LinkedIn
linkedin_prompt = LinkedInPrompts.post("你的帖子内容")

# Twitter
twitter_prompt = TwitterPrompts.tweet("你的推文内容", aspect_ratio="16:9")

# 即刻
jike_prompt = JikePrompts.post("你的即刻内容")
```

### 演示文稿图片

```python
from Skill.blog_image_generator.prompts import PPTPrompts

slide_prompt = PPTPrompts.slide(
    title="数据分析",
    content=["关键洞察 1", "关键洞察 2"],
    image_concept="抽象数据可视化",
    slide_type="content"
)
```

## 视觉样式系统

所有生成的图片都遵循 **Linear 深色模式** 美学：

- **背景**: 深炭色 (#1a1a1a 到 #0a0a0a)
- **强调色**: 紫蓝色 (#6B75FF)
- **质量**: 极简主义，哑光表面，高细节
- **元素**: 抽象几何形状，数据流，微妙的网格

完整规范请参阅 `visual-style-guide.md`。

## CLI 选项

### generate.py

```
--platform     平台：blog, linkedin, twitter, jike, pptx
--type         图片类型：cover, inline, post, slide
--prompt       文本描述或标题
--output       输出文件路径
--aspect-ratio 宽高比（默认：16:9）
--quality      图片质量：2K, 4K（默认：2K）
```

### batch.py

```
--platform     平台：blog, linkedin, twitter, jike, pptx
--prompts      包含提示词数组的 JSON 文件
--output_dir   生成图片的目录
--delay        API 调用之间的延迟（秒）
```

## API 备用行为

生成器自动按顺序尝试提供商：

1. **Gemini API** (GEMINI_API_KEY)
2. **Fal.ai Nano Banana Pro** (FAL_KEY)

如果一个失败，会自动尝试下一个可用的提供商。

## 文件结构

```
blog-image-generator/
├── README.md              # 英文文档
├── README.zh.md           # 中文文档（本文件）
├── SKILL.md               # AI 指令
├── scripts/
│   ├── generate.py        # CLI 入口
│   ├── batch.py           # 批量生成
│   └── image_generator.py # 核心 API 客户端
├── prompts/
│   ├── base.py            # 基础模板
│   ├── blog.py            # 博客提示词
│   ├── linkedin.py        # LinkedIn 提示词
│   ├── twitter.py         # Twitter 提示词
│   ├── jike.py            # 即刻提示词
│   └── pptx.py            # PPT 提示词
└── styles/
    ├── common.py          # 共享定义
    ├── linear.py          # Linear 博客样式
    ├── linkedin.py        # LinkedIn 样式
    ├── twitter.py         # Twitter 样式
    ├── jike.py            # 即刻样式
    └── pptx.py            # PPT 样式
```

## 与其他技能集成

安装后，其他技能可以使用共享服务：

```python
# 在任何技能的脚本中
from Skill.blog_image_generator.scripts.image_generator import ImageGenerator
from Skill.blog_image_generator.prompts import BlogPrompts

gen = ImageGenerator()
prompt = BlogPrompts.cover("文章标题")
image = gen.generate(prompt, style="blog")
```

## 错误处理

生成器处理常见错误：

- **速率限制**: 指数退避自动重试
- **区域限制**: 备用其他提供商
- **超时**: 可配置超时（默认：180秒）
- **API 错误**: 详细的错误调试信息

## 许可证

Ivan's Skills 集合的一部分。

## 相关技能

- [blog-writer](../blog-writer/) - 生成 SEO 优化的博客文章
- [linkedin-post-writer](../../social-media/linkedin-post-writer/) - 生成 LinkedIn 内容
- [twitter-post-writer](../../social-media/twitter-post-writer/) - 生成 Twitter 内容
- [content-pipeline](../content-pipeline/) - 端到端自动化工作流
