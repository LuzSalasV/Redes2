#!/usr/bin/env python3
import socket

HOST = "localhost"
PORT = 65432
buffer_size = 1024

# Creación del socket sin la cláusula 'with'
TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPServerSocket.bind((HOST, PORT))
TCPServerSocket.listen(1)

print("El servidor TCP está disponible y en espera de solicitudes...")

Client_conn, Client_addr = TCPServerSocket.accept()
print("Conectado a", Client_addr)

while True:
    data = Client_conn.recv(buffer_size)
    if not data:
        break

    mensaje = data.decode("utf-8")
    print("Recibido:", mensaje)

    # Analiza el fin de transferencia para responder y cerrar
    if mensaje.strip().lower() == "adiós" or mensaje.strip().lower() == "adios":
        respuesta = "Hasta luego."
        Client_conn.sendall(respuesta.encode("utf-8"))
        print("Servidor:", respuesta)
        break
    elif mensaje.strip() == "Hola":
        respuesta = "Hola, cliente."
    else:
        respuesta = "Mensaje recibido."

    Client_conn.sendall(respuesta.encode("utf-8"))
    print("Servidor:", respuesta)

# Cierre manual de sockets
Client_conn.close()
TCPServerSocket.close()
print("Conexión finalizada.")
