[English](README.md) | [中文](README.zh.md)

---

# LinkedIn 帖子撰写器

> 将零散的想法转化为引人入胜的 LinkedIn 帖子，并配以 AI 生成的视觉效果

## 概述

根据零散的想法或一般主题，创建专业、引人入胜的 LinkedIn 帖子。它将内容结构化与 AI 生成的图片相结合，生成可发布的帖子。

### 主要功能

- ✍️ **两种创作模式** - 从零散想法或主题开始
- 🎨 **AI 生成图片** - 专业的 16:9 或 1:1 图片
- 📝 **5 种成熟模板** - 适用于不同内容类型的帖子结构
- 💡 **品牌一致性** - 亲切、专业的语气
- 🎯 **最佳长度** - 300-800 字符，以实现最大互动

## 快速开始

### 先决条件

```bash
# 安装依赖
pip install requests

# 设置 Gemini API 密钥
export GEMINI_API_KEY='your_api_key_here'
```

### 使用方法

**从零散想法开始：**
```
"帮我写一篇 LinkedIn 帖子。想法：
- AI 改变产品设计工作流程
- 有助于头脑风暴
- 不能完全依赖它"
```

**从主题开始：**
```
"写一篇关于团队协作的 LinkedIn 帖子"
```

**生成图片：**
```bash
python scripts/generate_image.py \
  --prompt "你的帖子内容或描述" \
  --aspect-ratio 16:9 \
  --output_dir output
```

## 帖子模板

1.  **个人故事 → 洞察** - 分享经验，提炼教训
2.  **观察 → 分析** - 注意模式，提供解读
3.  **问题 → 探索** - 提出问题，探索视角
4.  **技巧列表 → 价值** - 分享可操作的建议
5.  **逆向观点 → 辩论** - 挑战假设，邀请讨论

## 资源

- **`references/brand_persona.md`** - 品牌语气指南
- **`references/post_templates.md`** - 帖子结构和示例
- **`scripts/generate_image.py`** - 图片生成工具

---

**发帖愉快！** 📝✨