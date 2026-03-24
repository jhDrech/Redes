import socket
import threading
from time import sleep

HOST = "0.0.0.0"
PORT = 9002
LETRA = "T"

semaforo = threading.Semaphore(0)

def atender_cliente(conn, addr):
    global CEP
    global NOME
    semaforo.acquire()
    with conn:
        conn.sendall(LETRA.encode())

        conn.sendall("CEP: ".encode())
    pass

    print(f"[Server] Conexão encerrada {addr}", flush=True)


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"Servidor ouvindo em {HOST}:{PORT}")

        conn_1, addr_1 = server.accept()
        thread_1 = threading.Thread(target=atender_cliente, args=(conn_1, addr_1), daemon=True)
        thread_1.start()

        conn_2, addr_2 = server.accept()
        thread_2 = threading.Thread(target=atender_cliente, args=(conn_2, addr_2), daemon=True)
        thread_2.start()

        #sorteia a letra



if __name__ == "__main__":
    iniciar_servidor()