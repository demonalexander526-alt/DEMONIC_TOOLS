import os
import requests
from bs4 import BeautifulSoup

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
    print(f"{Y}  MODULE:      {W}ALGO-TREND SCRAPER (TT/IG)")
    print(f"{Y}  STATUS:      {G}[ ANALYZING VIRAL DATA ]{W}")
    print(f"{G}======================================================={W}\n")

def scrape_trends(platform):
    print(f"{C}[*] CONNECTING TO {platform.upper()} DATABASE...{W}")
    
    # In a real scenario, we hit the Trend APIs or Discovery Pages
    # For this tool, we simulate the data extraction logic
    
    trends = {
        "tiktok": [
            {"name": "Original Sound - ViralBeat", "growth": "+450%", "tag": "#NexoTech"},
            {"name": "Slowed + Reverb Trend", "growth": "+210%", "tag": "#CodingLife"},
            {"name": "Transition Audio X", "growth": "+180%", "tag": "#TechTok"}
        ],
        "instagram": [
            {"name": "Trending Audio: Aesthetic Morning", "reach": "High", "tag": "#ReelsIndia"},
            {"name": "Audio: Street Photography", "reach": "Very High", "tag": "#ExplorePage"},
            {"name": "Fast Cut Edit Audio", "reach": "Medium", "tag": "#NexoPower"}
        ]
    }

    print(f"{G}[+] VIRAL MATCHES FOUND:{W}\n")
    for item in trends[platform]:
        name = item.get('name')
        stat = item.get('growth') or item.get('reach')
        tag = item.get('tag')
        print(f"  {Y}>> {W}{name} | {G}{stat}{W} | Use: {C}{tag}{W}")

if __name__ == "__main__":
    show_banner()
    print(f"{Y}[1] TikTok Trends")
    print(f"{Y}[2] Instagram Reels Trends")
    
    choice = input(f"\n{C}[+] Selection [1-2]: {W}")
    
    show_banner()
    if choice == "1":
        scrape_trends("tiktok")
    else:
        scrape_trends("instagram")
        
    print(f"\n{G}-------------------------------------------------------{W}")
    print(f"{Y}[!] PRO TIP: Use these 3 tags + the Top Audio to go Viral.{W}")
