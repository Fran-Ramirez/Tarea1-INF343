import socket
import sys
import os
from datetime import datetime

#hora logs
time = datetime.now()
actual = time.strftime("%Y-%m-%d %H:%M:%S")

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('server', 5000)#Definir una address
print ('Partiendo en el ip %s puerto %s' % server_address)
sock.bind(server_address)# Unir el socket al puerto 5000
# Escuchar mensajes
sock.listen(1)

while True:
    # Esperar una conexion
    print ( 'Esperando una conexion')
    connection, client_address = sock.accept()
    file = open("log.txt", "a")
    file.write('['+ actual+']Cliente '+str(client_address[0])+' intentando conectarse\n')
    file.close()
    try:
        file = open("log.txt", "a")
        file.write('['+ actual+']Conexion exitosa con '+str(client_address[0])+'\n')
        print ('Conexion desde', str(client_address[0]))
        connection.sendall('Estas conectado con server'.encode('utf-8'))
        file.write('['+ actual+']Se envia mensaje de confirmacion a '+str(client_address[0])+'\n')
        file.close()
        #Recibe mensajes hasta que no hayan mas
        data = connection.recv(1024)
        print ('recibido %s' % data)
        file = open("log.txt", "a")
        file.write('['+ actual+']Mensaje recibido de '+str(client_address[0])+' : {!r}'.format(data) + '\n\n')
        file.close()
        if data:
        	mensaje = 'El mensaje recibido de '+str(client_address[0])+' fue '+str(data)+'\n'
        	connection.sendall(mensaje.encode('utf-8'))
        else:
            print ('no hay mas mensajes', client_address)
            break

    finally:
        # Cierra la conexion.
        file = open("log.txt", "a")
        print("Cerrando conexion...\n\n")
        file.close()
        connection.close()
        #break
