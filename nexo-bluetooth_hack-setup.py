#!/data/data/com.termux/files/usr/bin/bash

# --- NEXO-TECH COLORS ---
G='\033[92m'
Y='\033[93m'
C='\033[96m'
R='\033[91m'
W='\033[0m'
B='\033[1m'

clear
echo -e "${R}${B}"
echo "  _   _  _______   _____    _____ ______ _____ _    _ "
echo " | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |"
echo " |  \| | | |__   \ V / | | |   | | |  __|| |    | |__| |"
echo " | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |"
echo " | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |"
echo " |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|"
echo -e "${G}======================================================={W}"
echo -e "${Y}  INSTALLER:   ${W}NEXO-BLUE OMNIPOTENCE GOD-MODE"
echo -e "${Y}  POWERED BY:  ${W}DEMON ALEX & BLUEY & AGTSMOKY"
echo -e "${G}======================================================={W}\n"

echo -e "${C}[*] Updating Repositories...${W}"
pkg update -y && pkg upgrade -y

echo -e "${C}[*] Installing Core Bluetooth Stack (Bluez)...${W}"
pkg install -y bluez tsu python git make clang -y

echo -e "${C}[*] Installing HID & MAC Spoofing Dependencies...${W}"
# bdaddr allows us to change the hardware MAC address for hijacking
if [ ! -f "$PREFIX/bin/bdaddr" ]; then
    echo -e "${Y}[!] Compiling MAC Spoofer (bdaddr)...${W}"
    git clone https://github.com
    cd bdaddr && make
    cp bdaddr $PREFIX/bin/
    cd .. && rm -rf bdaddr
fi

echo -e "${C}[*] Installing Python Libraries...${W}"
pip install pybluez2 2>/dev/null || pip install pybluez

echo -e "${C}[*] Activating Bluetooth Interface (hci0)...${W}"
# Force the Bluetooth radio to wake up and enter 'Scan' mode
tsu -c "hciconfig hci0 up"
tsu -c "hciconfig hci0 piscan"

echo -e "\n${G}[+] OMNIPOTENCE SETUP COMPLETE!${W}"
echo -e "${G}-------------------------------------------------------${W}"
echo -e "${Y}[!] TO ACTIVATE THE ENGINE:${W}"
echo -e "${C}1. Enter Root: ${G}tsu${W}"
echo -e "${C}2. Run Engine: ${G}python nexo-bluetooth_hack.py${W}"
echo -e "${G}-------------------------------------------------------${W}"
