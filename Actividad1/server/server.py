import socket
import sys

import os
from datetime import datetime

#Se crea el archivo de logs
file = open("logs.txt", "a")

#hora logs
time = datetime.now()
actual = time.strftime("%H:%M:%S")

file.write('['+ actual+']Iniciando...\n')
file.close()

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('server', 5000)#Definir una address
print ('Partiendo en el ip %s puerto %s' % server_address)
sock.bind(server_address)# Unir el socket al puerto 5000
# Escuchar mensajes
sock.listen(1)

file = open("logs.txt", "a")
file.write('['+ actual+']Partiendo en el ip {} puerto {}'.format(*server_address) + '\n')
file.close()

while True:
    # Esperar una conexion
    print ( 'Esperando una conexion')
    file = open("logs.txt", "a")
    file.write('['+ actual+']Esperando una conexion...\n')
    file.close()
    connection, client_address = sock.accept()
    try:
        print ('Conexion desde', client_address)
        connection.sendall("Estas conectado con server".encode('utf-8'))
        file = open("logs.txt", "a")
        file.write('['+ actual+']Confirmando conexion \n')
        #Recibe mensajes hasta que no hayan mas
        while True:
            data = connection.recv(64)
            print ('recibido "%s"' % data)
            file.write('['+ actual+']Mensaje del cliente: {!r}'.format(data) + '\n')
            if data:
            	mensaje= f"El mensaje recibido fue {data}"
            	connection.sendall(mensaje.encode('utf-8'))
            else:
                print ('no hay mas mensajes', client_address)
                break
            file.write('['+ actual+']Enviando mensaje...\n')
            file.close()

    finally:
        # Cierra la conexion.
        file = open("logs.txt", "a")
        file.write("[" + actual + "] Cerrando conexion...\n\n")
        file.close()
        connection.close()
        break
