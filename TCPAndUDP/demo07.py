# UDP时间戳服务器
"""
UDP和TCP的区别

TCP: 面向连接的协议

UDP: 面向无连接的协议

"""

from socket import *
import time

host = ""
port = 9876
bufferSize = 1024
addr = (host,port)
# ipv4, UDP
udpServerSocket = socket(AF_INET,SOCK_DGRAM)
udpServerSocket.bind(addr)

while True:
    print("正在等待消息...")
    data,addr = udpServerSocket.recvfrom(bufferSize)
    udpServerSocket.sendto(time.ctime().encode(encoding='utf-8') + b' ' + data, addr)
    print("客户端地址：",addr)

udpServerSocket.close()

