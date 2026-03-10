import os
import time
import random

# --- NEXO-TECH COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner(module="MASTER SUITE"):
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"{R}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(f" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_{W}")
    print(f"{R}======================================================={W}")
    print(f"{Y}  MODULE:      {W}{module}")
    print(f"{Y}  STATUS:      {G}ALGO-INJECTION READY{W}")
    print(f"{R}======================================================={W}\n")

# --- MODULE 1: FAKE GMAIL GEN ---
def gmail_gen():
    show_banner("GMAIL GENERATOR")
    count = int(input(f"{Y}[+] How many Gmails to generate?: {W}"))
    print(f"\n{R}[!] NEXO-TECH: BYPASSING GOOGLE CAPTCHA...{W}")
    time.sleep(2)
    
    for i in range(count):
        user = "nexo." + str(random.randint(1000, 9999)) + os.urandom(2).hex()
        mail = f"{user}@gmail.com"
        print(f"{G}[+] CREATED: {W}{mail} {C}| Status: {G}ACTIVE{W}")
        with open("nexo_database.txt", "a") as f:
            f.write(f"GMAIL: {mail}\n")
    
    input(f"\n{Y}Gmails saved to database. Press Enter...{W}")

# --- MODULE 2: SPAM PROMOTER ---
def spam_promote():
    show_banner("SPAM PROMOTER")
    print(f"{Y}[1] TikTok  [2] Instagram  [3] Facebook{W}")
    plat = input(f"\n{C}Selection: {W}")
    target = input(f"{Y}[+] Enter Target Link/Account: {W}")
    
    print(f"\n{R}[!] LOAD-BALANCING FAKE ACCOUNTS...{W}")
    time.sleep(2)
    
    hits = 0
    try:
        while True:
            # Simulated high-speed promotion using the generated "fake" accounts
            proxy = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
            print(f"\r{Y}[*] HITS: {W}{hits} {G}| {C}IP: {W}{proxy} {G}>>> {R}PROMOTING{W}", end="")
            hits += 1
            if hits % 50 == 0: time.sleep(0.01)
    except KeyboardInterrupt:
        print(f"\n\n{G}[+] Promotion Optimized. Total Algo-Hits: {hits}{W}")
        input(f"\n{Y}Press Enter...{W}")

# --- MAIN MENU ---
def main():
    while True:
        show_banner()
        print(f"  {G}1.{W} Generate Fake Gmails (for bots)")
        print(f"  {C}2.{W} Phone Number Trace (+CC)")
        print(f"  {Y}3.{W} Spam Promote (TT/IG/FB)")
        print(f"  {R}4.{W} Virus Creator Lab")
        print(f"  {R}5.{W} Exit")
        
        choice = input(f"\n{Y}NEXO-TECH > {W}")
        
        if choice == '1': gmail_gen()
        elif choice == '3': spam_promote()
        elif choice == '5': break

if __name__ == "__main__":
    main() 
