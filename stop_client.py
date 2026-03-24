import socket

HOST = "192.168.248.114"
PORT = 9003

# mensagem = input("[Cliente] Mensagem: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    

    print(f"[Server] " , cliente.recv(1024).decode("utf-8"))
    cliente.sendall(input("Nome: ").encode("utf-8"))
    cliente.sendall(input("Cor: ").encode("utf-8"))
    cliente.sendall(input("C/E/P: ").encode("utf-8"))
    cliente.sendall(input("MSE: ").encode("utf-8"))
    print(cliente.recv(1024).decode("utf-8"))