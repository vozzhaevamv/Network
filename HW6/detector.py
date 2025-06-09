from scapy.all import *
from collections import defaultdict
import time
import argparse
import threading


POST_THRESHOLD = 50   
TIMEOUT_THRESHOLD = 30 
DELAY_THRESHOLD = 5    
CLEANUP_INTERVAL = 10  
CLEANUP_TIMEOUT = 60   

active_posts = defaultdict(dict)
ip_counter = defaultdict(int)
last_cleanup = time.time()

def remove_connection(key):
    """Удаление соединения и обновление счетчиков"""
    if key in active_posts:
        ip = active_posts[key]['ip']
        ip_counter[ip] -= 1
        if ip_counter[ip] <= 0:
            del ip_counter[ip]
        del active_posts[key]

def cleanup_expired_connections():
    """Периодическая очистка неактивных соединений"""
    global last_cleanup
    while True:
        current_time = time.time()
        if current_time - last_cleanup > CLEANUP_INTERVAL:
            for key, conn in list(active_posts.items()):
                if current_time - conn['last_packet'] > CLEANUP_TIMEOUT:
                    remove_connection(key)
            last_cleanup = current_time
        time.sleep(CLEANUP_INTERVAL)

def process_packet(packet):
    """Обработка каждого сетевого пакета"""
    if not (packet.haslayer(TCP) and packet.haslayer(Raw)):
        return

    current_time = time.time()
    ip_src = packet[IP].src
    ip_dst = packet[IP].dst
    tcp = packet[TCP]
    key = (ip_src, tcp.sport, ip_dst, tcp.dport)
    
    try:
        data = packet[Raw].load.decode('utf-8', errors='ignore')
    except:
        return

    # Обнаружение начала POST-запроса
    if key not in active_posts and 'POST' in data and 'HTTP' in data:
        active_posts[key] = {
            'start_time': current_time,
            'last_packet': current_time,
            'ip': ip_src
        }
        ip_counter[ip_src] += 1
        
        if ip_counter[ip_src] > POST_THRESHOLD:
            print(f"[!] Аномалия: {ip_src} имеет {ip_counter[ip_src]} активных POST-запросов")

    
    elif key in active_posts:
        conn = active_posts[key]
        last_time = conn['last_packet']
        conn['last_packet'] = current_time
        if current_time - last_time > DELAY_THRESHOLD:
            print(f"[!] Медленный POST: {ip_src} -> {ip_dst} (задержка {current_time - last_time:.1f} сек)")

        
        if current_time - conn['start_time'] > TIMEOUT_THRESHOLD:
            print(f"[!!!] Long POST атака: {ip_src} -> {ip_dst} ({current_time - conn['start_time']:.1f} сек)")
            remove_connection(key)

    
    if tcp.flags & 0x01 or tcp.flags & 0x04:
        remove_connection(key)

def start_sniffing(port):
    """Запуск сниффера на указанном порту"""
    print(f"[*] Запуск анализатора HTTP POST Slow DoS на порту {port}...")
    print(f"[*] Параметры детекции:")
    print(f"    - Макс. активных POST с IP: {POST_THRESHOLD}")
    print(f"    - Макс. время запроса: {TIMEOUT_THRESHOLD} сек")
    print(f"    - Макс. задержка пакетов: {DELAY_THRESHOLD} сек")
    sniff(filter=f"tcp port {port}", prn=process_packet, store=0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Детектор HTTP POST Slow DoS атак")
    parser.add_argument("-p", "--port", type=int, default=80, help="Порт HTTP сервера")
    args = parser.parse_args()

    
    threading.Thread(target=cleanup_expired_connections, daemon=True).start()
    
    # Запуск перехвата трафика
    start_sniffing(args.port)