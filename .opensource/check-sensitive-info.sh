#!/bin/bash
# 检查公开仓库是否包含敏感信息
# 用法: ./check-sensitive-info.sh [path-to-public-repo]

PUBLIC_REPO="${1:-/Users/ivan/Documents/Ivan_Skills_Public}"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}🔍 检查敏感信息...${NC}\n"

ISSUES_FOUND=0

# 1. 检查品牌名称
echo -e "${YELLOW}1. 检查品牌名称泄露...${NC}"
if grep -r "Lensmor" "$PUBLIC_REPO" --exclude-dir=.git --exclude-dir=.opensource 2>/dev/null; then
    echo -e "${RED}❌ 发现 'Lensmor' 引用${NC}"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
else
    echo -e "${GREEN}✓ 未发现品牌名称${NC}"
fi

# 2. 检查API密钥模式
echo -e "\n${YELLOW}2. 检查API密钥泄露...${NC}"
if grep -rE "(AIza[0-9A-Za-z\\-_]{35}|sk-[a-zA-Z0-9]{48})" "$PUBLIC_REPO" --exclude-dir=.git 2>/dev/null; then
    echo -e "${RED}❌ 发现疑似API密钥${NC}"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
else
    echo -e "${GREEN}✓ 未发现API密钥${NC}"
fi

# 3. 检查真实作者信息
echo -e "\n${YELLOW}3. 检查真实姓名...${NC}"
if grep -rE "(Ivan|Kelvin)" "$PUBLIC_REPO/Skill/webflow-blog-publisher/assets/writers/" 2>/dev/null; then
    echo -e "${RED}❌ 发现真实姓名${NC}"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
else
    echo -e "${GREEN}✓ 作者信息已匿名化${NC}"
fi

# 4. 检查Webflow CDN链接（可能暴露网站）
echo -e "\n${YELLOW}4. 检查Webflow CDN链接...${NC}"
if grep -r "cdn.prod.website-files.com/691bdb22805dbb6a57758d15" "$PUBLIC_REPO" 2>/dev/null; then
    echo -e "${RED}❌ 发现真实Webflow CDN链接${NC}"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
else
    echo -e "${GREEN}✓ 未发现真实CDN链接${NC}"
fi

# 5. 检查私有项目声明
echo -e "\n${YELLOW}5. 检查许可证声明...${NC}"
if grep -r "Private project\|私有项目" "$PUBLIC_REPO/README"*.md 2>/dev/null; then
    echo -e "${RED}❌ 仍标记为私有项目${NC}"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
else
    echo -e "${GREEN}✓ 许可证已更新${NC}"
fi

# 6. 检查workspace目录
echo -e "\n${YELLOW}6. 检查workspace目录...${NC}"
if [ -d "$PUBLIC_REPO/workspace" ] && [ "$(ls -A "$PUBLIC_REPO/workspace" 2>/dev/null)" ]; then
    echo -e "${RED}❌ workspace目录未被忽略${NC}"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
else
    echo -e "${GREEN}✓ workspace目录已忽略${NC}"
fi

# 7. 检查secrets文件
echo -e "\n${YELLOW}7. 检查secrets文件...${NC}"
if find "$PUBLIC_REPO" -name "*secret*" -o -name "*.env" 2>/dev/null | grep -v ".gitignore" | grep -v ".opensource"; then
    echo -e "${RED}❌ 发现secrets文件${NC}"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
else
    echo -e "${GREEN}✓ 未发现secrets文件${NC}"
fi

# 总结
echo -e "\n${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
if [ $ISSUES_FOUND -eq 0 ]; then
    echo -e "${GREEN}✅ 检查通过！未发现敏感信息${NC}"
    echo -e "${GREEN}可以安全推送到公开仓库${NC}"
    exit 0
else
    echo -e "${RED}❌ 发现 $ISSUES_FOUND 个问题${NC}"
    echo -e "${YELLOW}请修复后再推送到公开仓库${NC}"
    exit 1
fi
