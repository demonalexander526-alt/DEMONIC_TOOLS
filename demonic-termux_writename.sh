
#!/bin/bash
# ==========================================
# TOOL NAME : DEMONIC NAMER
# CREATED BY: 😈 DEMON ALEX 😈
# ==========================================


USERNAME="DEMONIC"  
RESET="\e[0m"
MAGENTA="\e[35m"
CYAN="\e[36m"
GREEN='\e[32m'
command -v figlet >/dev/null 2>&1 || { echo -e "${CYAN}Installing figlet...${RESET}"; pkg install figlet -y; }
command -v toilet >/dev/null 2>&1 || { echo -e "${CYAN}Installing toilet...${RESET}"; pkg install toilet -y; }
command -v termux-notification >/dev/null 2>&1 || { echo -e "${CYAN}Installing termux-api...${RESET}"; pkg install termux-api -y; }

clear


toilet -f mono12 -F gay "$USERNAME"


echo -e "${GREEN}"
figlet -f big "$USERNAME"
echo -e "${RESET}"


echo -e "${CYAN}🔥 DEMONIC DIRECTORY ACTIVE 🔥${RESET}"
echo -e "${CYAN}CREATED BY DEMON ALEX${RESET}"
echo ""

termux-notification \
  --title "DEMONIC NAMER 😈🔥✅" \
  --content "$USERNAME is ACTIVE" \
  --priority high \
  --sound default

