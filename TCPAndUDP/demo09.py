# 实现socketserver TCP时间戳服务器

from socketserver import TCPServer as TCP,StreamRequestHandler as SRH
from time import ctime

host = ""
port = 9876
addr = (host,port)

class MyRequestHandler(SRH):
    def handle(self):
        print("客户端已经连接，地址",self.client_address)
        self.wfile.write(ctime().encode(encoding='utf-8') + b' ' + self.rfile.readline())

tcpServer = TCP(addr,MyRequestHandler)
tcpServer.serve_forever()
