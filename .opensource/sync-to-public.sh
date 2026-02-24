#!/bin/bash
# 自动同步私有仓库到公开仓库，并清理品牌信息
# 用法: ./sync-to-public.sh [commit-message]

set -e

PRIVATE_REPO="/Users/ivan/Documents/Ivan_Skills"
PUBLIC_REPO="/Users/ivan/Documents/Ivan_Skills_Public"
BRAND_CONFIG="$PRIVATE_REPO/.opensource/brand-config.json"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 开始同步到公开仓库...${NC}"

# 1. 检查公开仓库是否存在
if [ ! -d "$PUBLIC_REPO" ]; then
    echo -e "${YELLOW}⚠️  公开仓库不存在，正在克隆...${NC}"
    cd "$(dirname "$PUBLIC_REPO")"
    git clone "$PRIVATE_REPO" "$PUBLIC_REPO"
    cd "$PUBLIC_REPO"
    git remote rename origin private
    # 这里需要手动添加公开仓库的remote
    echo -e "${YELLOW}请手动添加公开仓库remote: git remote add origin <public-repo-url>${NC}"
fi

# 2. 同步最新代码
echo -e "${GREEN}📥 拉取私有仓库最新代码...${NC}"
cd "$PUBLIC_REPO"
git fetch private
git merge private/main --no-edit || {
    echo -e "${RED}❌ 合并冲突，请手动解决${NC}"
    exit 1
}

# 2.1 删除不应该公开的目录
echo -e "${GREEN}🗑️  删除不应公开的内容...${NC}"
rm -rf "$PUBLIC_REPO/Skill/brand-guidelines"
rm -rf "$PUBLIC_REPO/Skill/*/output"
rm -rf "$PUBLIC_REPO/Skill/linkedin-post-writer/output"

# 3. 执行品牌信息清理
echo -e "${GREEN}🧹 清理品牌信息...${NC}"

# 3.1 替换品牌名称
find . -type f \( -name "*.md" -o -name "*.py" \) \
    ! -path "./.git/*" \
    ! -path "./.opensource/*" \
    -exec sed -i '' 's/Lensmor/MyCompany/g' {} +

find . -type f \( -name "*.md" -o -name "*.py" \) \
    ! -path "./.git/*" \
    ! -path "./.opensource/*" \
    -exec sed -i '' 's/lensmor/mycompany/g' {} +

# 3.2 替换secrets路径
find . -type f \( -name "*.md" -o -name "*.py" \) \
    ! -path "./.git/*" \
    -exec sed -i '' 's/lensmor_secrets\.json/secrets\.json/g' {} +

# 3.3 匿名化作者信息
cat > "$PUBLIC_REPO/Skill/webflow-blog-publisher/assets/writers/writers.json" << 'EOF'
[
  {
    "name": "Author Name",
    "image_url": "https://example.com/author.jpg"
  },
  {
    "name": "Guest Writer",
    "image_url": "https://example.com/guest.jpg"
  }
]
EOF

# 3.4 更新许可证声明
sed -i '' 's/本项目为私有项目。保留所有权利。/本项目采用 MIT 许可证。/g' README.zh-CN.md
sed -i '' 's/Private project\. All rights reserved\./This project is licensed under the MIT License\./g' README.md

# 3.5 添加LICENSE文件
if [ -f "$PRIVATE_REPO/.opensource/MIT-LICENSE.txt" ]; then
    echo -e "${GREEN}📄 添加MIT许可证文件...${NC}"
    cp "$PRIVATE_REPO/.opensource/MIT-LICENSE.txt" "$PUBLIC_REPO/LICENSE"
fi

# 4. 移除.opensource目录（仅用于私有仓库）
if [ -d "$PUBLIC_REPO/.opensource" ]; then
    echo -e "${GREEN}🗑️  移除.opensource目录...${NC}"
    rm -rf "$PUBLIC_REPO/.opensource"
fi

# 确保.gitignore排除.opensource
if ! grep -q "^\.opensource/" "$PUBLIC_REPO/.gitignore" 2>/dev/null; then
    echo -e "${GREEN}📝 更新.gitignore...${NC}"
    echo "" >> "$PUBLIC_REPO/.gitignore"
    echo "# Sync tools (only for private repo)" >> "$PUBLIC_REPO/.gitignore"
    echo ".opensource/" >> "$PUBLIC_REPO/.gitignore"
fi

# 5. 添加开源说明文件
cat > "$PUBLIC_REPO/CONTRIBUTING.md" << 'EOF'
# Contributing Guidelines

Thank you for considering contributing to this project!

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Code Style

- Follow existing code patterns
- Add comments for complex logic
- Update documentation when needed

## Testing

- Test your changes thoroughly before submitting
- Provide example usage if adding new features
EOF

# 6. 检查变更
echo -e "${GREEN}📊 变更摘要:${NC}"
git status --short

# 7. 提交变更
COMMIT_MSG="${1:-Sync from private repo and sanitize brand info}"
echo -e "${GREEN}💾 提交变更: $COMMIT_MSG${NC}"
git add -A
git commit -m "$COMMIT_MSG" || echo "没有变更需要提交"

# 8. 推送到公开仓库（需要手动确认）
echo -e "${YELLOW}准备推送到公开仓库...${NC}"
echo -e "${YELLOW}请检查变更是否正确，然后运行: cd $PUBLIC_REPO && git push origin main${NC}"

echo -e "${GREEN}✅ 同步完成！${NC}"
echo -e "${GREEN}下一步：${NC}"
echo -e "  1. cd $PUBLIC_REPO"
echo -e "  2. 检查变更: git diff HEAD~1"
echo -e "  3. 推送: git push origin main"
