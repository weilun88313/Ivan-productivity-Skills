[English](README.md) | [中文](README.zh.md)

---

# 50k 潜在客户生成系统

> 结合 Apollo.io、Google Search 和 LinkedIn 抓取的完整 B2B 潜在客户生成机器

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 概述

自动化 B2B 潜在客户生成系统，结合多个数据源（Apollo.io、Google Search、LinkedIn）与 AI 驱动的个性化功能，大规模生成和筛选潜在客户。使用 n8n 工作流自动化和 Airtable 数据库管理构建。

### 关键特性

- 🎯 **多源抓取** - Apollo.io、Google Search、LinkedIn 数据提取
- 🤖 **AI 驱动个性化** - 自动化外联消息生成
- 📊 **潜在客户筛选** - 自动评分和过滤
- 🔄 **工作流自动化** - 基于 n8n 的管道编排
- 📁 **数据管理** - Airtable 集成提供 CRM 功能
- ⚡ **可扩展** - 生成多达 50,000 个合格潜在客户

## 快速开始

### 先决条件

```bash
# 安装依赖
pip install -r requirements.txt

# 配置 API 密钥 — 添加到仓库根目录的 .env：
#   APOLLO_API_KEY=your_apollo_key
#   LINKEDIN_COOKIE=your_linkedin_session
#   OPENAI_API_KEY=your_openai_key
```

### 使用方法

**基本工作流：**
```
Run the 50k lead generation system for [target industry/role]
```

**带参数：**
```bash
python scripts/wrapper.py \
  --industry "SaaS" \
  --role "CTO" \
  --company-size "50-200" \
  --limit 1000
```

## 工作原理

1. **数据收集** - 从 Apollo.io、Google Search 和 LinkedIn 抓取潜在客户
2. **数据丰富** - 交叉引用多个来源的数据
3. **资格筛选** - 基于自定义标准对潜在客户评分
4. **个性化** - 生成 AI 驱动的外联消息
5. **存储** - 将合格潜在客户存储到 Airtable CRM

## 配置

**必需：**
- Apollo.io API key
- LinkedIn session cookie
- OpenAI API key（用于个性化）

**可选：**
- Airtable base ID
- 自定义潜在客户评分规则
- 外联模板

## 输出格式

潜在客户存储在 Airtable 中，包含字段：
- 公司名称
- 联系人姓名和职位
- 电子邮件地址
- 潜在客户评分
- 个性化外联消息
- 来源归属

## 相关技能

| Skill | 用途 |
|-------|---------|
| [keyword-research](../keyword-research/) | 研究目标市场 |
| [content-pipeline](../content-pipeline/) | 完整内容自动化 |

## 故障排除

### Apollo.io 速率限制

- 在 API 调用之间实现延迟
- 如有可用，使用多个 API 密钥
- 缓存结果以避免重复调用

### LinkedIn 抓取被阻止

- 轮换 user agents
- 使用住宅代理
- 遵守速率限制

### 潜在客户质量低

- 优化筛选标准
- 调整评分权重
- 按公司规模、行业、地点过滤

## 文件结构

```
50k-lead-generation-system/
├── README.md              # 本文件
├── SKILL.md               # AI 指令
├── scripts/
│   └── wrapper.py         # Python 包装器
└── workflows/
    └── lead-gen-n8n.json  # n8n 工作流
```

## 资源

- [原始仓库](https://github.com/Awaisali36/50k-lead-generation-system)
- [n8n 文档](https://docs.n8n.io/)
- [Apollo.io API](https://docs.apollo.io/)

---

**大规模生成潜在客户！** 🚀📊
