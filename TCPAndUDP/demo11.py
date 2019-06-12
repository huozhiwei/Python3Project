# demo10 的客户端程序
from socket import *

host = "localhost"
port = 9999
bufferSize = 1024 # bytes
addr = (host,port)
# ipv4,UDP
udpClientSocket = socket(AF_INET, SOCK_DGRAM)
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
