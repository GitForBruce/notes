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
        # # readline()函数得到客户消息，用write()函数把字符串发给客户
        self.wfile.write(('[%s] %s' %(ctime(), self.rfile.readline().decode())).encode())

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()

