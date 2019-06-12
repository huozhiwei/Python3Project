# TCP与UDP编程
# TCP: 传输控制协议，面向连接的，保证数据的可达性
# UDP: 数据报协议，无连接的，不能保证数据一定可以到达另一端

# Socket （套接字）
# socketServer模块
# 建立TCP服务端

"""
1. 创建Socket对象
2. 绑定端口号
3. 监听端口号
4. 等待客户端Socket的连接
5. 读取从客户端发过来的数据
6. 向客户端发送数据
7. 关闭客户端Socket连接
8. 关闭服务端的Socket连接

"""

# 以下代码为服务端代码
# 9876
from socket import *

host = "" # ip
bufferSize = 1024 # 字节
port = 9876
addr = (host, port)
# 1. 创建Socket对象
# AF_INET:IPV4,AF_INET:IPV6,SOCK_STREAM：TCP
tcpServerSocket = socket(AF_INET,SOCK_STREAM)

# 2. 绑定端口号
tcpServerSocket.bind(addr)

# 3. 监听端口号
tcpServerSocket.listen()

print("Server Port:9876")
print("正在等待客户端连接")

# 4. 等待客户端Socket的连接
tcpClientSocket,addr = tcpServerSocket.accept()
print("客户端已经连接","addr","=",addr)

# 5. 读取从客户端发过来的数据
data = tcpClientSocket.recv(bufferSize) # 1024 byte
print(data.decode("utf-8"))

# 6. 向客户端发送数据
tcpClientSocket.send("hello,I love you.\n".encode(encoding="utf-8"))

# 7. 关闭客户端Socket连接
tcpClientSocket.close()

# 8. 关闭服务端的Socket连接
tcpServerSocket.close()