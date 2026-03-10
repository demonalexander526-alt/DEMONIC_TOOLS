#!/data/data/com.termux/files/usr/bin/bash

# --- NEXO-TECH COLORS ---
G='\033[92m'; Y='\033[93m'; C='\033[96m'; R='\033[91m'; W='\033[0m'

# --- THE BANNER ---
echo -e "${C}"
echo "  _   _  _______   _____    _____ ______ _____ _    _ "
echo " | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |"
echo " |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |"
echo " | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |"
echo " | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |"
echo " |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|"
echo -e "${G}=======================================================${W}"
echo -e "${Y}[!] NEXO-TECH SHELL DEPLOYMENT: VERSION 17.0${W}"
echo -e "${G}=======================================================${W}"

# 1. Update and Upgrade Termux
echo -e "\n${C}[*] Synchronizing Repositories...${W}"
pkg update -y && pkg upgrade -y

# 2. Install Essential Tools
echo -e "${C}[*] Installing Python, Nano, and Git...${W}"
pkg install -y python nano git curl

# 3. Install Python Dependencies
echo -e "${C}[*] Installing Flask and Requests...${W}"
pip install flask requests

# 4. Initialize Database
echo -e "${C}[*] Creating NEXO Database...${W}"
touch nexo_database.txt
chmod 600 nexo_database.txt

# 5. Finalize
echo -e "\n${G}=======================================================${W}"
echo -e "${G}[+] SYSTEM READY!${W}"
echo -e "${Y}[*] COMMANDS TO START:${W}"
echo -e "    1. Launch Gmail Gen: ${C}python nexo-gmail_creator.py${W}"
echo -e "    2. Launch Master UI: ${C}python nexo_master.py${W}"
echo -e "${G}=======================================================${W}"
