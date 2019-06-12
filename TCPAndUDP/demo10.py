"""
练习题

使用UDP Socket编写一个可以计算Python表达式的服务端应用
然后再编写一个用于测试这个服务端应用的客户端程序。
在客户端程序中输入Python表达式,然后将表达式字符串传到服务端
服务端执行后，再将结果返回给客户端程序。

"""

# 服务端
from socket import *

host = ''
port = 9999
bufferSize = 1024 # bytes
addr = (host,port)
# ipv4, UDP
udpServerSocket = socket(AF_INET,SOCK_DGRAM)
udpServerSocket.bind(addr)
while True:
    print('正在等待消息...')
    try:
        data,addr = udpServerSocket.recvfrom(bufferSize)
        # print(data)
        # print(addr)
        pythonCode = data.decode('utf-8')
        print(pythonCode)
        # eval()可以计算表达式的内置函数，比如：result = eval(3+4),结果result = 7
        result = eval(pythonCode)
        udpServerSocket.sendto(str(result).encode(encoding='utf-8'),addr)
        print("客户端地址：",addr)
    except Exception as e:
        print(e)
udpServerSocket.close()

