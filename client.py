# Cliente
import socket

HOST = "192.168.246.31"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input()
        s.sendall(msg.encode('utf-8'))
        print(s.recv(1024).decode())