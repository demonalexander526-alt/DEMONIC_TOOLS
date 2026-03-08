import os
import subprocess
import time
import sys

# --- NEXO Colors ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear')
    print(f"{C}{B}")
    print(r"  _   _  _______   _____    __          __ _____  ______ _____ ")
    print(r" | \ | | | ____\ \ / / _ \   \ \        / /|_   _||  ____|_   _|")
    print(r" |  \| | | |__   \ V / | | |   \ \  /\  / /   | |  | |__    | |  ")
    print(r" | . ` | |  __|   > <| | | |    \ \/  \/ /    | |  |  __|   | |  ")
    print(r" | |\  | | |____ / . \ |_| |     \  /\  /    _| |_ | |     _| |_ ")
    print(r" |_| \_| |______/_/ \_\___/       \/  \/    |_____||_|    |_____|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  PROJECT:     {W}NEXO-WIFI AUDITOR")
    print(f"{Y}  ENGINE:      {W}AIRCRACK-NG AUTOMATION")
    print(f"{G}======================================================={W}\n")

def check_root():
    if os.geteuid() != 0:
        print(f"{R}[!] FATAL: This tool requires ROOT/SUDO privileges.{W}")
        sys.exit()

def start_monitor(interface):
    print(f"{C}[*] Enabling Monitor Mode on {interface}...{W}")
    subprocess.run(["airmon-ng", "start", interface], stdout=subprocess.DEVNULL)
    return f"{interface}mon"

def scan_targets(interface):
    print(f"{Y}[*] Starting discovery scan. Press Ctrl+C to select a target.{W}")
    try:
        # Runs airodump-ng to show nearby networks
        subprocess.run(["airodump-ng", interface])
    except KeyboardInterrupt:
        print(f"\n{G}[+] Scan paused. Ready for targeting.{W}")

if __name__ == "__main__":
    show_banner()
    check_root()
    
    # 1. Identify Interface
    iface = input(f"{Y}Enter Wireless Interface (e.g., wlan0): {W}").strip()
    
    # 2. Start Monitor Mode
    mon_iface = start_monitor(iface)
    
    # 3. Discover Networks
    scan_targets(mon_iface)
    
    # 4. Target Selection
    bssid = input(f"\n{Y}Enter Target BSSID (MAC): {W}").strip()
    channel = input(f"{Y}Enter Target Channel: {W}").strip()
    
    print(f"\n{C}[*] Launching Handshake Capture on {bssid}...{W}")
    # Professional Command: Captures the handshake and saves it to a .cap file
    # subprocess.run(["airodump-ng", "--bssid", bssid, "-c", channel, "-w", "capture", mon_iface])
	
