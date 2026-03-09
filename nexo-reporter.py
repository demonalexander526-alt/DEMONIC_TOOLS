import os
import time
import random

# --- NEXO-TECH PRO COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"{R}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  CREATED BY:  {W}NEXO-TECH")
    print(f"{Y}  POWERED BY:  {W}DEMON ALEX & BLUEY & AGTSMOKY")
    print(f"{Y}  MODULE:      {R}UNIVERSAL MASS-REPORT BOT{W}")
    print(f"{G}======================================================={W}\n")

def run_ban_logic(link, threads):
    # Specialized TOS Violation Reasons
    reasons = ["Hate Speech", "Illegal Activities", "Child Safety", "Harassment"]
    
    print(f"{C}[*] ANALYZING LINK: {W}{link}")
    print(f"{C}[*] STATUS: {G}[ TARGET ACQUIRED ]{W}")
    print(f"{G}-------------------------------------------------------{W}")

    for i in range(1, threads + 1):
        reason = random.choice(reasons)
        # Simulation of the API reporting payload
        print(f"{R}[!] INJECTING REPORT #{i} {W}| Link: {link[:25]}... | Reason: {Y}{reason}{W}")
        time.sleep(0.3)

    print(f"\n{G}[+] BAN SEQUENCE COMPLETE. TARGET LINK IS UNDER REVIEW.{W}")

if __name__ == "__main__":
    show_banner()
    target_link = input(f"{Y}[+] Paste Target Link (TT/IG/FB): {W}")
    thread_count = int(input(f"{Y}[+] Enter Report Intensity (1-1000): {W}"))
    
    show_banner()
    print(f"{C}[*] NEXO-TECH ENGINE: {G}[ OVERDEADLY MODE ACTIVE ]{W}")
    run_ban_logic(target_link, thread_count)
