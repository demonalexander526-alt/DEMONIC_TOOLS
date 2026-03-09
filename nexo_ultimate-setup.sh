#!/data/data/com.termux/files/usr/bin/bash

# --- NEXO-TECH COLORS ---
G='\033[92m'
Y='\033[93m'
C='\033[96m'
R='\033[91m'
W='\033[0m'
B='\033[1m'

clear
echo -e "${C}${B}"
echo "  _   _  _______   _____    _____ ______ _____ _    _ "
echo " | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |"
echo " |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |"
echo " | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |"
echo " | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |"
echo " |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|"
echo -e "${G}======================================================={W}"
echo -e "${Y}  INSTALLER:   ${W}NEXO-ULTIMATE ROGUE ENGINE"
echo -e "${Y}  POWERED BY:  ${W}DEMON ALEX & BLUEY & AGTSMOKY"
echo -e "${G}======================================================={W}\n"

echo -e "${C}[*] Updating Repositories...${W}"
pkg update -y && pkg upgrade -y

echo -e "${C}[*] Installing Core Networking Tools...${W}"
pkg install -y root-repo x11-repo
pkg install -y python python-pip dnsmasq hostapd aircrack-ng tsu iw -y

echo -e "${C}[*] Installing Python Scapy Library...${W}"
pip install scapy

echo -e "${C}[*] Enabling IP Forwarding (The Trap)...${W}"
# This allows traffic to pass from the victim to the internet
tsu -c "sysctl -w net.ipv4.ip_forward=1"

echo -e "\n${G}[+] INSTALLATION COMPLETE!${W}"
echo -e "${G}-------------------------------------------------------${W}"
echo -e "${Y}[!] NEXT STEPS TO ACTIVATE THE ENGINE:${W}"
echo -e "${C}1. Type: ${G}tsu${W} (to enter root)"
echo -e "${C}2. Type: ${G}airmon-ng start wlan0${W} (Monitor Mode)"
echo -e "${C}3. Type: ${G}python nexo_ultimate.py${W}"
echo -e "${G}-------------------------------------------------------${W}"
