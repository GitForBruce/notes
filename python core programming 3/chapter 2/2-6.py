# -*- coding:utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 4096
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
# udpSerSock.listen(128)

while True:
    print("waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    print("server received %s at %s" % (data.decode(), ctime()))

    buf = '[' + ctime() + ']' + data.decode()
    udpSerSock.sendto(buf.encode(), addr)

udpSerSock.close()

