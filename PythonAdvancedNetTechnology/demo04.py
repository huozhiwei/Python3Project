# HTTP响应头
from urllib3 import *

disable_warnings()
http = PoolManager()
url = 'http://www.baidu.com'
response = http.request('GET',url)
# 获得响应头信息
print(response.info()) # 字典类型：HTTPHeaderDict()

print(response.info()['content-Length']) # bytes

