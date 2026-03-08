import os
import subprocess
import sys
import time

# --- NEXO Colors ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear')
    print(f"{C}{B}")
    print(r"  _   _  _______   _____    _____ _   _  _____ _______  _      _      ")
    print(r" | \ | | | ____\ \ / / _ \  |_   _| \ | |/ ____|__   __|/ \    | |     ")
    print(r" |  \| | | |__   \ V / | | |   | | |  \| | (___    | |  / _ \   | |     ")
    print(r" | . ` | |  __|   > <| | | |   | | | . ` |\___ \   | | / ___ \  | |     ")
    print(r" | |\  | | |____ / . \ |_| |  _| |_| |\  |____) |  | |/ /   \ \ | |____ ")
    print(r" |_| \_| |______/_/ \_\___/  |_____|_| \_|_____/   |_/_/     \_\______|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  PROJECT:     {W}NEXO-PACKAGES-INSTALLER (ELITE)")
    print(f"{Y}  TOOLS:       {W}BRUTE-FORCE & WIFI-AUDIT READY")
    print(f"{G}======================================================={W}\n")

def run_command(command, description):
    print(f"{C}[*] {description}...{W}")
    os.system(command)

def main():
    show_banner()
    
    print(f"{Y}[?] Start NEXO ELITE installation? (y/n): {W}", end="")
    if input().lower() != 'y':
        print(f"{R}[!] Installation Aborted.{W}")
        return

    # 1. System Core Updates
    run_command("pkg update -y && pkg upgrade -y", "Updating System Repositories")

    # 2. Hardcore System Dependencies (For WiFi & Brute Tools)
    # aircrack-ng is for WiFi, hydra is for pro brute-forcing
    sys_pkgs = ["tor", "libpcap", "wget", "git", "aircrack-ng", "hydra", "nmap", "openssl"]
    for pkg in sys_pkgs:
        run_command(f"pkg install {pkg} -y || sudo apt-get install {pkg} -y", f"Installing {pkg}")

    # 3. Python Module Engine
    run_command(f"{sys.executable} -m pip install --upgrade pip", "Upgrading Python PIP")
    
    python_modules = ["requests", "aiohttp", "stem", "flask", "pyngrok", "scapy", "colorama", "passlib"]
    for module in python_modules:
        run_command(f"{sys.executable} -m pip install {module}", f"Installing Python Module: {module}")

    # 4. Wordlist Setup (The "Engine" for NEXO-BRUTE)
    if not os.path.exists("pass.txt"):
        run_command("wget https://raw.githubusercontent.com -O pass.txt", "Downloading Starter Wordlist (pass.txt)")

    print(f"\n{G}{B}[SUCCESS] NEXO ELITE ENVIRONMENT DEPLOYED!{W}")
    print(f"{Y}[+] {W}NEXO-BRUTE:   {G}READY (Wordlist: pass.txt){W}")
    print(f"{Y}[+] {W}NEXO-WIFI:    {G}READY (Requires Root/External Adapter){W}")
    print(f"{Y}[+] {W}NEXO-PROXY:   {G}READY (Run 'tor' first){W}")
    print(f"\n{C}Usage: python <tool_name>.py{W}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] NEXO Installer killed.{W}")
	
