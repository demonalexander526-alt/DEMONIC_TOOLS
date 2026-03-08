#!/bin/bash
# Note for termux error if you encounter one run the commads below to fix it
# pkg install termux-api curl -y
# chmod +x demonic_ip-changer.sh
# ./demonic_ip-changer.sh
# for Kali linux users run 👇👇👇👇👇👇
# sudo apt install network-manager curl -y
# chmod +x demonic_ip-changer.sh
# sudo ./demonic_ip-changer.sh
# pls don't run the  harsh with it the only 
# purpose of he harsh is to comment the line out 

# ================= DEMONIC IP CHANGER =================
# Platform: Linux + Termux (Auto-detect)
# Interval: 3 Hours
# CREATED BY: DEMON ALEX
# =====================================================

INTERVAL=10800   # 3 hours (seconds)
LOG="$HOME/demonic_ip.log"

# ================= FUNCTIONS =================
get_ip() {
    curl -s https://api.ipify.org
}

is_termux() {
    [[ "$PREFIX" == *"com.termux"* ]]
}

# ================= START =================
clear
echo "========================================"
echo "😈 DEMONIC IP CHANGER ACTIVE"
echo "⏰ Interval : Every 3 Hours"
echo "📄 Log File : $LOG"
echo "========================================"
echo ""

# ================= TERMUX MODE =================
if is_termux; then
    if ! command -v termux-notification &>/dev/null; then
        echo "❌ Required Termux API not installed"
        echo "Run: pkg install termux-api"
        exit 1
    fi

    echo "[MODE] Termux (Mobile Data)"

    while true; do
        OLD_IP=$(get_ip)
        TIME=$(date "+%Y-%m-%d %H:%M:%S")

        termux-toast "DEMONIC: Changing IP..."
        termux-vibrate -d 300

        # Toggle mobile data
        svc data disable
        sleep 10
        svc data enable

        sleep 8
        NEW_IP=$(get_ip)

        echo "$TIME | TERMUX | OLD: $OLD_IP | NEW: $NEW_IP" >> "$LOG"

        termux-notification \
          --title "😈 DEMONIC IP CHANGED" \
          --content "New IP: $NEW_IP" \
          --priority high

        echo "[$TIME] IP Changed (Termux)"
        echo "OLD → $OLD_IP"
        echo "NEW → $NEW_IP"
        echo "----------------------------------------"

        sleep $INTERVAL
    done
fi

# ================= LINUX MODE =================
if ! is_termux; then
    if ! command -v nmcli &>/dev/null; then
        echo "❌ NetworkManager not found (nmcli)"
        echo "Install it first:"
        echo "  sudo apt install network-manager"
        exit 1
    fi

    if [ "$EUID" -ne 0 ]; then
        echo "❌ Linux mode requires root"
        echo "Run: sudo bash demonic_ip-changer.sh"
        exit 1
    fi

    echo "[MODE] Linux (NetworkManager)"

    get_active_conn() {
        nmcli -t -f NAME,DEVICE connection show --active | head -n1 | cut -d: -f1
    }

    while true; do
        OLD_IP=$(get_ip)
        CONN=$(get_active_conn)
        TIME=$(date "+%Y-%m-%d %H:%M:%S")

        if [ -z "$CONN" ]; then
            echo "[$TIME] ❌ No active connection found" | tee -a "$LOG"
            sleep $INTERVAL
            continue
        fi

        echo "[$TIME] Reconnecting: $CONN"
        nmcli connection down "$CONN"
        sleep 5
        nmcli connection up "$CONN"

        sleep 8
        NEW_IP=$(get_ip)

        echo "$TIME | LINUX | OLD: $OLD_IP | NEW: $NEW_IP" >> "$LOG"

        echo "IP Changed (Linux)"
        echo "OLD → $OLD_IP"
        echo "NEW → $NEW_IP"
        echo "----------------------------------------"

        sleep $INTERVAL
    done
fi

