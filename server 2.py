import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
addr = (SERVER,PORT)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(addr)

def client_handle(conn, addr):
    pass


def start():
    sock.listen()
    while():
        conn, addr = sock.accept()
        thread = threading.Thread(target=client_handle, args=(conn,addr))
        thread.start()
        print(f"")

print("Server is Running:")
start()