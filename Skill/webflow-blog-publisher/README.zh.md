[English](README.md) | [中文](README.zh.md)

---

# Webflow 博客发布器

> 将 Markdown 博客文章发布到 Webflow CMS，并自动上传图片

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 概述

自动将博客文章发布到 Webflow CMS。通过 Webflow API v2 处理 Markdown 到 HTML 的转换、自动图片上传、元数据映射和 CMS 项目创建。

### 主要功能

- 📝 **Markdown 转 HTML** - 自动转换，支持表格和代码块
- 🖼️ **自动图片上传** - 本地图片上传到 Webflow Assets
- 👤 **作者管理** - 随机或指定作者资料
- 🏷️ **分类映射** - 智能分类解析
- ⏱️ **自动字段** - 阅读时间、时间戳、排序顺序
- 🔄 **重试逻辑** - 健壮的错误处理，采用指数退避机制
- ✅ **草稿/发布** - 使用 `--publish` 标志控制状态

## 快速开始

### 先决条件

```bash
pip install requests markdown

# Configure ~/.claude/lensmor_secrets.json
{
  "WEBFLOW_API_TOKEN": "your_api_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "your_collection_id",
  "WEBFLOW_SITE_ID": "your_site_id"
}
```

有关设置，请参阅 [references/webflow-setup-guide.md](references/webflow-setup-guide.md)。

### 用法

```bash
# Publish as draft
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy

# Publish live
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

## 输入格式

期望来自 [blog-writer](../blog-writer) 的 Markdown 文件：

```markdown
# Your Blog Post Title

**Slug**: /blog/category/your-post-slug
**Meta Description**: SEO-friendly description
**Cover Image**:
![Cover](images/cover.png)

---

Article content with **bold** and *italic* text.

![Inline image](images/diagram.png)
```

## 流程

1. 解析 Markdown（标题、slug、元数据、图片、内容）
2. 将图片上传到 Webflow Assets → CDN URL
3. 将 Markdown 转换为 HTML
4. 将字段映射到 CMS 架构
5. 创建 CMS 项目（草稿或已发布）

## 命令选项

**必填：**
- `--file` - Markdown 文件路径

**可选：**
- `--category` - 分类别名（strategy, playbooks, teardowns）
- `--writer` - 作者姓名（如果未指定则随机）
- `--publish` - 立即发布（默认为草稿）
- `--collection_id` - 覆盖集合 ID

## 作者管理

作者存储在 `assets/writers/writers.json` 中：

```json
[
  {
    "name": "John Doe",
    "image_url": "https://cdn.prod.website-files.com/.../avatar.jpg"
  }
]
```

**添加作者：**
1. 将头像上传到 Webflow Assets
2. 将姓名和 CDN URL 添加到 writers.json
3. 使用 `--writer "姓名"`

## 图片上传

**支持的格式：** PNG, JPEG, GIF, WebP, AVIF, SVG

**要求：**
- 必须设置 `WEBFLOW_SITE_ID`
- 图片必须是本地文件
- 相对路径从 Markdown 文件位置解析

**没有 Site ID：** 图片将从内容中移除，需要手动上传

## 配置

创建 `~/.claude/lensmor_secrets.json`：

```json
{
  "WEBFLOW_API_TOKEN": "your_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "collection_id",
  "WEBFLOW_SITE_ID": "site_id"
}
```

或者使用环境变量（优先级更高）：

```bash
export WEBFLOW_API_TOKEN='your_token'
export WEBFLOW_BLOG_COLLECTION_ID='collection_id'
export WEBFLOW_SITE_ID='site_id'
```

## 工作流集成

与 [blog-writer](../blog-writer) 无缝协作：

```bash
# 1. 撰写内容（AI 辅助）
# 2. 生成图片
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "..." --output_dir workspace/blog/images

# 3. 发布到 Webflow
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

## 故障排除

- **图片上传超时**：检查网络连接，减小文件大小（< 5MB）
- **草稿不可见**：检查 CMS 过滤器，确认处于“所有项目”视图
- **图片未上传**：将 `WEBFLOW_SITE_ID` 添加到 secrets 文件中（在 Webflow 控制台 → 站点设置中查找）
- **API Token 错误**：验证 secrets 文件或环境变量中的 token
- **分类未找到**：使用有效的别名（strategy, playbooks, teardowns）

## 错误处理

自动重试逻辑：
- **服务器错误 (5xx)**：最多重试 3 次，采用指数退避机制
- **速率限制 (429)**：遵守 Retry-After 头部
- **超时**：每个请求 30 秒超时

## 最佳实践

**发布前：**
- 校对 Markdown 文件
- 验证图片是否存在且路径正确
- 首先以草稿形式测试（省略 `--publish`）

**安全：**
- 切勿将 secrets 文件提交到 Git
- 使用最小的 token 权限
- 定期轮换 API 密钥

## 文件结构

```
webflow-blog-publisher/
├── README.md                     # 本文件
├── SKILL.md                      # AI 工作流说明
├── scripts/
│   └── publish_to_webflow.py    # 主脚本
├── references/
│   └── webflow-setup-guide.md   # 设置说明
└── assets/
    └── writers/
        └── writers.json          # 作者资料
```

## 资源

- [SKILL.md](SKILL.md) - 技术文档
- [Setup Guide](references/webflow-setup-guide.md) - Webflow 配置
- [Blog Writer](../blog-writer) - 内容创作技能
- [Webflow API Docs](https://developers.webflow.com/) - 官方参考

---

**发布愉快！** 🚀📄

---