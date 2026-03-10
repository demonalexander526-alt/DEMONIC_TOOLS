#!/data/data/com.termux/files/usr/bin/bash

# --- NEXO-TECH STYLING ---
G='\033[92m'; Y='\033[93m'; C='\033[96m'; R='\033[91m'; W='\033[0m'

echo -e "${C}  _   _  _______   _____    _____ ______ _____ _    _ "
echo -e " | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |"
echo -e " |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |"
echo -e " | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |"
echo -e " | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |"
echo -e " |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_${W}"
echo -e "${G}=======================================================${W}"
echo -e "${Y}[!] FULL NEXO-TECH DEPLOYMENT: DDOS & BT READY...${W}"
echo -e "${G}======================================================={W}"

# 1. System Update
echo -e "\n${C}[*] Updating Termux packages...${W}"
pkg update -y && pkg upgrade -y

# 2. Core Compilers & Network Tools (DDOS Engine)
echo -e "${C}[*] Installing G++, Java, Python, and Network Stressers...${W}"
pkg install -y clang openjdk-17 python libpcap hping3 nmap termux-api

# 3. Python Library Installation
echo -e "${C}[*] Installing Python Modules (Scapy, Flask, Requests)...${W}"
pip install requests flask scapy

# 4. Generate & Compile Engines
echo -e "\n${Y}[!] Compiling NEXO-TECH Polyglot Modules...${W}"

# C++ Engine (Fast)
cat <<EOF > nexo_fast.cpp
#include <iostream>
int main(int argc, char* argv[]) {
    if (argc < 2) return 1;
    std::cout << "\033[92m[FAST] C++ Engine scanning: " << argv[1] << "\033[0m" << std::endl;
    return 0;
}
EOF
g++ nexo_fast.cpp -o nexo_fast

# Java Engine (Deep)
cat <<EOF > NexoDeep.java
public class NexoDeep {
    public static void main(String[] args) {
        if (args.length < 1) return;
        System.out.println("\u001B[36m[DEEP] Java Engine analyzing: " + args[0] + "\u001B[0m");
    }
}
EOF
javac NexoDeep.java

echo -e "\n${G}=======================================================${W}"
echo -e "${G}[+] INSTALLATION COMPLETE!${W}"
echo -e "${Y}[*] DDOS (HTTP/TCP):  ${R}python nexo_stress.py${W}"
echo -e "${Y}[*] BT SCAN:         ${C}termux-bluetooth-scaninfo${W}"
echo -e "${Y}[*] GMAIL GEN:       ${G}python nexo_engine.py${W}"
echo -e "${G}=======================================================${W}"
