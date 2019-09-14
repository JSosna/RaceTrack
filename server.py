import socket
from threading import Thread
import sys

clients = {}
addresses = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8080
server_ip = socket.gethostbyname(host)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))


def acceptConnections():
    id = 0
    while True:
        clientConnection, clientAddress = s.accept()
        print(clientAddress + " has connected to the server!")
        addresses[clientConnection] = clientAddress

        Thread(target=handleClient, args=(clientConnection, clientAddress, id)).start()

        id += 1


def handleClient(connection, address, id):
    clients[connection] = id
    print("Client got id: " + id)

    connection.send(str.encode(id))

    while True:




if __name__ == '__main__':
    s.listen(5)
    print("Waiting for connection...")
    t1 = Thread(target=acceptConnections)
    t1.start()
    t1.join()
