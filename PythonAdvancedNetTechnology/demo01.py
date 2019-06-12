# 网络高级技术
# 1. urllib3
# 2. Twisted
# 3. FTP
# 4. Email

# 发送HTTP GET请求
# 安装第三方模块: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple urllib3

import urllib3
from urllib3.response import HTTPResponse
from urllib.parse import urlencode

# 关闭urllib3中的警告
urllib3.disable_warnings()
# poolManager类:池化管理
http = urllib3.PoolManager()
url = 'http://www.baidu.com/s?' + urlencode({'wd': '极客起源'})
# print(url) # http://www.baidu.com/s?wd=%E6%9E%81%E5%AE%A2%E8%B5%B7%E6%BA%90

# 普通url请求为GET请求,表单请求为POST请求
response = http.request('GET',url)
# print(type(response)) # <class 'urllib3.response.HTTPResponse'>
# print(type(response.data)) # <class 'bytes'>
print(response.data.decode('utf-8'))

url_1 = 'http://www.baidu.com/s'

response_1 = http.request('GET',url,fields = {'wd': '极客起源'})
print(response_1.data.decode('UTF-8'))
