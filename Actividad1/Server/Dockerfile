FROM ubuntu:latest
RUN apt-get update 
RUN apt-get install -y python3
RUN cd /usr/local/bin 
RUN ln -s /usr/bin/python3 python 
ADD server.py /server/
