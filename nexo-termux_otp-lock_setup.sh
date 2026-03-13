#!/bin/bash

# --- NEXO-TECH AUTO SETUP & RUN ---
G='\033[92m'
R='\033[91m'
W='\033[0m'

echo -e "${G}[*] INITIALIZING SYSTEM...${W}"

# 1. Update and install core packages
pkg update && pkg upgrade -y
pkg install python ngrok -y

# 2. Install Python dependencies
pip install flask requests pyngrok

# 3. Add Ngrok Token (Applying your token)
ngrok config add-authtoken 2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF

# 4. Final check for the python script
if [ -f "nexo-termux_otp-lock.py" ]; then
    echo -e "${G}[+] Script found. Launching Nexo-Tech...${W}"
    python nexo-termux_otp-lock.py
else
    echo -e "${R}[!] ERROR: nexo-termux_otp-lock.py not found in this folder!${W}"
fi
