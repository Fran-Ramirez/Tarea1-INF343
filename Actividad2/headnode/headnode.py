import socket
import sys
import random
import threading
import time
import struct

import os
from datetime import datetime



class RepeatedTimer(object):
  def __init__(self, interval, function, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False

#Creacion archivos
file1 = open("hearbeat_server.txt", "a")
file1.close()
file2 = open("registro_server.txt", "a")
file2.close()

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('headnode', 5000)#Definir una address
print ('Partiendo en el ip %s puerto %s' % server_address)
sock.bind(server_address)# Unir el socket al puerto 5000
# Escuchar mensajes
sock.listen(1)
def run_check():
    timer = datetime.now()
    actual = time.strftime("%Y-%m-%d %H:%M:%S")
    multisock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    multisock.settimeout(0.2)
    ttl = struct.pack('b', 1)
    multisock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    multicast = ('224.1.1.1', 5003)
    mensaje="Operativo?"
    try:
        # Envío de mensaje al grupo multicast
        sent = multisock.sendto(mensaje.encode('utf-8'), multicast)
        x=0
        while True:
            try:
                data, server = multisock.recvfrom(1024)

            except socket.timeout:
                    break
            else:
                print(data.decode("utf-8") + "\n")#Heartbeat_register
                file1 = open("hearbeat_server.txt", "a")
                file1.write('[Estado '+actual+' ] '+str(data)+'\n')
                file1.close()
    finally:
        multisock.close()

t=RepeatedTimer(5, run_check)

### Conexion cliente ###
while True:
    # Esperar una conexion
    print ( 'Esperando una conexion')
    connection, client_address = sock.accept()
    try:
        print ('Conexion desde', str(client_address[0]))
        connection.sendall("Estas conectado con headnode".encode('utf-8'))
        #Recibe mensajes hasta que no hayan mas
        data = connection.recv(1024)
        print ('recibido %s' % data)

        if data:
            r = random.randint(1,3)
            datanode_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            datanode_address=('datanode'+str(r),5001)
            datanode_sock.connect(datanode_address)

            file = open("registro_server.txt", "a")
            file.write('El cliente '+str(client_address[0])+' envio el mensaje:\n '+str(data)+'\n que fue guardado en el datanode'+str(r)+'\n \n')
            file.close()

            mensaje = 'El mensaje recibido de '+str(client_address[0])+' fue '+str(data)+'que fue guardado en el datanode'+str(r)+'\n'
            connection.sendall(mensaje.encode('utf-8'))

            data2=datanode_sock.recv(1024)
            if data2:
                connection.sendall(mensaje.encode('utf-8'))
                print('Recibido {!r}'.format(data2))
        else:
            print ('no hay mas mensajes', client_address)
            break
    finally:
        file1 = open("hearbeat_server.txt", "a")
        file1.write('\n')
        file1.close()
        # Cierra la conexion.
        print("Cerrando conexion...\n\n")
        connection.close()
        t.stop()
        #break
