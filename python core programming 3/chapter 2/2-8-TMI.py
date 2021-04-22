# -*- coding:utf-8 -*-
"""
支持多个客户端连接
"""
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH, ThreadingMixIn as TMI)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class Server(TMI, TCP):
    pass

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write(('[%s] %s' %(ctime(), self.rfile.readline().decode())).encode())

tcpServ = Server(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()

