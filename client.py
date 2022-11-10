import socket
import os
import subprocess

s = socket.socket()
host = '172.16.14.185'
port = 9999

s.connect((host, port))

while True:
    commande = s.recv(1024)


    if len(commande) > 0:
        print(commande)
        if commande == b'2':
            print("gg")

