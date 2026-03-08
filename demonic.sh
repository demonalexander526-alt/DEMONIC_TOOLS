#!/bin/bash
# цвет
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
MAGENTA="\e[35m"
CYAN="\e[36m"
RESET="\e[0m"
# цвет фона
BG_BLACK='\e[40m'
BG_RED='\e[41m'
BG_GREEN='\e[42m'
BG_YELLOW='\e[43m'
BG_BLUE='\e[44m'
BG_MAGENTA='\e[45m'
BG_CYAN='\e[46m'
BG_WHITE='\e[47m'

type_text() {
    text="$1"
    color="$2"
    speed=0.04
    echo -ne "$color"
    for (( i=0; i<${#text}; i++ )); do
        printf "%s" "${text:$i:1}"
        echo -ne "\a"
        sleep $speed
    done
    printf "\n${RESET}"
}

startup_loading() {
    clear
    echo -ne "Starting DEMONIC: ["
    for ((i=0; i<=40; i++)); do
        echo -ne "#"
        sleep 0.03
    done
    echo "]"
    sleep 0.5
    clear
}

startup_loading

################ Баннер  ############
show_banner() {
    clear
    type_text "===========================================================" "$BG_MAGENTA"
    type_text "            TOOL NAME:✅✅🔥 DEMONIC" "$MAGENTA"
    type_text "            CREATED BY: DEMON ALEX 😈😈" "$MAGENTA"
    type_text "            NEXT UPDATE: (2026) CAM-PHISH WILL BE ADDED TO DEMONIC" "$MAGENTA"
    type_text "===========================================================" "$BG_MAGENTA"
    echo ""
}


scan_nmap() {
    type_text "Enter IP (your own device/server):" "$YELLOW"
    read target
    if ! command -v nmap &>/dev/null; then
        type_text "Installing Nmap..." "$CYAN"
        pkg install nmap -y
    fi
    type_text "Running Nmap scan..." "$CYAN"
    nmap -Pn "$target"
    type_text "Scan completed." "$GREEN"
}


auto_status() {
    clear
    type_text "DEMONIC AUTO STATUS 😈" "$MAGENTA"

    [ ! -f auto_status.txt ] && echo "DEMONIC ACTIVE 🔥" > auto_status.txt

    echo -e "${CYAN}1) Post text status${RESET}"
    echo -e "${CYAN}2) Change default status${RESET}"
    echo -e "${CYAN}0) Back${RESET}"
    read -p "Choose: " st

    case $st in
        1)
            STATUS=$(cat auto_status.txt)
            xdg-open "https://wa.me/?text=$STATUS"
            ;;
        2)
            type_text "Enter new status:" "$YELLOW"
            read ns
            echo "$ns" > auto_status.txt
            type_text "Status updated!" "$GREEN"
            ;;
    esac
}

timer() {
    type_text "Enter alarm name:" "$MAGENTA"
    read alarm
    type_text "Enter time (seconds):" "$YELLOW"
    read sec

    while [ $sec -gt 0 ]; do
        echo -ne "${CYAN}⏱ $alarm : $sec sec remaining\r${RESET}"
        sleep 1
        ((sec--))
    done
    echo ""
    type_text "⏰ ALARM UP: $alarm" "$RED"

    termux-media-player play /system/media/audio/alarms/Alarm_Classic.ogg &

    termux-notification \
      --title "⏰ DEMONIC ALARM" \
      --content "$alarm is UP!" \
      --priority high \
      --sound

    read -p "Press ENTER to stop alarm..."
    termux-media-player stop
}

# ================= Меню 👌💀💀💀 ==================
show_menu() {
    show_banner
    type_text "Choose an option:" "$CYAN"
    echo ""
    type_text "1) Join Official WhatsApp Group" "$GREEN"
    type_text "2) Log System IP to Owner" "$YELLOW"
    type_text "3) Ping Website / IP" "$BLUE"
    type_text "4) Exit" "$RED"
    type_text "5) Contact Owner on WhatsApp" "$MAGENTA"
    type_text "6) Send Anonymous SMS" "$CYAN"
    type_text "7) Join WhatsApp Channel" "$GREEN"
    type_text "8) Run Nmap Scan" "$YELLOW"
    type_text "9) Auto Status Poster" "$MAGENTA"
    type_text "10) Timer Alarm Tool" "$CYAN"
    type_text "11) BLACK BOX " "$MAGENTA"
    type_text "12)  Dev_2" "$GREEN"
    type_text "13) Dev 3" "$MAGENTA"
    echo ""
}

while true; do
    show_menu
    read -p "Enter choice: " choice

    case $choice in
        1) xdg-open "https://chat.whatsapp.com/GBLk6GbpwhPGKmUombsivo" ;;
        2)
            IP=$(curl -s https://api.ipify.org)
            DEV=$(uname -a)
            xdg-open "https://wa.me/2349054345858?text=DEMONIC%20LOG%0AIP:$IP%0A$DEV"
            ;;
        3)
            read -p "Target: " t
            ping -c 4 "$t"
            ;;
        4) exit ;;
        5) xdg-open "https://wa.me/2349054345858" ;;
        6)
            read -p "Number: " n
            read -p "Message: " m
            curl -s -X POST https://textbelt.com/text \
              --data-urlencode "phone=$n" \
              --data-urlencode "message=$m" \
              -d key=textbelt
            ;;
        7) xdg-open "https://chat.whatsapp.com/0029VbBTIB9GzzKYKnhOTp32" ;;
        8) scan_nmap ;;
        9) auto_status ;;
        10) timer ;;
        11) xdg-open "https://black-box-official.onrender.com/homepage.html";;
        12) xdg-open "https://wa.me/2348141104435";;
        13) xdg-open "https://wa.me/2347061247283";;
        *) type_text "Invalid option!" "$RED" ;;

    esac

    type_text "Press ENTER to continue..." "$CYAN"
    read
done
