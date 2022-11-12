import socket
import sys
#from main import *

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.2.212" #fonction trouver adresse machine
        #client -> scanner adresses pour trouver le serveur en lui feedant le port
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        print("bind done")
        s.listen(5)
        print("listen done")

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    global conn
    conn, address = s.accept()
    print("accept done")
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    #send_commands(conn)
   # conn.close()

# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
#def recv_commands(conn):
    #request = conn.recv(1024)


def main():
    request = "a"
    create_socket()
    bind_socket()
    socket_accept()
    while request != "q":
        request = conn.recv(1024)
        print(request)

    conn.close()



main()

