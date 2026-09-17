#!/usr/bin python3 //indica el sistema operativo que se debe usar para interpretar.

import socket #importa el modulo socket, necesario para trabajar con redes

Host = "" #define la variable host y le asigna la direccion de red donde estara el Servidor
PORT = 65432 #especifica el numero de puerto TCP en el que el servidor estara escuchando. los puertos encima de 1024 no son privilegiados 
buffer_size = 1024 #define el tamano en bytes de los datos que el servidor leera en cada llamada. 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket: 
#crea el socket del servidor usando el contexto with (asegura el cierre automatico de la conexion)
#AF_INET indica IPv4 y SOCK_STREAM indica el protocolo TCP
    TCPServerSocket.bind((Host,PORT)) #enlaza el socket a la direccion IP y puerto especificados como tupla
    TCPServerSocket.listen(5) #pone al servidor en escucha, el 5 representa el tamano de la cola de conexiones entrantes pendientes antes de ser rechazadas
    print("El servidor TCP esta disponible y en espera de solicitudes") #imprime el mensaje de que el servidor ya esta activo.
    Client_conn, Client_addr = TCPServerSocket.accept() #bloquea la ejecucion hasta que llega un cliente, devuelve dos elementos un nuevo objeto socjet cliente_conn, para cominicarse exclusivamente con ese cliente y si direccion client_addr

#crear objeto thread (client_conn) codigo de un solo hilo y sincrono
with Client_conn: #abre un bloque de contexto para asegurar que la conexion con el cliente se cierre automaticamente
    print("conectado a", Client_addr) #muestra la ip y el puerto de origen del cliente que se acaba de conectar
    while True: #inicia un bucle infinito para mantener la comunicacion activa y seguir recibiendo mensajes continuos del cliente.
        print("esperando a recibir datos")
        data = Client_conn.recv(buffer_size) #pausa el programa y lee hasta 1024 bytes de datos 
        print("recibido", data," de ") #imprime los datos recibidos
        if not data: #comprueba si el cliente cerro la conexion
            break #rompe el while 
        print("enviando respuesta a ", Client_addr)
        Client_conn.sendall(data) #devuelve los datos recibidos "eco"
