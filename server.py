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
    while True:
        clientConnection, clientAddress = s.accept()
        print(clientAddress + " has connected to the server!")
        addresses[clientConnection] = clientAddress
        Thread(target=handleClient, args=(clientConnection, clientAddress)).start()


def handleClient(connection, address):
    pass


if __name__ == '__main__':
    s.listen(5)
    print("Waiting for connection...")
