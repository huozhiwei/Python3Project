# 客户端Socket
# 连接demo04 tcp服务端时间戳服务器

from socket import *
host = "localhost"
port = 1234
buffetSize = 1024
# 服务端的地址和端口号
addr = (host,port)
# ipv4, tcp
tcpClientSocket = socket(AF_INET,SOCK_STREAM)
# 通过connect方法连接服务端的地址和端口号
tcpClientSocket.connect(addr)
while True:
    data = input(">")
    if not data:
        break
    data = data.encode(encoding="utf-8")
    tcpClientSocket.send(data)
    dataRecv = tcpClientSocket.recv(buffetSize)
    print(dataRecv.decode('utf-8'))
tcpClientSocket.close()