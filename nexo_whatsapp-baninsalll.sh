#!/data/data/com.termux/files/usr/bin/bash

# --- NEXO-TECH COLORS ---
G='\033[92m'; Y='\033[93m'; C='\033[96m'; R='\033[91m'; W='\033[0m'

echo -e "${C}  _   _  _______   _____    _____ ______ _____ _    _ "
echo -e " | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |"
echo -e " |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |"
echo -e " | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |"
echo -e " | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |"
echo -e " |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_${W}"
echo -e "${G}=======================================================${W}"
echo -e "${Y}[!] TERMUX NON-ROOT INSTALLER: NEXO-TECH v16.0${W}"
echo -e "${G}=======================================================${W}"

# 1. Update Packages
echo -e "\n${C}[*] Updating Termux Repositories...${W}"
pkg update -y && pkg upgrade -y

# 2. Install Python & Basic Tools
echo -e "${C}[*] Installing Python, Nano, and Requests...${W}"
pkg install -y python nano ncurses-utils

# 3. Install Python Modules
echo -e "${C}[*] Installing Flask and Requests for Gmail Gen...${W}"
pip install requests flask

# 4. Create Database File
touch nexo_database.txt
chmod 777 nexo_database.txt

echo -e "\n${G}=======================================================${W}"
echo -e "${G}[+] INSTALLATION SUCCESSFUL!${W}"
echo -e "${Y}[*] STEPS TO RUN:${W}"
echo -e "    1. Save your code as: ${C}nexo_master.py${W}"
echo -e "    2. Run the tool:      ${G}python nexo_master.py${W}"
echo -e "${G}=======================================================${W}"
