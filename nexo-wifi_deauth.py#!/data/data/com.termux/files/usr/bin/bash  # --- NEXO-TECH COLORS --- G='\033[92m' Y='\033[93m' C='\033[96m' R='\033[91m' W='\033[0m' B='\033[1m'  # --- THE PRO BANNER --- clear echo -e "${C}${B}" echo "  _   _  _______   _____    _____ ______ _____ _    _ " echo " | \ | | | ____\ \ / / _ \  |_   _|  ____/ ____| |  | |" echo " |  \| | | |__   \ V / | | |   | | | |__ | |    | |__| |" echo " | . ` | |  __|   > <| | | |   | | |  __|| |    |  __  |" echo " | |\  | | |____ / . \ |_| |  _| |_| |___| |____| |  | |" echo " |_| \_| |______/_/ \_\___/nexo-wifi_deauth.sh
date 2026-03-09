#!/data/data/com.termux/files/usr/bin/bash

# --- NEXO-TECH COLORS ---
G='\033[92m'
Y='\033[93m'
C='\033[96m'
R='\033[91m'
W='\033[0m'
B='\033[1m'

# --- THE PRO BANNER ---
clear
echo -e "${C}${B}"
echo "  _   _  _______   _____    _____ ______ _____ _    _ "
echo " | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |"
echo " |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |"
echo " | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |"
echo " | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |"
echo " |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|"
echo -e "${G}=======================================================${W}"
echo -e "${Y}  INSTALLER:   ${W}NEXO-DEAUTH ENGINE"
echo -e "${Y}  SYSTEM:      ${W}TERMUX / ANDROID"
echo -e "${G}=======================================================${W}\n"

# --- INSTALLATION PROCESS ---
echo -e "${C}[*] Updating Repositories...${W}"
pkg update -y && pkg upgrade -y

echo -e "${C}[*] Installing Root & X11 Repos...${W}"
pkg install -y root-repo x11-repo

echo -e "${C}[*] Installing Python & Network Tools...${W}"
pkg install -y python python-pip aircrack-ng tsu iw -y

echo -e "${C}[*] Installing Scapy Library...${W}"
pip install scapy

# --- FINISH ---
echo -e "\n${G}[+] NEXO-TECH SETUP COMPLETE!${W}"
echo -e "${G}-------------------------------------------------------${W}"
echo -e "${Y}[!] NEXT STEPS:${W}"
echo -e "${C}1. Connect USB OTG Wi-Fi Adapter (Required for most phones)${W}"
echo -e "${C}2. Enter Root Mode: ${G}tsu${W}"
echo -e "${C}3. Start Monitor Mode: ${G}airmon-ng start wlan0${W}"
echo -e "${C}4. Launch Engine: ${G}python nexo-wifi_deauth.py${W}"
echo -e "${G}-------------------------------------------------------${W}"
