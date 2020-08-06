import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url=str(packet[http.HTTPRequest].Host+packet[http.HTTPRequest].Path)
        real=url[2:len(url)-1]
        display=True
        unnecessary = [".png",".css",".woff",".js",".zip",".php",".txt",".exe","microsoft",".icon"]
        for i in unnecessary:
            if i in real:
                display=False
                break
        if display:
            print("\n[+]  HTTP Request >>"+real)

sniff("eth0")