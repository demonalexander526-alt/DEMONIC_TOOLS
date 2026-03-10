import os
import time
import random

# --- NEXO-TECH COLORS ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

# --- 1. GLOBAL MASTER BANNER ---
def main_banner(module="SYSTEM STATUS"):
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
    print(f"{Y}  ENGINE:      {G}NEXO-TECH PYTHON 3.1{W}")
    print(f"{R}======================================================={W}\n")

# --- 2. SPECIFIC SUB-BANNERS ---
def whatsapp_group_banner():
    print(f"{G}{B}  [ WHATSAPP GROUP INTELLIGENCE / BANNER ]{W}")
    print(f"{G}-------------------------------------------------------{W}")

def number_trace_banner():
    print(f"{C}{B}  [ PHONE NUMBER TRACE / BANNER ]{W}")
    print(f"{C}-------------------------------------------------------{W}")

def virus_creator_banner():
    print(f"{R}{B}  [ MALWARE & VIRUS CREATOR LAB ]{W}")
    print(f"{R}-------------------------------------------------------{W}")

# --- 3. CORE MODULES ---

def whatsapp_module():
    main_banner("WHATSAPP OSINT")
    whatsapp_group_banner() # <--- Now forced to show
    link = input(f"{Y}[+] Enter Group Invite Link: {W}")
    print(f"\n{R}[!] NEXO-TECH: SCRAPING GROUP DATA...{W}")
    time.sleep(2)
    print(f"{G}[+] Group Metadata Captured Successfully.{W}")
    input(f"\n{Y}Press Enter to return...{W}")

def number_module():
    main_banner("NUMBER TRACE")
    number_trace_banner() # <--- Now forced to show
    cc = input(f"{G}[+] Enter Country Code (e.g. +234): {W}")
    num = input(f"{G}[+] Enter Phone Number: {W}")
    target = cc + num
    print(f"\n{R}[!] NEXO-TECH: RUNNING GLOBAL TRACE ON {target}...{W}")
    time.sleep(2)
    print(f"{C}[*] Status:      {G}ACTIVE{W}")
    print(f"{C}[*] Search Link: {W}https://www.google.com{target}%22")
    input(f"\n{Y}Press Enter to return...{W}")

def virus_module():
    main_banner("VIRUS CREATOR")
    virus_creator_banner() # <--- Now forced to show
    print(f"  {R}1.{W} Android Trojan (.apk)\n  {R}2.{W} Windows Keylogger (.exe)")
    choice = input(f"\nSelection: ")
    name = input(f"{C}[+] Payload Name: {W}")
    print(f"\n{R}[!] GENERATING MALWARE STUB...{W}")
    time.sleep(2)
    ext = ".apk" if choice == "1" else ".exe"
    with open(name + ext, "w") as f:
        f.write("X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*")
    print(f"{G}[+] VIRUS CREATED: {W}{name}{ext}")
    input(f"\n{Y}Press Enter to return...{W}")

def otp_lock_module():
    main_banner("OTP LOCK ENGINE")
    print(f"{Y}{B}  [ OTP LOCK / BYPASS SIMULATOR ]{W}")
    print(f"{Y}-------------------------------------------------------{W}")
    target = input(f"{Y}[+] Enter Target (+CodeNumber): {W}")
    print(f"\n{R}[!] INITIALIZING OTP SATURATION...{W}")
    count = 0
    try:
        while True:
            print(f"\r{R}[ALERT] {W}Sending OTP Request #{count} {G}>>> {W}STATUS: {R}LOCKED", end="")
            count += 1
    except KeyboardInterrupt:
        print(f"\n\n{G}[+] Total Requests Sent: {count}{W}")
        input(f"\n{Y}Press Enter...{W}")

# --- 4. MAIN MENU ---
def start_tool():
    while True:
        main_banner("MASTER MENU")
        print(f"  {G}1.{W} WhatsApp Group Intelligence")
        print(f"  {C}2.{W} Phone Number Trace (+CC)")
        print(f"  {Y}3.{W} OTP Lock Simulator")
        print(f"  {R}4.{W} Virus Creator Lab")
        print(f"  {R}5.{W} Exit")
        
        choice = input(f"\n{Y}NEXO-TECH > {W}")
        
        if choice == "1": whatsapp_module()
        elif choice == "2": number_module()
        elif choice == "3": otp_lock_module()
        elif choice == "4": virus_module()
        elif choice == "5": break

if __name__ == "__main__":
    start_tool()
