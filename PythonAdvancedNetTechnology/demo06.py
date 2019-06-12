# 超时

# urllib3: 连接超时，读超时(从服务端读取数据)

# timeout: 连接超时和读超时设置为4.0秒
# http.request('GET',url,timeout=4.0)
# connect: 连接超时；read: 读超时
# connect:2.0(s); read:5.0(s)
# http.request('GET',url,timeout=Timeout(connect=2.0,read=5.0))

from urllib3 import *
# HTTPResponse.info()
disable_warnings()
# 设置全局超时timeout=Timeout(connect=2.0,read=6.0)
http = PoolManager(timeout=Timeout(connect=2.0,read=6.0))

# 不存在的url
url1 = 'http://baidu.com122.com'
# 存在的url，但是会模拟3s给出响应，因为'http://httpbin.org/delay/3'最尾端的数字是3
# 目的是模拟读超时
url2 = 'http://httpbin.org/delay/3'

try:
    http.request('GET',url1)
except Exception as e:
    print(e)

response = http.request('GET',url2,timeout=Timeout(connect=2.0,read=4.0))
print(type(response)) # <class 'urllib3.response.HTTPResponse'>
print(response.info) # 是一个方法名，<bound method HTTPResponse.info of <urllib3.response.HTTPResponse object at 0x000002824B79E978>>
# 获得响应头信息
# print(response.info())

response_1 = http.request('GET',url2,timeout=Timeout(connect=2.0,read=2.0))
print(response_1.info)
