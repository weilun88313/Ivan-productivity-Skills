[English](README.md) | [中文](README.zh.md)

---

# 关键词研究

发现并优先排序用于SEO和GEO内容策略的关键词。根据搜索意图分析和竞争评估，生成可操作的文章主题建议。

## 主要功能

- **种子关键词头脑风暴**，涵盖核心术语、问题、解决方案、比较和疑问
- **意图分类**：信息性、商业性、交易性
- **真实数据驱动的竞争评估**（使用 Ahrefs API）
- **GEO机会识别**，用于AI引用潜力
- **主题聚类**，用于建立主题权威性

## 快速开始

```
Research keywords for [topic/product/service]
```

```
Find keyword opportunities for [industry] targeting [audience]
```

此技能输出一个包含文章主题、目标关键词、意图分类和竞争估计的优先排序表格。

## Ahrefs 集成

**此技能使用 Ahrefs MCP** 提供真实的关键词数据：
- ✅ 准确的月度搜索量
- ✅ 关键词难度（KD）评分 0-100
- ✅ 流量潜力估算
- ✅ SERP 分析

**要求**：Ahrefs API v3 访问权限（标准套餐 $249/月包含 500 次免费查询/月）

## 相关技能

| 技能 | 用途 |
|-------|---------|
| [content-pipeline](../content-pipeline/) | 完整的自动化工作流程（推荐） |
| [blog-writer](../blog-writer/) | 撰写文章 |
| [webflow-blog-publisher](../webflow-blog-publisher/) | 发布到Webflow |