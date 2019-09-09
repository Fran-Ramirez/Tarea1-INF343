# -*- coding: cp1252 -*-
import socket
import sys

# Se crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#se escoje un puerto para enviar la informacion.
sock.bind(('0.0.0.0',50001))
# Connectar el socket con el puerto en el que el servidor esta escuchando
server_address = ('192.168.43.113', 1234)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
#Recibir confirmacion de Conexion al servidor
data = sock.recv(64)
print (sys.stderr, 'received "%s"' % data)
try:
    # Enviar primer mensaje codificado con utf-8.
    message1 = 'Hola, carcamo.'
    print (sys.stderr, 'sending "%s"' % message1)
    sock.sendall(message1.encode('utf-8'))
    # Enviar segundo mensaje codificado con utf-8.
    message2 = 'Que tal?'
    print (sys.stderr, 'sending "%s"' % message2)
    sock.sendall(message2.encode('utf-8'))

# Avisar el cierre del socket y cerrarlo.
finally:
    print (sys.stderr, 'closing socket')
    sock.close()
