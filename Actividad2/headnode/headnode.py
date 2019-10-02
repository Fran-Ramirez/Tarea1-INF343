import socket
import sys
import random
import threading 
import time
import struct

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
# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('headnode', 5000)#Definir una address
print ('Partiendo en el ip %s puerto %s' % server_address)
sock.bind(server_address)# Unir el socket al puerto 5000
# Escuchar mensajes
sock.listen(1)
def run_check():
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
                data, server = multisock.recvfrom(16)

            except socket.timeout:
                    break
            else:
                print (data.decode("utf-8") + "\n")#Heartbeat_register         
    finally:        
        multisock.close()

t=RepeatedTimer(0.3, run_check)
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
                r=random.randint(1,3)
                datanode_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                datanode_address=('datanode'+r,5001)
                datanode_sock.connect(datanodea_address)
                mensaje= f"El mensaje recibido fue {data} enviado al Datanode{r}"
                data=datanode_sock.recv(5000)
                if data:
                    connection.sendall(mensaje.encode('utf-8'))
                    print('Recibido {!r}'.format(data))#Escribir en registro_server :'Mensaje guardado en Datanode'+r
            else:
                print ('no hay mas mensajes', client_address)
                break
    finally:
        # Cierra la conexion.
        connection.close()
        t.stop()
        break
