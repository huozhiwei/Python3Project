# 用Socket实现HTTP服务器

# HTTP

"""
HTTP请求头
GET POST

GET /html/rfc2616 HTTP/1.1
Host: www.w3.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://www.baidu.com/link?url=PZp7iCBLEnC4IQq06ANaRtCuuPowWBzJaodbvccmnshYK0--pPP9b3T3CnQhgoE7cnMuAVU3T3gbW9AS6rmXWa&wd=&eqid=f6e311020049cfa1000000035cf635df
Connection: keep-alive
Upgrade-Insecure-Requests: 1
If-Modified-Since: Wed, 01 Sep 2004 13:24:52 GMT
If-None-Match: "40d7-3e3073913b100-gzip"
Cache-Control: max-age=0


HTTP响应头

HTTP/2.0 200 OK
date: Tue, 04 Jun 2019 09:12:15 GMT
last-modified: Wed, 01 Sep 2004 13:24:52 GMT
etag: "40d7-3e3073913b100-gzip"
accept-ranges: bytes
vary: Accept-Encoding
content-encoding: gzip
cache-control: max-age=21600
expires: Tue, 04 Jun 2019 15:12:15 GMT
content-length: 5535
content-type: text/html; charset=iso-8859-1
strict-transport-security: max-age=15552000; includeSubdomains; preload
content-security-policy: upgrade-insecure-requests
X-Firefox-Spdy: h2
"""

from socket import *
import os
import os.path

# 从文件中读取要返回的HTTP响应头文本，并设置响应头中“Content-length”的长度内容为length（%d）
def responseHeader(file, length):
    f = open(file,"r")
    headersText = f.read()
    headersText = headersText % length
    return headersText

# print(responseHeader("./response_headers.txt",10))

# 根据HTTP请求头的路径得到服务端的本地路径
def filePath(get):
    if get == "/":
        return "static" + os.sep + "index.html"
    else:
        paths = get.split('/')
        s = 'static'
        for path in paths:
            if path.strip() != "":
                s = s + os.sep + path
        return s

host =""
bufferSize = 1024 # 字节
port = 8765
addr = (host,port)
# ipv4,tcp
tcpServerSocket = socket(AF_INET,SOCK_STREAM)
tcpServerSocket.bind(addr)
tcpServerSocket.listen(5)
while True:
    print("正在等待客户端连接。。。")
    tcpClientSocket,addr = tcpServerSocket.accept()
    print("客户端已经连接","addr","=",addr)
    data = tcpClientSocket.recv(bufferSize)
    data = data.decode("utf-8")
    try:
        # 获取HTTP请求头的第一行
        firstLine = data.split("\n")[0]
        # 获取请求路径
        path = firstLine.split(" ")[1]
        # 将Web路径转换为本地路径
        pathServerLocal = filePath(path)
        if os.path.exists(pathServerLocal):
            print(type(os.path),"os.path")
            file = open(pathServerLocal,"rb")
            content = file.read()
            file.close()
        else:
            content = "<h1>File Not Found</h1>".encode(encoding='utf-8')
        print(len(content), "bytes")
        rh = responseHeader("response_headers.txt",len(content)) + "\r\n"
        tcpClientSocket.send(rh.encode(encoding="utf-8") + content)
    except Exception as e:
        print(e)

    tcpClientSocket.close()
tcpServerSocket.close()