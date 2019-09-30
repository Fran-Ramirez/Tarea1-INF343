FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3
RUN cd /usr/local/bin

ADD client.py /client/

WORKDIR /client/
