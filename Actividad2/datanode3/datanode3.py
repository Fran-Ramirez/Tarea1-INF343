import socket
import sys
# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('datanode3', 5001)#Definir una address
print ('Partiendo en el ip %s puerto %s' % server_address)
sock.bind(server_address)# Unir el socket al puerto 5000
# Escuchar mensajes
sock.listen(1)
while True:
    # Esperar una conexion
    print ( 'Esperando una conexion')
    connection, client_address = sock.accept()
    try:
        print ('Conexion desde', client_address)
        connection.sendall("Estas conectado con Datanode3".encode('utf-8'))

        #Recibe mensajes hasta que no hayan mas
        while True:
            data = connection.recv(64)
            print ('recibido "%s"' % data)
            if data:
            	mensaje= f"El mensaje recibido fue {data}"
            	connection.sendall(mensaje.encode('utf-8'))
            else:
                print ('no hay mas mensajes', client_address)
                break

    finally:
        # Cierra la conexion.
        connection.close()
        break
