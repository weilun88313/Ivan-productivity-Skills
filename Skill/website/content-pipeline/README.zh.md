[English](README.md) | [中文](README.zh.md)

---

# 内容流水线

端到端的内容工作流程，可在单个会话中协调关键词研究、博客文章撰写、图像生成和 Webflow 发布。

## 主要功能

- **一个命令，完整流水线**：研究 → 撰写 → 图像 → 发布
- **智能编排**：仅在关键决策（主题选择）时暂停
- **品牌感知**：自动加载 MyCompany 品牌指南以用于产品内容
- **集成图像生成**：Gemini API 采用一致的 Linear 暗色模式风格
- **Webflow 发布**：直接 CMS 集成，支持草稿/发布选项

## 快速开始

```
Run the content pipeline for [topic/product]
```

或

```
Research keywords, write an article, and publish to Webflow about [topic]
```

该流水线将：
1. 头脑风暴关键词并建议文章主题
2. 等待您选择主题
3. 撰写完整文章
4. 生成封面 + 内联图像
5. 发布到 Webflow（默认为草稿）

## 先决条件

```bash
pip install requests markdown
```

API 密钥位于 `.env`（仓库根目录）中：
- `GEMINI_API_KEY`（Gemini 图像生成）
- `WEBFLOW_API_TOKEN`
- `WEBFLOW_BLOG_COLLECTION_ID`
- `WEBFLOW_SITE_ID`

## 相关技能

| Skill | Purpose |
|-------|---------|
| [keyword-research](../keyword-research/) | 独立关键词研究 |
| [blog-writer](../blog-writer/) | 独立文章撰写 |
| [webflow-blog-publisher](../webflow-blog-publisher/) | 独立 Webflow 发布 |
| [mycompany-brand-guideline](../mycompany-brand-guideline/) | MyCompany 品牌上下文 |