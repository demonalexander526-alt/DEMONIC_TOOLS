import os
import time

# --- NEXO Colors ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear')
    print(f"{C}{B}")
    print(r"  _   _  _______   _____     _____ ______ _   _ ")
    print(r" | \ | | | ____\ \ / / _ \   / ____|  ____| \ | |")
    print(r" |  \| | | |__   \ V / | | | | |  __| |__  |  \| |")
    print(r" | . ` | |  __|   > <| | | | | | |_ |  __| | . ` |")
    print(r" | |\  | | |____ / . \ |_| | | |__| | |____| |\  |")
    print(r" |_| \_| |______/_/ \_\___/   \_____|______|_| \_|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  PROJECT:     {W}NEXO-GEN V1.0")
    print(f"{Y}  TYPE:        {W}TARGETED PROFILING GENERATOR")
    print(f"{G}======================================================={W}\n")

def generate_wordlist():
    show_banner()
    
    # 1. Gather Profile Data
    print(f"{C}[*] Enter target details (Leave blank if unknown):{W}")
    first_name = input(f"{Y}> First Name: {W}").lower().strip()
    last_name = input(f"{Y}> Last Name: {W}").lower().strip()
    birthday = input(f"{Y}> Birthday (DDMMYYYY): {W}").strip()
    pet_name = input(f"{Y}> Pet's Name: {W}").lower().strip()
    company = input(f"{Y}> Company/Brand: {W}").lower().strip()
    
    seeds = [first_name, last_name, pet_name, company]
    seeds = [s for s in seeds if s] # Filter out blanks

    # 2. Advanced Transformations
    # Professionals add common suffixes and "Leet" speak variations
    years = ["2023", "2024", "2025", "2026"]
    special_chars = ["!", "@", "#", "$", "123"]
    
    wordlist = set()
    
    print(f"\n{C}[*] Engineering wordlist combinations...{W}")
    
    for s in seeds:
        wordlist.add(s)
        wordlist.add(s.capitalize())
        wordlist.add(s.upper())
        
        # Add years and special characters
        for y in years:
            wordlist.add(f"{s}{y}")
            wordlist.add(f"{s.capitalize()}{y}")
        for char in special_chars:
            wordlist.add(f"{s}{char}")
            wordlist.add(f"{s.capitalize()}{char}")
            
    if birthday:
        wordlist.add(birthday)
        if len(birthday) == 8: # DDMMYYYY
            wordlist.add(birthday[:4]) # DDMM
            wordlist.add(birthday[4:]) # YYYY

    # 3. Save to File
    filename = "nexo_wordlist.txt"
    with open(filename, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")
            
    print(f"{G}[+] Success! {len(wordlist)} passwords saved to {filename}.{W}")

if __name__ == "__main__":
    generate_wordlist()

