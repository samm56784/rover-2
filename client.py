import socket
import os
import subprocess

s = socket.socket()
host = '192.168.209.129'
port = 9999

s.connect((host, port))
continuer = True
while continuer:
    commande = input()
    s.send(str.encode(commande))
    if commande == "q":
        continuer = False
        s.close()


