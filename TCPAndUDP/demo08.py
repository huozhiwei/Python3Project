# UDP时间戳客户端
# 连接demo07 udp服务端时间戳服务器

from socket import *

host = "localhost"
port = 9876
bufferSize = 1024
addr = (host,port)
# ipv4,udp（数据报协议）
udpClientSocket = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input(">")
    if not data:
        break
    udpClientSocket.sendto(data.encode(encoding='utf-8'),addr)
    data,addr = udpClientSocket.recvfrom(bufferSize)
    if not data:
        break
    print(data.decode('utf-8'))

udpClientSocket.close()
