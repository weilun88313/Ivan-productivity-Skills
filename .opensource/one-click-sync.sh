#!/bin/bash
# 一键同步到公开仓库（包含安全检查）
# 用法: ./one-click-sync.sh "commit message"

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PRIVATE_REPO="$(dirname "$SCRIPT_DIR")"
PUBLIC_REPO="/Users/ivan/Documents/Ivan_Skills_Public"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# 1. 运行同步脚本
echo -e "${GREEN}🚀 步骤 1/3: 同步代码...${NC}"
bash "$SCRIPT_DIR/sync-to-public.sh" "$1"

# 2. 运行安全检查
echo -e "\n${GREEN}🔍 步骤 2/3: 安全检查...${NC}"
bash "$SCRIPT_DIR/check-sensitive-info.sh" "$PUBLIC_REPO"

if [ $? -ne 0 ]; then
    echo -e "${YELLOW}⚠️  发现安全问题，已终止推送${NC}"
    exit 1
fi

# 3. 推送到公开仓库
echo -e "\n${GREEN}📤 步骤 3/3: 推送到公开仓库...${NC}"
cd "$PUBLIC_REPO"

# 检查是否有remote origin
if ! git remote get-url origin >/dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  未配置公开仓库remote，请先运行:${NC}"
    echo -e "   cd $PUBLIC_REPO"
    echo -e "   git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO.git"
    exit 1
fi

# 显示即将推送的变更
echo -e "\n${YELLOW}即将推送以下变更:${NC}"
git log origin/main..HEAD --oneline 2>/dev/null || git log --oneline -5

# 确认推送
read -p "确认推送到公开仓库？(y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git push origin main
    echo -e "\n${GREEN}✅ 同步完成！${NC}"
    echo -e "${GREEN}公开仓库已更新: $(git remote get-url origin)${NC}"
else
    echo -e "${YELLOW}已取消推送${NC}"
fi
