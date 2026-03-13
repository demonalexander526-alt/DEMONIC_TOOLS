#!/bin/bash

# NEXO-TECH FULL LOADER
clear
echo -e "\033[92m[*] PREPARING NEXO-TECH FOR TERMUX...\033[0m"

# Ensure Python and dependencies are ready
pkg update && pkg upgrade -y
pkg install python wget tar -y
pip install flask requests pyngrok

# MANUAL NGROK BINARY INSTALL (Fixes the 'Android' Error)
if [ ! -f "/data/data/com.termux/files/usr/bin/ngrok" ]; then
    echo -e "\033[93m[*] Downloading Ngrok Binary...\033[0m"
    wget https://bin.equinox.io
    tar -xvzf ngrok-v3-stable-linux-arm64.tgz
    chmod +x ngrok
    mv ngrok /data/data/com.termux/files/usr/bin/
    rm ngrok-v3-stable-linux-arm64.tgz
fi

# Apply Token
ngrok config add-authtoken 2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF

# Start Tool
if [ -f "nexo-termux_otp-lock.py" ]; then
    python nexo-termux_otp-lock.py
else
    echo -e "\033[91m[!] Error: Python script not found in current folder.\033[0m"
fi
