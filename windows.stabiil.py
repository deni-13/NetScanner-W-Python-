#Last Update #windows' girince 

import scapy.all as scapy
#first arp request
arp_rq=scapy.ARP(pdst="10.0.2.1/24")  #istek olusturdum
#scapy.ls(scapy.ARP())
#second step: broadcast

#broadcast_packet = scapy.Ether()
broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #gidilcek yer #string

combined_packet = broadcast_packet/arp_rq
#iki paketi al tek paket yap!!

(answered_list,unans_list)=scapy.srp(combined_packet,timeout=1) #sendandreqpacketsbirlesik fonk
answered_list.summary() #scapy sagolsun 
