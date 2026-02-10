[English](README.md) | [中文](README.zh.md)

---

# 参展商页面导航器

> 自动查找展会网站上的参展商名录页面

## 概述

一种工作流技能，通过智能导航策略和验证检查，在展会网站上定位参展商名录页面。

## 用例

- 🔍 **市场研究** - 查找参展商列表进行竞品分析
- 📊 **潜在客户开发** - 在行业活动中定位潜在客户
- 🎯 **活动策划** - 研究公司参与情况
- 🌐 **网络爬虫准备** - 在数据提取前找到正确的URL

## 快速开始

### 输入

提供一个展会主页URL：
```
https://www.example-tradeshow.com
```

### 输出

包含名录URL和验证信息的JSON：

```json
{
  "status": "success",
  "found_directory_url": "https://www.example-tradeshow.com/exhibitors",
  "navigation_method": "Menu Click",
  "verification_reason": "Page has search bar, filters, 200+ exhibitor cards",
  "confidence_level": "high"
}
```

## 工作原理

1.  **导航** - 加载主页，处理弹窗，扫描菜单，点击参展商链接
2.  **回退策略** - URL猜测（`/exhibitors`，`/directory`），站点搜索，站点地图检查
3.  **验证** - 通过搜索栏、筛选器、公司列表、页面标题验证进行确认

## 它能找到什么

✅ **将找到：**
- 公开的参展商名录
- 参展公司列表
- 参展商搜索页面
- 带有列表的平面图

❌ **不会返回：**
- 登录/门户页面
- 销售页面
- 往届活动存档
- 仅限赞助商的列表

## 置信水平

| Level | Meaning |
|-------|---------|
| **高** | 菜单链接 + 3个以上指标（搜索/筛选器/分页） |
| **中** | URL猜测 + 2个指标（有卡片但无筛选器） |
| **低** | 回退方法 + 1个指标 |

## 边缘情况

-   **需要登录** - 返回失败状态并附带原因
-   **已存档活动** - 检查年份，查找“下一届”链接
-   **多语言** - 切换到英语或尝试`/en/`路径
-   **PDF列表** - 返回PDF URL，置信水平为中等

## 故障排除

-   **未找到链接** - 检查列表是否已发布，手动尝试`/exhibitors`，查找“即将推出”
-   **返回登录页面** - 查找“以访客身份查看”或公共名录选项
-   **显示往届活动** - 检查年份选择下拉菜单或“下一届”链接

## 局限性

-   仅定位名录URL（不提取数据）
-   无法绕过登录要求
-   不抓取联系信息

## 集成示例

```python
# Get URL from skill output
directory_url = "https://www.example.com/exhibitors"

# Then scrape with your preferred tool
import requests
from bs4 import BeautifulSoup

response = requests.get(directory_url)
soup = BeautifulSoup(response.content, 'html.parser')
exhibitors = soup.find_all('div', class_='exhibitor-card')
```

## 常见问题

**问：这能提取参展商数据吗？**
答：不能，它只查找URL。请使用爬虫工具进行提取。

**问：如果需要登录怎么办？**
答：将返回`status: "failed"`并附带解释。

**问：URL猜测的准确性如何？**
答：对于常见模式，成功率约为60-70%。

---

**注意**：需要具备网页浏览能力的AI助手。为浏览器自动化或网络爬虫工具提供结构化方法。