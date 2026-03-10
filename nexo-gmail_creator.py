import os
import requests
import datetime
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- NEXO-TECH COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"{C}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  TOOL:        {W}MULTI-GMAIL ENGINE")
    print(f"{Y}  CREATED BY:  {W}NEXO-TECH")
    print(f"{G}======================================================={W}\n")

# --- HTML INTERFACE ---
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>NEXO-TECH Engine</title>
    <style>
        body { background-color: #0d1117; color: #58a6ff; font-family: 'Courier New', monospace; text-align: center; padding: 50px; }
        .box { border: 2px solid #238636; padding: 20px; display: inline-block; border-radius: 10px; background: #161b22; min-width: 400px; }
        .email-text { color: #f0883e; font-size: 22px; font-weight: bold; margin: 15px; border: 1px dashed #58a6ff; padding: 10px; }
        .type-tag { font-size: 14px; padding: 5px 10px; border-radius: 5px; color: white; }
        .btn { background: #238636; color: white; border: none; padding: 10px 20px; cursor: pointer; border-radius: 5px; text-decoration: none; display: inline-block; margin-top: 10px; }
    </style>
</head>
<body>
    <h1>NEXO-TECH GMAIL ENGINE</h1>
    <div class="box">
        <p>Generated <span class="type-tag" style="background:{{ color }};">{{ mode }}</span> Address:</p>
        <div class="email-text">{{ email }}</div>
        <p>Status: <span style="color:#7ee787;">READY</span></p>
        <a href="/" class="btn">BACK TO MENU</a>
    </div>
</body>
</html>
"""

MENU_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>NEXO-TECH Menu</title>
    <style>
        body { background-color: #0d1117; color: #58a6ff; font-family: 'Courier New', monospace; text-align: center; padding: 50px; }
        .menu-btn { background: #21262d; color: #58a6ff; border: 1px solid #30363d; padding: 15px; margin: 10px; width: 300px; cursor: pointer; border-radius: 6px; display: block; margin-left: auto; margin-right: auto; text-decoration: none; }
        .menu-btn:hover { background: #238636; color: white; }
    </style>
</head>
<body>
    <h1 style="color:#f85149;">-- SELECT GENERATION MODE --</h1>
    <a href="/gen/7day" class="menu-btn">1. Gmail (Expires 7 Days)</a>
    <a href="/gen/permanent" class="menu-btn">2. Gmail (No Expiry - Alias)</a>
    <a href="/gen/24hr" class="menu-btn">3. Gmail (Expires 24 Hours)</a>
</body>
</html>
"""

@app.route('/')
def menu():
    return render_template_string(MENU_PAGE)

@app.route('/gen/<mode>')
def generate(mode):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    color_map = {"7day": "#f0883e", "permanent": "#238636", "24hr": "#f85149"}
    
    # Logic for different modes
    if mode == "permanent":
        # Uses the DOT/Alias trick on a base name
        email = f"nexo.tech.{os.urandom(2).hex()}@gmail.com"
        expiry = "PERMANENT"
    elif mode == "7day":
        # Requires Gmailnator/SmailPro Premium style logic
        email = f"tmp.7d.{os.urandom(3).hex()}@gmail.com"
        expiry = "7 DAYS"
    else:
        # Standard disposable 24h address
        email = f"tmp.24h.{os.urandom(3).hex()}@gmail.com"
        expiry = "24 HOURS"

    # --- LOGGING TO CONSOLE WITH BANNER ---
    print(f"{R}[{timestamp}] NEXO-TECH ALERT: NEW GENERATION{W}")
    print(f"{G}[+] TYPE:    {W}{mode.upper()}")
    print(f"{G}[+] EMAIL:   {W}{email}")
    print(f"{C}[*] EXPIRY:  {W}{expiry}")
    print(f"{G}-------------------------------------------------------{W}")

    # Log to nexo_database.txt
    with open("nexo_database.txt", "a") as f:
        f.write(f"[{timestamp}] MODE: {mode} | EMAIL: {email} | EXPIRY: {expiry}\n")

    return render_template_string(HTML_PAGE, email=email, mode=mode.upper(), color=color_map.get(mode, "#58a6ff"))

if __name__ == '__main__':
    show_banner()
    print(f"{C}[*] NEXO-TECH ENGINE: {G}[ ONLINE ]{W}")
    print(f"{C}[*] PORT:            {W}5000")
    print(f"{G}-------------------------------------------------------{W}")
    app.run(host='0.0.0.0', port=5000)
