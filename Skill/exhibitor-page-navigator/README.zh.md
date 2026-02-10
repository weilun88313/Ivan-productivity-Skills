[English](README.md) | [中文](README.zh.md)

---


# 展商页面导航器

> 自动查找展会网站上的展商目录页面

## 概述

**展商页面导航器** 是一个工作流技能，帮助你在任何展会网站上定位展商目录页面。它使用智能导航策略和验证检查来找到展商列表的位置，而无需提取实际数据。

## 使用场景

- 🔍 **市场研究**：查找展商列表进行竞争分析
- 📊 **潜在客户开发**：定位行业活动中的潜在客户
- 🎯 **活动规划**：研究哪些公司参加特定展会
- 🌐 **网页爬取准备**：在数据提取前找到正确的 URL

## 快速开始

### 输入格式

提供展会主页 URL：

```
https://www.example-tradeshow.com
```

### 预期输出

包含目录 URL 和验证详情的 JSON 对象：

```json
{
  "status": "success",
  "homepage_url": "https://www.example-tradeshow.com",
  "found_directory_url": "https://www.example-tradeshow.com/exhibitors",
  "navigation_method": "Menu Click",
  "verification_reason": "Page has search bar, category filters, displays 200+ exhibitor cards",
  "confidence_level": "high"
}
```

## 工作原理

### 第一阶段：导航
1. 加载主页
2. 处理 cookie/隐私弹窗
3. 扫描导航菜单中的展商链接
4. 点击最相关的链接

### 第二阶段：后备策略
如果未找到菜单链接：
- **URL 猜测**：尝试常见路径，如 `/exhibitors`、`/directory`
- **站内搜索**：使用内置搜索查找"exhibitor list"
- **站点地图检查**：扫描 sitemap.xml 查找相关 URL

### 第三阶段：验证
确认页面是真正的展商目录：
- 检查搜索栏和过滤器
- 验证是否可见多个公司列表
- 确认页面标题包含"Exhibitor"或"Directory"
- 验证活动年份是当前/即将到来的

## 能找到什么

✅ **会找到：**
- 公开展商目录
- 参展公司列表
- 展商搜索页面
- 带展商列表的平面图

❌ **不会返回：**
- 登录/门户页面（"展商专区"）
- 销售页面（"成为展商"）
- 过往活动档案
- 仅赞助商列表

## 常见场景

### 场景 1：简单导航
**主页** → 菜单 → "Exhibitors" → **目录页面**

大多数展会在导航菜单中有明确的"Exhibitors"或"Exhibitor List"链接。

### 场景 2：隐藏在下拉菜单下
**主页** → "Attend"下拉菜单 → "Exhibitor Directory" → **目录页面**

许多网站将展商链接嵌套在"Attend"、"Visit"或"Visitors"部分下。

### 场景 3：URL 猜测
**主页** → 尝试 `/exhibitors` → **目录页面**

如果没有链接，技能会尝试常见的 URL 模式。

### 场景 4：外部平台
**主页** → "View Exhibitors" → **重定向到子域** → **目录页面**

一些展会将展商目录托管在独立平台或子域上。

## 置信度级别

| 级别 | 含义 | 示例 |
|------|------|------|
| **高** | 通过菜单找到 + 3+ 个指标 | 明确的"Exhibitor List"链接，有搜索/过滤/分页 |
| **中** | 通过 URL 猜测 + 2 个指标 | `/exhibitors` URL 有效，有公司卡片但无过滤器 |
| **低** | 通过后备方式 + 1 个指标 | 通过站点地图找到，最少的视觉指标 |

## 处理的边缘情况

### 1. 需要登录
```json
{
  "status": "failed",
  "verification_reason": "Directory requires login/registration"
}
```

### 2. 已归档的活动
技能会检查活动年份，如果检测到已归档的目录，会寻找"下一届"链接。

### 3. 多语言网站
如果可用，自动切换到英语，或尝试 `/en/` URL 路径。

### 4. 仅 PDF 列表
```json
{
  "status": "success",
  "found_directory_url": "https://example.com/exhibitors.pdf",
  "navigation_method": "Download Link",
  "confidence_level": "medium"
}
```

## 故障排除

### 问题："未找到展商链接"

**解决方案：**
1. 检查活动是否还未发布展商列表
2. 尝试手动访问 `/exhibitors` 或 `/directory`
3. 在网站上查找"即将推出"消息
4. 检查目录是否需要注册

### 问题："找到登录页面而不是目录"

**解决方案：**
1. 查找"以访客身份查看"或"公共目录"选项
2. 检查页脚中的备用链接
3. 尝试 URL 猜测绕过登录要求

## 最佳实践

### 对于用户

1. **提供干净的 URL**：使用主页 URL，而不是子页面
2. **检查时机**：目录可能不会提前很久发布
3. **验证结果**：始终手动检查返回的 URL
4. **处理失败**：有些展会确实不发布公共目录

### 对于开发者

1. **遵守 Robots.txt**：在自动爬取之前检查
2. **速率限制**：在请求之间添加延迟以避免被屏蔽
3. **缓存结果**：目录 URL 通常不经常更改
4. **处理重定向**：正确处理 301/302 重定向

## 限制

此技能：
- ❌ **不会**提取展商数据
- ❌ **不会**绕过登录要求
- ❌ **不会**爬取联系信息
- ✅ 仅**定位**目录 URL

要进行数据提取，在获取 URL 后需要额外的工具或脚本。

## 集成示例

### 与 Python 爬虫集成

```python
# 1. 使用此技能获取目录 URL
directory_url = "https://www.example.com/exhibitors"  # 来自技能输出

# 2. 然后爬取目录
import requests
from bs4 import BeautifulSoup

response = requests.get(directory_url)
soup = BeautifulSoup(response.content, 'html.parser')

# 提取展商数据...
exhibitors = soup.find_all('div', class_='exhibitor-card')
```

## 常见问题

**问：这能提取展商电子邮件地址吗？**
答：不能，此技能只查找 URL。你需要爬取工具进行数据提取。

**问：如果目录需要登录怎么办？**
答：技能将返回 `status: "failed"` 并附上解释。你需要凭据才能访问。

**问：URL 猜测的准确率如何？**
答：对于 `/exhibitors` 和 `/directory` 等常见模式，成功率约为 60-70%。

**问：它能处理非英语网站吗？**
答：可以，它会尝试切换到英语，或尝试适用于多种语言的常见 URL 模式。

## 版本历史

### v2.0.0 (2026-02-08)
- ✅ 增强了详细工作流的文档
- ✅ 在输出中添加了置信度级别
- ✅ 改进了边缘情况处理
- ✅ 添加了故障排除指南
- ✅ 结构化了后备策略
- ✅ 添加了实际示例

### v1.0.0 (2026-02-03)
- 初始发布，带基本导航工作流

## 支持

如有问题或疑问：
- 查看故障排除部分
- 检查 SKILL.md 了解详细工作流
- 提交问题时附上失败的展会 URL

---

**注意**：此技能设计用于具有网页浏览功能的 AI 助手。它提供了结构化方法，但需要通过浏览器自动化或网页爬虫库等工具执行。
