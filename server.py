import socket
from threading import Thread

clients = {}
addresses = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8080
server_ip = socket.gethostbyname(host)

try:
    s.bind((host, port))
except socket.error as e:
    print("error while trying s.bind in server.py" + str(e))


players_positions = ["0:50,50", "1:100,100"]


def accept_connections():
    player_id = 0
    while True:
        client_connection, client_address = s.accept()
        # print(client_address + " has connected to the server!")
        # addresses[client_connection] = client_address

        Thread(target=handle_client, args=(client_connection, player_id)).start()

        player_id += 1


def handle_client(connection, player_id):
    # TODO: add possibility for more than 2 players (proper id handling and sending positions)

    global players_positions

    clients[connection] = player_id
    print("Client got id: ", player_id)

    connection.send(str.encode(str(player_id)))

    while True:
        try:
            data = connection.recv(1024).decode("utf8")
            if not data:
                connection.send(str.encode("Bye"))
                break
            else:
                print("Received: " + data)
                arr = data.split(":")
                sender_id = int(arr[0])
                players_positions[sender_id] = data

                if player_id == 0:
                    other_id = 1
                else:                       # player_id == 1:
                    other_id = 0

                reply = players_positions[other_id][:]
                print("Sending: " + reply)

            connection.sendall(str.encode(reply))
        except socket.error as err:
            print("Error while receiving position or sending it back (server.py)" + str(err))
            break

        print("Connection closed.")
        connection.close()


if __name__ == '__main__':
    s.listen(5)
    print("Waiting for connection...")
    t1 = Thread(target=accept_connections)
    t1.start()
    t1.join()
