# 服务端接收数据的缓冲区
# 如果客户端发送给服务端的数据过多，需要分多次读取，每次最多读取
# 缓冲区尺寸的数据，bufferSize。
# bufferSize = 2


# 服务端代码
from socket import *
host = ""
bufferSize = 2
port = 9876
addr = (host,port)
# ipv4,tcp
tcpServerSocket = socket(AF_INET,SOCK_STREAM)
tcpServerSocket.bind(addr)
tcpServerSocket.listen()
print("Server Port:9876")
print('正在等待客户端的连接')

tcpClientSocket,addr = tcpServerSocket.accept()
print("客户端已经连接","addr = ",addr)

fullDateBytes = b""

while True:
    # 每次最多读取两个字节的数据
    data = tcpClientSocket.recv(bufferSize)
    fullDateBytes += data
    if len(data) < bufferSize:
        break
print(fullDateBytes)
print(fullDateBytes.decode("ISO-8859-1")) # ASCII
tcpClientSocket.close()
tcpServerSocket.close()

