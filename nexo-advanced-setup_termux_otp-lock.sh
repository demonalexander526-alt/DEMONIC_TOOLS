#!/bin/bash
# NEXO-TECH SYSTEM INITIALIZATION
# VERSION: 8.0 BLACKOUT - CORE DEPLOYMENT

echo -e "\033[92m[*] SYNCHRONIZING SYSTEM REPOSITORIES...\033[0m"
apt update -y && apt upgrade -y

echo -e "\033[92m[*] INSTALLING NETWORK DEPENDENCIES...\033[0m"
apt install python -y
pip install flask requests phonenumbers

# Check for Ngrok
if ! command -v ngrok &> /dev/null
then
    echo -e "\033[91m[!] NGROK BINARY MISSING. INITIATING PKG INSTALL...\033[0m"
    pkg install ngrok -y
fi

# Applying Token
echo -e "\033[96m[*] INJECTING AUTHENTICATION TOKEN...\033[0m"
ngrok config add-authtoken 2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF

# Permission fix
python nexo-advanced_termux_otp-lock.py

echo -e "\033[92m[+] CORE INITIALIZED. SYSTEM READY.\033[0m"
echo -e "\033[93m[!] EXECUTE: python nexo-advanced_termux_otp-lock.py\033[0m"
