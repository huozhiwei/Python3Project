# 服务端的请求队列

# Thread
# 在两次调用accept方法之间，会有一段时间,20ms

# 请求队列根据操作系统的不同，存储客户端Socket是有上限的，linux:128

# 服务端代码
from socket import *
host = ""
bufferSize = 1024
port = 9876
addr = (host,port)
# ipv4,tcp
tcpServerSocket = socket(AF_INET,SOCK_STREAM)
tcpServerSocket.bind(addr)
# 最大连接数
tcpServerSocket.listen(2)
print("Server Port:9876")
print('正在等待客户端的连接')

while True:
    tcpClientSocket, addr = tcpServerSocket.accept()
    print("客户端已经连接", "addr = ", addr)
    # 每次最多读取1024个字节的数据
    data = tcpClientSocket.recv(bufferSize)
    print(data.decode("utf-8"))
    tcpClientSocket.send("hello,I love you \n".encode(encoding="utf-8"))
    tcpClientSocket.close()

tcpServerSocket.close()