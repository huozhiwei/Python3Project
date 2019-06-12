# 时间戳服务器

from socket import *
from time import ctime # currentTime

host = ""
bufferSize = 1024 # bytes
port = 1234
addr = (host, port)
# ipv4,tcp
tcpServerSocket = socket(AF_INET,SOCK_STREAM)
tcpServerSocket.bind(addr)
print(addr,"服务端的ip以及端口号")
tcpServerSocket.listen(5)
while True:
    print("正在等待客户端连接")
    tcpCLientSocket,addr_1 = tcpServerSocket.accept()
    print("客户端已经连接","addr = ",addr_1)
    print(addr, "服务端的ip以及端口号")
    while True:
        data = tcpCLientSocket.recv(bufferSize)
        if not data:
            break
        tcpCLientSocket.send(ctime().encode(encoding="utf-8") + b" " + data)
    tcpCLientSocket.close()
tcpServerSocket.close()

