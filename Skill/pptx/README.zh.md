[English](README.md) | [中文](README.zh.md)

---


# PPTX Skill

> 使用 Python python-pptx 库创建和编辑 PowerPoint 演示文稿

## 概述

**PPTX Skill** 提供使用 `python-pptx` 库以编程方式创建、修改和操作 PowerPoint (.pptx) 文件的全面指南和示例。

### 核心功能

- 📊 **演示文稿创建** - 从头创建新的 PowerPoint 文件
- 🎨 **幻灯片操作** - 添加、删除和重新排列幻灯片
- 📝 **内容添加** - 文本、图片、图表、表格、形状
- 🎯 **布局管理** - 使用预定义布局和母版
- 💾 **文件操作** - 保存、加载和修改现有演示文稿

## 快速开始

### 安装

```bash
pip install python-pptx
```

### 基本使用

```python
from pptx import Presentation

# 创建新演示文稿
prs = Presentation()

# 添加标题幻灯片
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)

# 设置标题和副标题
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "Hello, World!"
subtitle.text = "python-pptx 演示"

# 保存演示文稿
prs.save('presentation.pptx')
```

## 常见操作

### 1. 创建幻灯片

```python
# 标题幻灯片
title_slide = prs.slides.add_slide(prs.slide_layouts[0])

# 标题和内容
content_slide = prs.slides.add_slide(prs.slide_layouts[1])

# 空白幻灯片
blank_slide = prs.slides.add_slide(prs.slide_layouts[6])
```

### 2. 添加文本

```python
# 添加文本框
from pptx.util import Inches
left = top = Inches(1)
width = height = Inches(3)

textbox = slide.shapes.add_textbox(left, top, width, height)
text_frame = textbox.text_frame
text_frame.text = "这是一个文本框"
```

### 3. 添加图片

```python
from pptx.util import Inches

img_path = 'image.png'
left = Inches(1)
top = Inches(2)
pic = slide.shapes.add_picture(img_path, left, top)
```

### 4. 添加表格

```python
from pptx.util import Inches

rows, cols = 3, 3
left = top = Inches(2)
width = Inches(6)
height = Inches(2)

table = slide.shapes.add_table(rows, cols, left, top, width, height).table

# 设置单元格值
table.cell(0, 0).text = '标题1'
table.cell(0, 1).text = '标题2'
```

### 5. 添加图表

```python
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches

# 定义图表数据
chart_data = CategoryChartData()
chart_data.categories = ['Q1', 'Q2', 'Q3', 'Q4']
chart_data.add_series('销售额', (10, 15, 20, 25))

# 添加图表
x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)
chart = slide.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data
).chart
```

## 高级功能

### 格式化文本

```python
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN

# 访问文本框架
text_frame = shape.text_frame

# 添加段落
p = text_frame.add_paragraph()
p.text = "格式化文本"
p.font.bold = True
p.font.size = Pt(24)
p.alignment = PP_ALIGN.CENTER
```

### 使用母版和布局

```python
# 列出所有可用布局
for layout in prs.slide_layouts:
    print(f"{layout.name}: {layout.slide_layout_id}")

# 使用特定布局
custom_layout = prs.slide_layouts[5]  # 标题和内容
slide = prs.slides.add_slide(custom_layout)
```

### 操作现有演示文稿

```python
# 打开现有文件
prs = Presentation('existing.pptx')

# 遍历幻灯片
for slide in prs.slides:
    for shape in slide.shapes:
        if hasattr(shape, "text"):
            print(shape.text)

# 保存修改
prs.save('modified.pptx')
```

## 资源

- [SKILL.md](SKILL.md) - 详细的 AI 指令和示例
- [python-pptx 文档](https://python-pptx.readthedocs.io/) - 官方文档

## 故障排除

### 常见问题

**问：如何更改幻灯片大小？**
```python
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)
```

**问：如何添加备注？**
```python
notes_slide = slide.notes_slide
text_frame = notes_slide.notes_text_frame
text_frame.text = "这是备注"
```

**问：如何删除幻灯片？**
```python
from pptx import Presentation

prs = Presentation('presentation.pptx')
# 通过索引删除幻灯片
rId = prs.slides._sldIdLst[2].rId
prs.part.drop_rel(rId)
del prs.slides._sldIdLst[2]
```

## 最佳实践

1. **使用布局**：利用预定义布局保持一致性
2. **测量单位**：始终使用 `Inches()` 或 `Pt()` 以保持一致
3. **错误处理**：处理缺失的图片文件和无效数据
4. **性能**：对于大型演示文稿，分批处理幻灯片
5. **版本控制**：在修改之前备份原始文件

## 支持

如有问题或疑问：
1. 查看 [python-pptx 文档](https://python-pptx.readthedocs.io/)
2. 检查 SKILL.md 了解更多示例
3. 搜索 GitHub Issues 查找已知问题

---

**创建精彩演示文稿！** 📊✨
