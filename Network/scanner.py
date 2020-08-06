import scapy.all as scapy
import optparse


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
    print("IP\t\tMAC\n-----------------------------------------------------------")
    client_list = []
    for element in answered:
        client = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)


option=get_arguments()
scan(option.ip)