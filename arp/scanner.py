import scapy.all as scapy
import optparse


def Extract(lst):
    return [item["ip"] for item in lst]

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="Enter IP adress")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        print("[-] Please enter an ip address")
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad = broadcast/arp_request
    answered = scapy.srp(arp_req_broad, timeout=1, verbose=False)[0]
    print("IP\t\t\tMAC\t\t\t\tSTATUS\n-----------------------------------------------------------")
    client_list = []
    tx="10.0.2."
    for element in answered:
        client = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client)
        print(element[1].psrc + "\t\t" + element[1].hwsrc+"\t\tONLINE")
    online=Extract(client_list)
    for i in range(1,25):
        tx=tx+str(i)
        if tx not in online:
            print(tx+ "\t\t----------------- \t\tOFFLINE")
        tx = "10.0.2."


scan("10.0.2.1/24")