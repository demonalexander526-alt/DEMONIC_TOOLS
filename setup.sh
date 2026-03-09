#!/bin/bash
# NEXO-TECH AUTOMATED INSTALLER

# Colors for professional look
G='\033[92m'
Y='\033[93m'
R='\033[91m'
W='\033[0m'

echo -e "${G}[+] NEXO-TECH: STARTING SYSTEM CHECK...${W}"

# 1. Update System & Install Python
sudo apt update -y
sudo apt install python3 python3-pip curl wget -y

# 2. Install Flask (The Engine)
echo -e "${G}[+] INSTALLING ENGINE DEPENDENCIES...${W}"
pip3 install flask --break-system-packages

# 3. Install Cloudflared (The Tunnel)
if ! command -v cloudflared &> /dev/null; then
    echo -e "${Y}[!] CLOUDFLARED NOT FOUND. INSTALLING...${W}"
    wget https://github.com -O cloudflared
    chmod +x cloudflared
    sudo mv cloudflared /usr/local/bin/
fi

echo -e "${G}[SUCCESS] NEXO-TECH IS READY.${W}"
echo -e "${Y}[*] Run 'python3 nexo_pro.py' to start the engine.${W}"
