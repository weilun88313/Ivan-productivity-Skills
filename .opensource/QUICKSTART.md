# 快速开始：开源同步系统

## 🎯 目标
维护两个仓库：
- **Ivan_Skills** (私有) - 日常工作用，包含真实品牌信息
- **Ivan_Skills_Public** (公开) - 开源分享，自动清理敏感信息

## 📋 5分钟设置指南

### 步骤1: 赋予脚本执行权限
```bash
cd /Users/ivan/Documents/Ivan_Skills
chmod +x .opensource/*.sh
```

### 步骤2: 创建公开仓库
1. 访问 https://github.com/new
2. 仓库名: `claude-code-skills` (或你喜欢的名字)
3. 设置为 **Public**
4. 不要初始化README (我们会推送现有代码)

### 步骤3: 克隆并设置公开仓库
```bash
# 克隆私有仓库到新目录
cd ~/Documents
cp -r Ivan_Skills Ivan_Skills_Public

# 进入公开仓库目录
cd Ivan_Skills_Public

# 重命名原remote为private (用于拉取更新)
git remote rename origin private

# 添加GitHub公开仓库remote
git remote add origin git@github.com:YOUR_USERNAME/claude-code-skills.git

# 检查remotes配置
git remote -v
# 应该看到:
# origin    git@github.com:YOUR_USERNAME/claude-code-skills.git (fetch)
# origin    git@github.com:YOUR_USERNAME/claude-code-skills.git (push)
# private   /Users/ivan/Documents/Ivan_Skills (fetch)
# private   /Users/ivan/Documents/Ivan_Skills (push)
```

### 步骤4: 首次同步
```bash
cd /Users/ivan/Documents/Ivan_Skills

# 运行一键同步脚本
./.opensource/one-click-sync.sh "Initial open source release"

# 脚本会自动:
# ✓ 同步代码
# ✓ 清理品牌信息
# ✓ 运行安全检查
# ✓ 询问是否推送
```

### 步骤5: 验证
访问你的GitHub仓库，确认：
- [ ] 代码已上传
- [ ] README中没有"Lensmor"字样
- [ ] 作者信息已匿名化
- [ ] 许可证显示为MIT

## 🔄 日常使用

### 场景1: 添加新功能后同步

```bash
# 1. 在私有仓库正常开发
cd /Users/ivan/Documents/Ivan_Skills
# ... 修改代码 ...
git add .
git commit -m "Add new skill: product-hunt-monitor"
git push

# 2. 一键同步到公开仓库
./.opensource/one-click-sync.sh "Add product-hunt-monitor skill"

# 完成！公开仓库已自动更新并清理敏感信息
```

### 场景2: 只运行安全检查

```bash
# 检查公开仓库是否有敏感信息泄露
./.opensource/check-sensitive-info.sh

# 如果发现问题，手动修复后再推送
```

### 场景3: 手动同步（不自动推送）

```bash
# 只同步和清理，不推送
./.opensource/sync-to-public.sh "Update documentation"

# 手动检查变更
cd ~/Documents/Ivan_Skills_Public
git diff HEAD~1

# 满意后手动推送
git push origin main
```

## 📊 同步的内容

### ✅ 会自动清理
- `Lensmor` → `MyCompany`
- 真实作者姓名 → `Author Name`
- Webflow CDN链接 → `example.com`
- "私有项目" → "MIT许可证"
- `.opensource/` 目录被移除

### ❌ 不会同步
- `workspace/` 目录 (被.gitignore排除)
- `*_secrets.json` 文件
- `.env` 文件
- `.DS_Store` 等系统文件

## 🛡️ 安全提示

1. **永远在私有仓库工作** - 不要直接修改公开仓库
2. **推送前检查** - 使用 `check-sensitive-info.sh` 验证
3. **选择性同步** - 如果某个commit包含敏感内容，暂时不同步
4. **定期审查** - 每月检查一次公开仓库，确保没有信息泄露

## ❓ 常见问题

### Q1: 如果不小心推送了敏感信息怎么办？
```bash
# 立即删除公开仓库的commit
cd ~/Documents/Ivan_Skills_Public
git revert HEAD
git push origin main -f

# 或者联系GitHub支持删除历史记录
```

### Q2: 可以只同步特定的Skills吗？
可以。修改 `sync-to-public.sh` 添加过滤逻辑，或使用 `cherry-pick`:
```bash
cd ~/Documents/Ivan_Skills_Public
git cherry-pick <commit-hash>
# 然后运行清理命令
```

### Q3: 同步脚本会修改私有仓库吗？
**不会**。所有修改只发生在 `Ivan_Skills_Public`，私有仓库100%安全。

## 🎓 工作流程最佳实践

```
┌─────────────────────────────────────────────┐
│              你的工作习惯                     │
├─────────────────────────────────────────────┤
│  周一-周五                                   │
│    • 在私有仓库开发                          │
│    • 使用真实品牌信息                        │
│    • 正常commit & push                      │
│                                              │
│  周五/月末                                   │
│    • 运行 one-click-sync.sh                 │
│    • 同步到公开仓库                          │
│    • 分享给开源社区                          │
└─────────────────────────────────────────────┘
```

## 🔗 相关文件

- `sync-to-public.sh` - 主同步脚本
- `check-sensitive-info.sh` - 安全检查脚本
- `one-click-sync.sh` - 一键同步（推荐）
- `brand-config.json` - 替换规则配置
- `README.md` - 完整文档

---

**准备好了吗？运行你的第一次同步：**
```bash
./.opensource/one-click-sync.sh "My first sync"
```
