import socket
import sys

import os
#Se crea el archivo de respuestas
file = open("respuestas.txt", "a")
file.write("Inicializando cliente...\n")
print("Inicializando cliente")

# Se crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#se escoje un puerto para enviar la informacion.
sock.bind(('0.0.0.0',5000))
# Connectar el socket con el puerto en el que el servidor esta escuchando
server_address = ('server', 5000)
print ('conectando a %s por el puerto %s' % server_address)
file.write('conectando a {} por el puerto {}'.format(*server_address) + "\n")
sock.connect(server_address)

#Recibir confirmacion de Conexion al servidor
data = sock.recv(64)
print('Recibido {!r}'.format(data))
file.write("Servidor confirma conexion: " + '{!r}'.format(data)+ "\n")
file.close()
try:
    # Enviar primer mensaje codificado con utf-8.
    file = open("respuestas.txt", "a")
    message = 'Mensaje de prueba'
    print ('Enviando "%s"' % message)
    file.write("Enviando mensaje de prueba al servidor...\n")
    sock.sendall(message.encode('utf-8'))

    # Esperando respuesta
    data = sock.recv(5000)
    print('Recibido {!r}'.format(data))
    file.write("Servidor envia respuesta: " + '{!r}'.format(data)+ "\n")

    file.close()
# Avisar el cierre del socket y cerrarlo.
finally:
    file = open("respuestas.txt", "a")
    print ('cerrando socket')
    file.write('cerrando socket...\n\n')
    sock.close()
    file.close()
