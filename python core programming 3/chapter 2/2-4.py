# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break

    tcpCliSock.send(data.encode())
    print("client sent data at %s" % ctime())
    
    data = tcpCliSock.recv(BUFSIZE).decode()
    print("client received received %s at %s" % (data, ctime()))

    if not data:
        break
    print(data)

tcpCliSock.close()