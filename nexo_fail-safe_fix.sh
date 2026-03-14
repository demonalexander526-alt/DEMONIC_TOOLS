#!/bin/bash

# NEXO-TECH V8.0 BLACKOUT - SYSTEM PREPARATION SCRIPT
# This script installs ngrok and required Python libraries for Kali Linux

G='\033[92m'
Y='\033[93m'
C='\033[96m'
R='\033[91m'
W='\033[0m'

clear
echo -e "${R}=======================================================${W}"
echo -e "${C}       NEXO-TECH V8.0 SYSTEM INITIALIZER               ${W}"
echo -e "${R}=======================================================${W}"

# 1. Update and Install Python Dependencies
echo -e "${Y}[*] Installing Python dependencies...${W}"
pip3 install flask requests phonenumbers --break-system-packages

# 2. Install Ngrok
echo -e "${Y}[*] Checking for Ngrok installation...${W}"
if ! command -v ngrok &> /dev/null
then
    echo -e "${R}[!] Ngrok not found. Installing via official repository...${W}"
    curl -s https://ngrok-agent.s3.amazonaws.com | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
    echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
    sudo apt update && sudo apt install ngrok -y
else
    echo -e "${G}[+] Ngrok is already installed.${W}"
fi

# 3. Configure Ngrok Token
echo -e "${Y}[*] Configuring Ngrok AuthToken...${W}"
ngrok config add-authtoken 2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF

# 4. Finalizing
echo -e "${R}=======================================================${W}"
echo -e "${G}[+] SYSTEM READY FOR DEPLOYMENT!${W}"
echo -e "${C}[>] To start your tool, run: python3 nexo-advanced_termux_otp-lock.py${W}"
echo -e "${R}=======================================================${W}"
