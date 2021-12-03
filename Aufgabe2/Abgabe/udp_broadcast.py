import socket
import time
import threading
import psutil

class UDPBroadcast:

    def start_loop(self):
        print("Broadcast-Loop started!")
        while(True):
            for IP in self.get_broadcast():

                UDP_PORT = 9876
                MESSAGE = "Dieser Server wurden von der Gruppe 2 implementiert und stellt die\nFibonacci-Funktion als Dienst bereit. Um den Dienst zu nutzen, senden Sie eine\nNachricht an Port 65432 auf diesem Server. Das\nFormat der Nachricht sollte folgendermaßen aussehen b'x' wobei x eine Zahl ist."
                print("Broadcast send to: ", IP)
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
                sock.sendto(bytes(MESSAGE, "utf-8"), (IP, UDP_PORT))
            print("-----")
            time.sleep(5)

    def get_intf(self):
        addrs = psutil.net_if_addrs()
        for key in addrs:
            print(key,'->', addrs[key][1][0],addrs[key][1][1],addrs[key][1][2])
            
    def get_broadcast(self):
        addrs = psutil.net_if_addrs()
        interfaces =[]
        for key in addrs:
            x = addrs[key][1][2]
            if x is not None:
                netmaskc = x.count('.0')
                ip = addrs[key][1][1]
                split= ip.split('.',4-netmaskc)
                ip=""
                for h in range(4-netmaskc):
                    if ip == "":
                        ip = split[h]
                    else:
                        ip = ip+'.'+split[h]
                #     ip =ip + split[h]
                for x in range(netmaskc):
                    ip = ip +'.255'
                interfaces.append(ip)
        return interfaces

