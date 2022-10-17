from scapy.all import * # install scapy if needed " apt install python3-scapy "

interface = "eth0" # change according to your network interface name
ip_range = "10.10.X.X/24" # change according to your local IP block
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range) 

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
