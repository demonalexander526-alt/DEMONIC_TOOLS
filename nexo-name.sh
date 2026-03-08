#!/bin/bash

# --- Color Definitions ---
G='\033[92m' # Green
Y='\033[93m' # Yellow
C='\033[96m' # Cyan
W='\033[0m'  # White
B='\033[1m'  # Bold

USER_FILE="$HOME/.nexo_king_id"

clear

# --- 1. AUTO-ENGINE CHECK ---
if ! command -v toilet &> /dev/null; then
    echo -e "${Y}[*] INSTALLING HEAVY ENGINES...${W}"
    pkg install toilet figlet -y &> /dev/null
fi

# --- 2. THE LOAD UP MENU (Percentage Bar Runs FIRST) ---
echo -e "${C}${B}[#] NEXO SYSTEM INITIALIZING...${W}"
echo ""
for p in 10 20 35 60 85 100; do
    sleep 0.2
    printf "\r${Y}LOADING: ${G}%3d%% ${W}" $p
    # Draws the solid block bar █
    for ((i=0; i<p/5; i++)); do echo -ne "${G}█"; done
done

echo -e "\n\n${G}[+] KERNEL LOADED. ACCESS GRANTED.${W}"
sleep 0.8
clear

# --- 3. IDENTITY SETUP (Asks after loading) ---
if [ ! -f "$USER_FILE" ]; then
    echo -e "${C}${B}=========================================="
    echo -e "${Y}      NEW NEXO KING DETECTED"
    echo -e "${C}==========================================${W}"
    echo -ne "${G}ENTER YOUR KING NAME: ${W}"
    read name
    echo "$name" > "$USER_FILE"
    clear
fi

NEXO_NAME=$(cat "$USER_FILE")

# --- 4. THE MASSIVE RAINBOW BANNER ---
# 'mono9' or 'block' for maximum thickness
toilet -f mono9 -F gay "$NEXO_NAME"
echo ""

