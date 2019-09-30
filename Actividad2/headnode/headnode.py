import socket
import sys
import random
from threading import Timer
# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socka = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
datanodea_address=('datanodea',5001)
datanode2_address=('datanode2',5001)
datanode3_address=('datanode3',5001)
server_address = ('headnode', 5000)#Definir una address
print ('Partiendo en el ip %s puerto %s' % server_address)
sock.bind(server_address)# Unir el socket al puerto 5000
# Escuchar mensajes
socka.connect(datanodea_address)
sockb.connect(datanode2_address)
sockc.connect(datanode3_address)
dataa=socka.recv(5000)
datab=sockb.recv(5000)
datac=sockc.recv(5000)
print ('Recibido {!r}'.format(dataa),'Recibido {!r}'.format(datab),'Recibido {!r}'.format(datac))
sock.listen(1)
def run_check():
    mensaje="Operativo"
    socka.sendall(mensaje.encode('utf-8'))
    sockb.sendall(mensaje.encode('utf-8'))
    sockc.sendall(mensaje.encode('utf-8'))
    dataa=socka.recv(5000)
    datab=sockb.recv(5000)
    datac=sockc.recv(5000)

t=Timer(1.0, run_check)
t.start()
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
            print ('recibido "%s"' % data)
            if data:
            	mensaje= f"El mensaje recibido fue {data}"
            	connection.sendall(mensaje.encode('utf-8'))
            	r=random.randint(1,3)
            	if  r==1:
            	    socka.sendall(mensaje.encode('utf-8'))
            	    data=socka.recv(5000)
            	elif r==2:
            	    sockb.sendall(mensaje.encode('utf-8'))
            	    data=sockb.recv(5000)
            	else:
            	    sockc.sendall(mensaje.encode('utf-8'))
            	    data=sockc.recv(5000)
            	print('Recibido {!r}'.format(data))
            else:
                print ('no hay mas mensajes', client_address)
                break

    finally:
        # Cierra la conexion.
        connection.close()
        t.cancel()
        break
