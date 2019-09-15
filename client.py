import socket


class Client:

    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.id = self.connect()

    def connect(self):
        self.s.connect((self.host, self.port))
        return self.s.recv(1024).decode()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            self.s.send(str.encode(data))
            reply = self.s.recv(1024).decode()
            return reply
        except socket.error as err:
            print("Error in function 'send' in client.py" + str(err))
