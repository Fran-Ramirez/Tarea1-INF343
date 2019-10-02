import socket
import sys
import struct
import threading 
# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('datanode3', 5001)#Definir una address
print ('Partiendo en el ip %s puerto %s' % server_address)
sock.bind(server_address)# Unir el socket al puerto 5000
# Escuchar mensajes
sock.listen(1)
def multireceiver():
    multicast = '224.1.1.1'
    multisock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    multisock.bind(('', 5003))
    g = socket.inet_aton(multicast)
    struc = struct.pack('4sL', g, socket.INADDR_ANY)
    multisock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, struc)
    print ('multireceiver')
    while True:
        multidata, address = multisock.recvfrom(5000)
        multisock.sendto('Operativo 3'.encode('utf-8'), address)
threading.Thread(target=multireceiver).start()
while True:
    # Esperar una conexion
    print ( 'Esperando una conexion')
    connection, client_address = sock.accept()
    try:
        print ('Conexion desde', client_address)
        #Recibe mensajes hasta que no hayan mas
        while True:
            multidata, address = multisock.recvfrom(5000)
            if multidata:
                multisock.sendto(b'Operativo', address)
            data = connection.recv(64)
            print ('recibido "%s"' % data)#Escribir en data.txt
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
