# -*- coding:utf-8 -*-

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 4096
ADDR = (HOST, PORT)

udpClient = socket(AF_INET, SOCK_DGRAM)

while 1:
    data = input('> ')
    if not data:
        break
    udpClient.sendto(data.encode(), ADDR)

    data, ADDR = udpClient.recvfrom(BUFSIZE)

    if not data:
        break

    print(bytes.decode(data))

udpClient.close()
