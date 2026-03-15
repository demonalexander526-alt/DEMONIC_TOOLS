import os
import subprocess
import time

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
    print(f"{Y}  SYSTEM:      {W}COMBINED OSINT ENGINE v7.0")
    print(f"{Y}  ARCHITECTURE:{W} POLYGLOT (PY/C++/JAVA)")
    print(f"{G}======================================================={W}\n")

def start_engine():
    show_banner()
    
    print(f"{Y}[+] SELECT ENGINE MODE:{W}")
    print(f"  {G}1.{W} C++ Engine (Fast Scan)")
    print(f"  {C}2.{W} Java Engine (Deep Scan)")
    print(f"  {R}3.{W} Full Polyglot (Both)")
    
    choice = input(f"\n{Y}Selection [1-3]: {W}")
    target = input(f"{Y}Enter Target Phone: {W}")

    print(f"\n{R}[!] NEXO-TECH: WAKING UP ENGINE...{W}")
    time.sleep(1) # For that "loading" feel
    print(f"{G}-------------------------------------------------------{W}")

    try:
        if choice == "1":
            # Direct terminal execution so results SHOW UP
            subprocess.call(["./nexo_fast", target])
        elif choice == "2":
            subprocess.call(["java", "NexoDeep", target])
        elif choice == "3":
            subprocess.call(["./nexo_fast", target])
            subprocess.call(["java", "NexoDeep", target])
        else:
            print(f"{R}[!] Invalid selection.{W}")
    except Exception as e:
        print(f"{R}[-] ENGINE ERROR: Check if files are compiled!{W}")

    print(f"{G}-------------------------------------------------------{W}")
    print(f"{Y}[*] Scan Complete. NEXO-TECH System Standby.{W}")

if __name__ == '__main__':
    start_engine()
