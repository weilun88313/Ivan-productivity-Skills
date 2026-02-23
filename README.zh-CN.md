[![EN](https://img.shields.io/badge/English-blue?style=for-the-badge)](./README.md)
[![中文](https://img.shields.io/badge/简体中文-red?style=for-the-badge)](./README.zh-CN.md)

# Ivan 的生产力技能合集

用于内容创作、社交媒体、销售自动化和工作流自动化的生产就绪 AI 技能。

## 📚 可用技能 (14 个)

### 🌐 官网博客

**[keyword-research](./Skill/website/keyword-research/)** - 使用 Ahrefs API 集成发现高价值关键词以进行 SEO 策略

**[blog-writer](./Skill/website/blog-writer/)** - 生成 SEO 优化博客文章，配有 AI 生成的 Linear 风格插图

**[blog-image-generator](./Skill/website/blog-image-generator/)** - 统一 AI 图片生成服务，适用于所有平台（博客、LinkedIn、Twitter、即刻、PPTX）

**[webflow-blog-publisher](./Skill/website/webflow-blog-publisher/)** - 将 Markdown 文章发布到 Webflow CMS，并自动上传图片

**[content-pipeline](./Skill/website/content-pipeline/)** - 端到端自动化：研究 → 撰写 → 图片 → 发布

### 📱 社交媒体

**[linkedin-post-writer](./Skill/social-media/linkedin-post-writer/)** - 创建具有品牌一致格式的专业 LinkedIn 帖子

**[twitter-post-writer](./Skill/social-media/twitter-post-writer/)** - 生成具有病毒式传播优化的引人入胜的 Twitter/X 帖子

**[jike-post-writer](./Skill/social-media/jike-post-writer/)** - 为即刻社交平台创建内容

### 🛠️ 开发工具

**[pptx](./Skill/pptx/)** - 创建遵循 Linear 设计风格的 AI 生成视觉内容的演示文稿幻灯片

**[skill-creator](./Skill/skill-creator/)** - 使用双语文档模板搭建新技能

**[skill-manager](./Skill/skill-manager/)** - 管理和组织技能仓库

**[skill-evolution-manager](./Skill/skill-evolution-manager/)** - 跟踪和演进技能能力

**[github-to-skills](./Skill/github-to-skills/)** - 将 GitHub 仓库转换为 Claude Code 技能

**[lensmor-brand-guideline](./Skill/lensmor-brand-guideline/)** - 集中化的品牌信息和产品详情参考

---

## 🚀 快速开始

### 先决条件

```bash
# Python 3.8+
pip install -r requirements.txt

# 配置 API 密钥
cp .env.example .env
# 编辑 .env 并添加您的密钥
```

### 示例：官网博客工作流

```bash
# 1. 研究关键词
cd Skill/website/keyword-research
# "Research keywords for AI content marketing"

# 2. 撰写博客文章
cd ../blog-writer
# "Write a blog post about AI content marketing best practices"

# 3. 生成图片（使用统一的 blog-image-generator）
cd ../blog-image-generator
python scripts/generate.py --platform blog --type cover --prompt "AI 内容营销" --output ../../../workspace/blog/images/cover.png

# 4. 发布到 Webflow
cd ../webflow-blog-publisher
python scripts/publish_to_webflow.py --file ../../../workspace/blog/article.md --publish
```

**或使用完整管道：**
```bash
cd Skill/website/content-pipeline
# "Run the content pipeline for AI content marketing"
```

---

## 📖 文档

每个技能都包含：
- **README.md** / **README.zh.md** - 用户指南（双语）
- **SKILL.md** - AI 代理指令
- **examples/** - 示例用法（可选）
- **scripts/** - 可执行工具

**关键资源：**
- [技能开发指南](./SKILL_DEVELOPMENT_GUIDELINES.md)
- [内容管道指南](./Skill/website/content-pipeline/README.md)

---

## 🔐 配置

将 `.env.example` 复制为 `.env` 并填入密钥：

```bash
cp .env.example .env
```

```dotenv
# .env
GEMINI_API_KEY=your_gemini_api_key
FAL_KEY=your_fal_api_key
WEBFLOW_API_TOKEN=your_webflow_token
WEBFLOW_BLOG_COLLECTION_ID=your_collection_id
WEBFLOW_SITE_ID=your_site_id
```

或导出为环境变量：
```bash
export GEMINI_API_KEY="your_key"
export FAL_KEY="your_key"
```

---

## 🛠️ 技术栈

- **Python 3.8+** - 核心语言
- **Gemini API / Fal.ai** - AI 图像生成（自动回退）
- **Ahrefs API v3** - SEO 关键词研究
- **Webflow API v2** - CMS 发布
- **Apollo.io** - 潜在客户数据源
- **n8n** - 工作流自动化
- **Markdown** - 内容格式

---

## 🤝 贡献

1. Fork 此仓库
2. 创建功能分支
3. 遵循[技能开发指南](./SKILL_DEVELOPMENT_GUIDELINES.md)
4. 彻底测试
5. 提交 Pull Request

---

## 📄 许可证

本项目为私有项目。保留所有权利。

---

**用 ❤️ 构建，旨在实现高效内容创作、社交媒体和销售自动化**
