import socket
import sys

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.43.113', 1234)#Definir una address
print (sys.stderr,'Partiendo en el ip %s puerto %s' % server_address)
sock.bind(server_address)# Unir el socket al puerto 1234
# Escuchar mensajes
sock.listen(1)

while True:
    # Esperar una conexion
    print ( 'Esperando una conexion')
    connection, client_address = sock.accept()
    try:
        print ('Conexion desde', client_address)
        connection.sendall("Estas conectado con Carcamo".encode('utf-8'))

        #Recibe mensajes hasta que no hayan mas
        while True:
            data = connection.recv(64)
            print (sys.stderr, 'recibido "%s"' % data)
            if data:
            	continue
            else:
                print (sys.stderr, 'no hay mas mensajes', client_address)
                break

    finally:
        # Cierra la conexion.
        connection.close()
