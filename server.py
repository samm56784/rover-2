import socket
import sys
#from main import *

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.1.100" #fonction trouver adresse machine
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

def requests_management(choix):
    #choix.upper()
    if choix == b's':
        print("Start")
        #start
    elif choix == b'f':
        print("Forward")
        #forward
    elif choix == b'r':
        print("Return")
        #return
    elif choix == b'p':
        print("Pause")
        #pause
    elif choix == b'b':
        print("Backward")
        #backward
    else:
        return
    return choix


def recv_input():
    request = conn.recv(1024)
    return request
        #print(request)

def initialisation():
    create_socket()
    bind_socket()
    socket_accept()

'''def looprecv():
    request = b'o'
    while request !=b'q':
        request =recv_input()
    conn.close()'''