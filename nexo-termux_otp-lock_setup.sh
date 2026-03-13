#!/bin/bash
clear
echo -e "\033[92m[*] INITIALIZING FULL NEXO-TECH PROFESSIONAL SUITE...\033[0m"

# Update and install
pkg update && pkg upgrade -y
pkg install python wget tar -y
pip install flask requests

# Fix Binary
if [ ! -f "$PREFIX/bin/ngrok" ]; then
    wget https://bin.equinox.io
    tar -xvzf ngrok-v3-stable-linux-arm64.tgz
    mv ngrok $PREFIX/bin/
    rm ngrok-v3-stable-linux-arm64.tgz
fi

# Apply Token
ngrok config add-authtoken 2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF

# Run
python nexo-termux_otp-lock.py
