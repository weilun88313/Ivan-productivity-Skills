# 开发者技能集合

[![EN](https://img.shields.io/badge/English-blue?style=for-the-badge)](./README.md)
[![中文](https://img.shields.io/badge/简体中文-red?style=for-the-badge)](./README.zh-CN.md)

一套用于内容创作、活动情报和工作流自动化的生产级AI技能集合。

## 📚 可用技能

### 🎨 内容创作

#### [hubspot-blog-writer](./Skill/hubspot-blog-writer/)
生成高质量、SEO优化的HubSpot风格博客文章，配备AI生成的插图。

**功能特性：**
- 5段式提示词模板，确保图片质量一致
- Linear深色模式美学（#6B75FF, #1a1a1a）
- 使用Gemini API自动生成图片
- 4种内联图片类别（数据簇、流程、分层、时间线）
- 完整内容结构（Hook → Why → How → CTA）

**使用场景：** 创建带抽象可视化的专业博客内容

---

#### [pptx](./Skill/pptx/)
生成遵循Linear设计原则的演示幻灯片，配备AI生成的图片。

**功能特性：**
- 结构化提示词模板，保证视觉一致性
- 共享Gemini API模块
- 支持多种幻灯片布局
- 完整设计系统文档

**使用场景：** 创建专业视觉效果的演示文稿

---

### 📤 内容发布

#### [webflow-blog-publisher](./Skill/webflow-blog-publisher/)
将Markdown博客文章直接发布到Webflow CMS，自动上传图片并映射字段。

**功能特性：**
- 自动上传封面图和内联图片到Webflow Assets
- 全宽图片样式（使用`!important`覆盖）
- 动态字段检测和映射
- 支持元描述、分类和作者配置
- Markdown转HTML，保留完整alt文本

**使用场景：** 从Markdown到Webflow站点的自动化博客发布流程

---

### 🔍 研究与情报

#### [exhibitor-page-navigator](./Skill/exhibitor-page-navigator/)
智能导航展商网站，提取产品和公司信息。

**功能特性：**
- 4阶段工作流，带置信度评分
- 保护内容的备用策略
- 6个JSON示例场景
- 高/中/低置信度级别

**使用场景：** 自动化展商调研，用于展会和活动

---

## 🚀 快速开始

### 环境要求

```bash
# Python 3.8+
python --version

# 安装依赖
pip install -r requirements.txt

# 配置API密钥
cp ~/.claude/lensmor_secrets.json.example ~/.claude/lensmor_secrets.json
# 编辑并添加你的API密钥
```

### 示例：生成博客文章

```bash
# 1. 生成博客内容
cd Skill/hubspot-blog-writer
python scripts/generate_blog.py --topic "邮件营销最佳实践"

# 2. 生成图片（使用5段式模板）
python scripts/generate_image.py \
  --prompt "$(cat references/visual-style-guide.md | grep -A 50 'Cover Image Example')" \
  --output_dir ../../workspace/images

# 3. 发布到Webflow
cd ../webflow-blog-publisher
python scripts/publish_to_webflow.py \
  --file ../../workspace/your-blog.md \
  --category strategy
```

---

## 📖 文档

每个技能都包含完整文档：

- **README.md** - 用户指南，包含快速开始、使用案例和故障排除
- **SKILL.md** - AI代理指令（用于Claude Code等工具）
- **examples/** - 示例输入和输出
- **references/** - 风格指南和模板

### 核心文档文件

- [博客工作流指南](./Skill/BLOG_WORKFLOW.md) - 端到端博客创建和发布
- [视觉风格指南](./Skill/hubspot-blog-writer/references/visual-style-guide.md) - 强制5段式提示词模板
- [优化总结](./Skill/OPTIMIZATION_SUMMARY.md) - 技能审计和改进报告

---

## 🎨 视觉风格系统

所有生成的图片都遵循**严格的5段式提示词模板**：

1. **Style（风格）** - 视觉方法（例如："抽象高科技封面艺术"）
2. **Color Palette（配色）** - 精确的十六进制颜色代码（#6B75FF, #1a1a1a）
3. **Concept（概念）** - 详细的抽象描述
4. **Keywords Allowed（允许的关键词）** - 最少文字规范
5. **Environment（环境）** - 背景和深度细节
6. **Negative Constraints（负面约束）** - 明确禁止项（NO UI、NO仪表板）

**为什么？** 确保一致的Linear深色美学，防止UI元素出现。

---

## 🛠️ 技术栈

- **Python 3.8+** - 核心语言
- **Gemini API** - AI图片生成（gemini-3-pro-image-preview）
- **Webflow API v2** - CMS发布
- **Markdown** - 内容格式
- **GitHub Actions** - CI/CD（可选）

---

## 📊 项目结构

```
.
├── README.md                           # 英文版
├── README.zh-CN.md                     # 本文件（中文版）
├── .gitignore                          # 忽略规则
├── Skill/
│   ├── BLOG_WORKFLOW.md                # 博客创建指南
│   ├── OPTIMIZATION_SUMMARY.md         # 技能报告
│   │
│   ├── hubspot-blog-writer/
│   │   ├── README.md                   # 用户指南（503行）
│   │   ├── SKILL.md                    # AI指令
│   │   ├── references/
│   │   │   └── visual-style-guide.md   # 5段式模板（303行）
│   │   ├── scripts/
│   │   │   ├── gemini_api.py           # 共享API模块
│   │   │   └── generate_image.py       # 图片生成
│   │   └── examples/
│   │       └── sample-blog-post.md     # 完整示例（2,400词）
│   │
│   ├── webflow-blog-publisher/
│   │   ├── README.md                   # 用户指南（573行）
│   │   ├── scripts/
│   │   │   └── publish_to_webflow.py   # 发布脚本（449行）
│   │   └── assets/
│   │       └── writers/
│   │           └── writers.json        # 作者配置
│   │
│   ├── exhibitor-page-navigator/
│   │   ├── README.md                   # 用户指南（329行）
│   │   ├── SKILL.md                    # 增强版（从38行到293行）
│   │   └── examples/                   # 6个JSON场景
│   │
│   └── pptx/
│       ├── README.md                   # 用户指南（464行）
│       ├── SKILL.md
│       └── scripts/
│           ├── gemini_api.py           # 共享模块
│           ├── ppt_img_gen.py
│           └── images2pptx.py
│
└── workspace/                          # 生成的内容（已忽略）
    ├── images/
    └── *.md
```

---

## 🔐 配置

所有API密钥应存储在 `~/.claude/lensmor_secrets.json`：

```json
{
  "NANO_API_KEY": "你的gemini_api_key",
  "WEBFLOW_API_TOKEN": "你的webflow_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "你的collection_id",
  "WEBFLOW_SITE_ID": "你的site_id"
}
```

或者设置环境变量：

```bash
export GEMINI_API_KEY="你的密钥"
export WEBFLOW_API_TOKEN="你的token"
export WEBFLOW_BLOG_COLLECTION_ID="你的collection_id"
export WEBFLOW_SITE_ID="你的site_id"
```

---

## 📈 最近更新

### v2.1.0 (2026-02-09)

**图片生成质量控制**
- ✅ 强制所有图片使用完整5段式提示词模板
- ✅ 更新visual-style-guide.md（从61行到303行）
- ✅ 添加4种内联图片类别模板
- ✅ 增强所有技能README文件

**Webflow发布器改进**
- ✅ 修复封面图上传（正确的markdown格式检测）
- ✅ 添加全宽图片样式（使用`!important`覆盖）
- ✅ 改进alt文本以提高可访问性

**代码质量**
- ✅ 创建共享`gemini_api.py`模块（DRY原则）
- ✅ 移除硬编码API密钥
- ✅ 添加完整.gitignore

---

## 🤝 贡献

欢迎贡献！请：

1. Fork本仓库
2. 创建特性分支（`git checkout -b feature/amazing-feature`）
3. 遵循现有代码风格和文档标准
4. 充分测试你的更改
5. 使用描述性消息提交
6. 推送到你的分支
7. 打开Pull Request

---

## 📄 许可证

本项目为私有项目。保留所有权利。

---

## 🔗 相关资源

- [Claude Code 文档](https://docs.anthropic.com)
- [Webflow API v2 文档](https://developers.webflow.com)
- [Gemini API 文档](https://ai.google.dev)
- [Linear 设计系统](https://linear.app)

---

## 📞 支持

遇到问题或疑问：
1. 查看各个技能的README文件
2. 查看examples/目录
3. 查阅visual-style-guide.md了解图片生成
4. 在GitHub上开issue

---

**用 ❤️ 打造，为高效内容创作和工作流自动化服务**
