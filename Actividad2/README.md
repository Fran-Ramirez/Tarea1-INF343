Para desplegar la arquitectura se deben usar los siguientes comando tras ingresar a la carpeta Actividad1:

-sudo docker-compose build

-sudo docker-compose up

Para mantener el servidor en constante estado de espera es necesario ejecutar el cliente desde otra terminar y seguir los siguientes pasos:

1. Entrar por terminal a la carpeta Actividad2/client

2. Ejecutar los siguientes comandos

  -sudo docker exec -it actividad2_client_1 bash

  -python3 client.py

3. El ultimo comando se puede ejecutar repetidas veces y se ejecutará el cliente quien enviará un mensaje genérico de prueba

Importante:

actividad2_client_1 es el nombre del contenedor, para verificar que el nombre es el correcto y no cambia usar el comando:

  -sudo docker ps
 
 Con el comando anterior se podrán ver los nombres de todos los contenedores.

La ruta de los archivos son las siguientes:

-Actividad2/headnode/hearbeat_server.txt

-Actividad2/headnode/registro_server.txt

-Actividad2/client/registro_cliente.txt

-Actividad2/datanode1/data.txt

-Actividad2/datanode2/data.txt

-Actividad2/datanode3/data.txt

Para recuperar la arquitectura de cualquier error ejecutar el siguiente comando:

-sudo docker-compose down
