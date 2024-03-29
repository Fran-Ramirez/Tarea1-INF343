import socket
import sys
import os

print("Inicializando cliente")
# Se crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connectar el socket con el puerto en el que el servidor esta escuchando
server_address = ('headnode', 5000)
print ('Conectando a %s por el puerto %s' % server_address)
sock.connect(server_address)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

file = open("registro_cliente.txt", "a")
file.write('Conectando a '+str(IPAddr)+' por el puerto '+str(server_address[1])+'\n')
file.close()
print('Conectado a '+str(IPAddr)+' por el puerto '+str(server_address[1]))

#Recibir confirmacion de Conexion al servidor
data = sock.recv(1024)
print('Servidor confirma conexion: \n recibido {!r}'.format(data))
try:
    # Enviar primer mensaje codificado con utf-8.
    message = 'Mensaje de prueba'
    print ('Enviando "%s"' % message)
    sock.sendall(message.encode('utf-8'))

    # Esperando respuesta
    data = sock.recv(1024)
    print('Servidor envia el siguiente mensaje: \n Recibido ' + '{!r}'.format(data))
    file = open("registro_cliente.txt", "a")
    file.write('[Respuesta del servidor]' + '{!r}'.format(data)+ '\n\n')
    file.close()

# Avisar el cierre del socket y cerrarlo.
finally:
    print ('Cerrando socket')
    sock.close()
