import socket
from main import main


HOST = '192.168.27.27'  # The server's hostname or IP address
PORT = 5002        # The port used by the server

s = socket.socket()
s.connect((HOST, PORT))

def receive():
    while True:
        text = s.recv(1024)
        print(text.decode())
        send(map=text.decode())

def send(map):
    text = main(map)#"ROB:15,15;OBS1:45,125,0;OBS2:135,155,270;OBS3:105,105,180;OBS4:145,45,90")
    s.send(text.encode())

if __name__ == '__main__':
    receive()



        