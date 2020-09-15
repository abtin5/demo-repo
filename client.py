import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#def send(message):
    