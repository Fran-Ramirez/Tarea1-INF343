import socket
import sys

import os

#Se crea el archivo de respuestas
file = open("./respuestas.txt", "w")

# Se crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#se escoje un puerto para enviar la informacion.
sock.bind(('0.0.0.0',5000))
# Connectar el socket con el puerto en el que el servidor esta escuchando
server_address = ('server', 5000)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)
#Recibir confirmacion de Conexion al servidor
data = sock.recv(64)
print('Recibido {!r}'.format(data))
#guardar el mensaje Recibido
file.write(str(data))
try:
    # Enviar primer mensaje codificado con utf-8.
    message = 'Mensaje de prueba'
    print ('sending "%s"' % message)
    sock.sendall(message.encode('utf-8'))

    # Esperando respuesta
    data = sock.recv(5000)
    print('Recibido {!r}'.format(data))
    file.write(str(data))
    message_new = ''

# Avisar el cierre del socket y cerrarlo.
finally:
    print ('closing socket')
    sock.close()
    file.close()
