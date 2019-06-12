# 发送HTTP POST请求

# flask
# 安装第三方模块: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
# 服务端程序为server.py文件

from urllib3 import *

disable_warnings()

http = PoolManager()

url = "http://localhost:5000/register"
# 通过url发送POST请求
response = http.request('POST',url,fields={'name': 'zzw','age': 18})
data = response.data.decode('utf-8')
print(data)