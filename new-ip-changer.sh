#!/bin/bash
# ===================== DEMONIC IP CHANGER =====================
# Created by: 😈 DEMON ALEX 😈
# Rotates public IP via Tor every X hours with notification

# --------------------- CONFIGURATION --------------------------
INTERVAL_HOURS=3   # Change IP every 3 hours (adjustable)
TORRC_PATH="$HOME/.tor/torrc"

# --------------------- COLORS --------------------------
# Define colors
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
MAGENTA="\e[35m"
CYAN="\e[36m"
RESET="\e[0m"
#!/bin/bash

# Text colors
BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'
MAGENTA='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'

# Background colors
BG_BLACK='\e[40m'
BG_RED='\e[41m'
BG_GREEN='\e[42m'
BG_YELLOW='\e[43m'
BG_BLUE='\e[44m'
BG_MAGENTA='\e[45m'
BG_CYAN='\e[46m'
BG_WHITE='\e[47m'

# Style
# Example usage
# --------------------- FUNCTIONS -----------------------
echo -e "${BG_MAGENTA}==============================================${RESET}"
echo -e "${BG_MAGENTA}     CREATED BY:DEMON ALEX 😈😈😈😈 ${RESET}"
echo -e "${BG_MAGENTA} TOOL NAME: DEMONIC-IP_CHANGER ✅✅✅🔥🔥 ${RESET}"
echo -e "${BG_MAGENTA}============================================== ${RESET}"
check_install() {
    command -v tor >/dev/null 2>&1 || {
        echo -e "${YELLOW}DEMONIC😈😈: Tor not found. Installing...${RESET}"
        pkg update -y
        pkg install tor -y
    }

    command -v termux-notification >/dev/null 2>&1 || {
        echo -e "${YELLOW}DEMONIC😈😈:termux-api not found. Installing...${RESET}"
        pkg install termux-api -y
    }
}
start_tor() {
    echo -e "${GREEN}DEMONIC😈😈:Starting Tor service...${RESET}"
    tor &>/dev/null &
  sleep 4
}

new_ip() {
    echo -e "${YELLOW}DEMONIC😈😈:Rotating IP...${RESET}"
    # Signal Tor for new identity
    pkill -HUP tor
    sleep 2
    PUBLIC_IP=$(curl -s --socks5-hostname 127.0.0.1:9050 ifconfig.me)
    echo -e "${GREEN}DEMONIC😈😈:New IP: ${PUBLIC_IP}${RESET}"
sleep 1  
}

# --------------------- MAIN LOOP --------------------------
check_install
start_tor

while true; do
    new_ip
    echo -e "${YELLOW}DEMONIC😈😈:Waiting ${INTERVAL_HOURS} hour(s) for next IP change...${RESET}"
    sleep "${INTERVAL_HOURS}h"
done
