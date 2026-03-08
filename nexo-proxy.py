import time
import sys
import os
import requests
from stem import Signal
from stem.control import Controller

# --- NEXO Colors ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear')
    print(f"{C}{B}")
    print(r"  _   _  _______   _____    __      __ _____  _   _ ")
    print(r" | \ | | | ____\ \ / / _ \   \ \    / /|  __ \| \ | |")
    print(r" |  \| | | |__   \ V / | | |   \ \  / / | |__) |  \| |")
    print(r" | . ` | |  __|   > <| | | |    \ \/ /  |  ___/| . ` |")
    print(r" | |\  | | |____ / . \ |_| |     \  /   | |    | |\  |")
    print(r" |_| \_| |______/_/ \_\___/       \/    |_|    |_| \_|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  TOOL:        {W}NEXO TERMINAL VPN (TOR ENGINE)")
    print(f"{Y}  STATUS:      {W}ACTIVE ROTATION")
    print(f"{G}======================================================={W}\n")

def get_current_ip():
    """Fetches the current public IP via Tor proxy."""
    proxies = {
        'http':  'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    try:
        # Using a public API to verify the external IP
        return requests.get('https://api.ipify.org', proxies=proxies, timeout=10).text
    except:
        return "Connection Error"

def rotate_ip():
    """Signals Tor to build a new circuit for a new IP."""
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate() # Ensure ControlPort is active in torrc
            controller.signal(Signal.NEWNYM)
            return True
    except Exception as e:
        print(f"{R}[!] ControlPort Error: {e}{W}")
        return False

def start_vpn():
    show_banner()
    print(f"{C}[*] Establishing secure tunnel...{W}")
    
    while True:
        if rotate_ip():
            time.sleep(3) # Wait for Tor to stabilize the new circuit
            new_ip = get_current_ip()
            timestamp = time.strftime('%H:%M:%S')
            print(f"{G}[{timestamp}] {W}New Identity Assigned: {B}{Y}{new_ip}{W}")
        
        # Change IP every 30 seconds (adjust as needed)
        time.sleep(30)

if __name__ == "__main__":
    try:
        start_vpn()
    except KeyboardInterrupt:
        print(f"\n{R}[!] NEXO VPN Shutdown.{W}")

