# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #pede a liberação
    s.listen(1) #começa a usar

    print("[server] aguardando jogador1")
    conn, addr = s.accept() #ponto de sincronização
    print("[server] aguardando jogador2")
    conn2, addr2 = s.accept()
            
    conn.sendall("[server] OK. Você é o jogador 1".encode())
    conn2.sendall("[server] OK. Você é o jogador 2".encode())

    ganhador = None

    msg1 = s.recv(1024).decode()
    print("jogador1 jogou", msg1)
    msg2 = s.recv(1024).decode()
    print("jogador2 jogou", msg2)

    if(msg1 == msg2):
        print("empate")
    elif(msg1 == "papel"):
        if(msg2 == "pedra"):
            
        if(msg2 == "tesoura"):




    conn.close()
    conn2.close()