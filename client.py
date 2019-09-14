import socket
from threading import Thread


class Client:

    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.id = self.connect()

    # def receive(self):
    #     while True:
    #         try:
    #             msg = self.s.recv(1024).decode("utf8")
    #             print(msg)
    #         except socket.error as e:
    #             print("Error while receiving message: " + str(e))

    def connect(self):
        self.s.connect((self.host, self.port))
        return self.s.recv(1024).decode()
        # receiveThread = Thread(target=self.receive).start()
