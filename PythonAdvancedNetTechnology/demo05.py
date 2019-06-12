# 上传文件
# request('POST', url, fields={'file':(fileName,fileData)})
# flask 模拟服务器

from urllib3 import *
disable_warnings()
http = PoolManager()
url = 'http://localhost:5000/'

while True:
    fileName = input('请输入要上传的文件名：')
    if not fileName:
        break
    with open(fileName,'rb') as f:
        fileData = f.read()
    response = http.request("POST",url,fields={'file1':(fileName,fileData)})
    print(response.data.decode('utf-8'))