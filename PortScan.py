from http import server
import socket
from datetime import datetime

Server = input("IP Adresi girin: ")
ServerIp = socket.gethostbyname(Server)


print("-" * 50)
print("Taranan Hedef: " + Server)
zaman1 = print("Tarama Saati:" + str(datetime.now()))
print("-" * 50)

for port in range(1,10):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((ServerIp,port))
    if result == 0:
        f = open(Server + "Açık Portlar.txt", "a")
        print("Port {}: Open\n".format(port))
        f.write("Port {}: Open\n".format(port))
    else:
        f = open(Server + "Kapalı Portlar.txt", "a")
        print("Port {}: Close\n".format(port))
        f.write("Port {}: Close\n".format(port))
    sock.close()

