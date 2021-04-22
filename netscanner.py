import scapy .all as scapy
#first arp request
arp_rq=scapy.ARP(pdst="10.0.2.1/24")  #istek olusturdum
scapy.ls(scapy.ARP())
#second step: broadcast

broadcast_packet = scapy.Ether()
scapy.ls(scapy.Ether())  #listeleme broadcast yapabilceklerim

#Bu kodlar Python3'de çalısmaktadır.Dosya olarak attıgım scapy python3un içinde çünkü
#Çalısması için butun sanal makinelerin natnetworku aynı olmalı .
#These codes works stable in PY3.The folder that I send to Python3 is Scapy
#To work all of the VM has to be on the same NATnetwork. :D


#%%  #broadcast 

#scapy.ls(scapy.ARP())
#second step: broadcast

#broadcast_packet = scapy.Ether()
broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #gidilcek yer #string
#default mac adresimiz !!!class mantıgı !!!
combined_packet = broadcast_packet/arp_rq
#iki paketi al tek paket yap!!

result=scapy.srp(combined_packet,timeout=1)
print(result)

#%% list seklinde cast ettik broadcasti answered unsanswer

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
print(list(answered_list))

#%% Last Update #windows' girince 

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


#%% kodumuzu guzellestirelim 

#Beynım yandı
import scapy.all as scapy 
import optparse 

    def get_user_input():
        parse_object=optparse.OptionParser()
        parse_object.add_option(-"-i","ipaddres",dest="ip_add
        (user_input,arguments)= parse_object.parse_args()
        #tuple ()
        if not user_input.ipaddres:
            print("enter ip")
        return user_input


def scan_my_network(ip):
    arp_rq=scapy.ARP(pdst=pdst=ip)  #istek olusturdum
    broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #gidilcek yer #string

    combined_packet = broadcast_packet/arp_rq
    #iki paketi al tek paket yap!!

    (answered_list,unans_list)=scapy.srp(combined_packet,timeout=1) #sendandreqpacketsbirlesik fonk
    answered_list.summary() #scapy sagolsun 

user_ip_addres=get_user_input()
scan_my_network(user_ip_addres.ipp_addres)