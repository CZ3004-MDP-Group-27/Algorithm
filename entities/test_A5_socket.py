import socket
import threading
from test_A5 import calcPath

HOST = '192.168.27.27'  # The server's hostname or IP address
PORT = 5009        # The port used by the server

distance = 60

s = socket.socket()
s.connect((HOST, PORT))


# def receive():
#     while True:
#         text = s.recv(1024)
#         print(text.decode())

def send():
    instructions = calcPath(60)
    s.send(instructions.encode())
    s.close()

#threading.Thread(target=receive).start()
send()



        