import socket
import sys
import struct
import threading

import os
#crear archivo
file = open("data.txt", "a")
file.close()

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('datanode1', 5001)#Definir una address
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
    while True:
        multidata, address = multisock.recvfrom(1024)
        multisock.sendto('Operativo 1'.encode('utf-8'), address)

threading.Thread(target=multireceiver).start()
while True:
# Esperar una conexion
print ( 'Esperando una conexion')
connection, client_address = sock.accept()
try:
    print('Conexion desde', client_address)
    #Recibe mensajes hasta que no hayan mas
    multidata, address = multisock.recvfrom(1024)
    if multidata:
        multisock.sendto(b'Operativo', address)
    data = connection.recv(1024)
    print ('recibido "%s"' % data)#Escribir en data.txt
    file = open("data.txt", "a")
    file.write('[Mensaje del cliente]'+str(data)+'\n\n')
    file.close()
    if data:
        mensaje= f"El mensaje recibido fue {data}"
        connection.sendall(mensaje.encode('utf-8'))
    else:
        print ('no hay mas mensajes', client_address)
        break

finally:
    # Cierra la conexion.
    connection.close()
    #break
