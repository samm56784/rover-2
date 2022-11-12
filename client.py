import socket
import os
import subprocess

s = socket.socket()
host = '192.168.2.212'
port = 9999

s.connect((host, port))

while True:
    commande = input()
    s.send(str.encode(commande))
    if commande == "q":
        s.close()


