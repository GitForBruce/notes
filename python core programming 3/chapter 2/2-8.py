# -*- coding:utf-8 -*-

"""
仅支持单个客户端连接
"""
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write(('[%s] %s' %(ctime(), self.rfile.readline().decode())).encode())

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()

