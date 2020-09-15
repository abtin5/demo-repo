import socket
import threading  # for CLients wont need to wait for each other to get responce from server

HEADER = 64  # this is the lenght of the first msg sent to server by client that tell the next msg lenght
PORT = 5050
# SERVER = "192.168.43.163"
SERVER = socket.gethostbyname(socket.gethostname())  # return this pc ip
ADD = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(ADD)  # bind the ServerAdd + Port


def handle_client(conn, addr):
    print(f"New Connection, {addr} is connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr}] {msg}")
    conn.close()


def start():
    sock.listen()
    print(f"[Listening] {SERVER}")
    while True:

        conn, addr = sock.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections = {threading.activeCount() - 1}")


print("Server is starting...")
start()
