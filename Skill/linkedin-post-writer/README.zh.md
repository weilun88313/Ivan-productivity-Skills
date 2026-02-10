[English](README.md) | [中文](README.zh.md)

---


# LinkedIn 帖子写作工具

> 将零散想法转化为引人入胜的 LinkedIn 帖子，配有 AI 生成的视觉效果

## 概述

**LinkedIn 帖子写作工具** 技能帮助你从零散的思绪或一般性话题创建专业、引人入胜的 LinkedIn 帖子。它结合了内容结构化专业知识和 AI 生成的图像，生成符合你个人品牌的即发即用帖子。

### 核心功能

- ✍️ **两种创作模式** - 从零散想法到完整帖子，或从话题到完整叙述
- 🎨 **AI 生成图片** - 专业的 16:9 或 1:1 图片，针对 LinkedIn 优化
- 📝 **基于模板** - 5 种经过验证的帖子结构，适用于不同内容类型
- 💡 **品牌一致性** - 保持平易近人、专业的语气
- 🎯 **最佳长度** - 300-800 字符，获得最大互动
- 🔄 **完整工作流** - 从构思到最终带图片的帖子

## 快速开始

### 前置要求

```bash
# 安装依赖
pip install requests

# 设置 Gemini API key
export GEMINI_API_KEY='your_api_key_here'

# 或者添加到 ~/.claude/lensmor_secrets.json
{
  "NANO_API_KEY": "your_api_key_here"
}
```

### 基本使用

**场景 1：从零散想法出发**

```
"帮我写一篇 LinkedIn 帖子。想法：
- AI 改变了产品设计工作流
- 对头脑风暴很有用
- 可以分析用户访谈
- 但不能完全依赖它"
```

**场景 2：从话题出发**

```
"写一篇关于团队协作的 LinkedIn 帖子"
```

**生成图片**

```bash
python scripts/generate_image.py \
  --prompt "Your post content or image description" \
  --aspect-ratio 16:9 \
  --output_dir output \
  --filename post_image
```

## 帖子结构

### 5 种模板类型

1. **个人故事 → 洞察**
   - 分享经验，提炼教训
   - 示例：让你学到东西的团队时刻

2. **观察 → 分析**
   - 注意到模式，提供解读
   - 示例：行业趋势分析

3. **问题 → 探索**
   - 提出问题，探索观点
   - 示例："产品经理应该懂代码吗？"

4. **技巧列表 → 价值传递**
   - 分享可执行的建议及背景
   - 示例："我在产品设计中使用 AI 的 3 种方式"

5. **反常观点 → 辩论**
   - 挑战假设，邀请讨论
   - 示例："不受欢迎的观点：MVP 已经过时了"

## 参考文件

- **`references/brand_persona.md`** - 完整的品牌语气和写作风格指南
- **`references/post_templates.md`** - 详细的帖子结构和示例
- **`scripts/generate_image.py`** - 图片生成工具
- **`scripts/gemini_api.py`** - 共享的 Gemini API 客户端

---

**愉快发帖！** 📝✨
