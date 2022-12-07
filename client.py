import socket
import os
import subprocess
import tkinter as tk
connected = False
s = socket.socket()
sub_ip = "192.168.1."
it = 103
host = sub_ip + str(it)
port = 9999
s.connect((host, port))


def envoyer_commande(commande):
    s.send(commande)
    print(commande)
    return
def quit():
    s.close()
    app.destroy()

app = tk.Tk()
app.title('app_Rover')
button1 = tk.Button(app, text="Arrêter",state=tk.NORMAL,command = lambda :envoyer_commande(b'q'))
button1.grid(row=0,column=0)
button2 = tk.Button(app, text="Avancer rapide",state=tk.NORMAL,command = lambda :envoyer_commande(b'w'))
button2.grid(row=2,column=0)
button3 = tk.Button(app, text="Reculer vite",state=tk.NORMAL,command = lambda :envoyer_commande(b's'))
button3.grid(row=3,column=0)
button4 = tk.Button(app, text="Tourner à droite",state=tk.NORMAL,command = lambda :envoyer_commande(b'd'))
button4.grid(row=3,column=0)
button5 = tk.Button(app, text="Tourner à gauche",state=tk.NORMAL,command = lambda :envoyer_commande(b'a'))
button5.grid(row=3,column=0)
button6 = tk.Button(app, text="Automatique",state=tk.NORMAL,command = lambda :envoyer_commande(b'o'))
button6.grid(row=5,column=0)
button7 = tk.Button(app, text="Quitter",state=tk.NORMAL,command = quit)
button7.grid(row=0,column=7)

app.mainloop()

