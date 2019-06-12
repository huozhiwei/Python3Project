# 读行与写行

import os

f = open('./files/urls.txt','r+')
url = ''
while True:
    url = f.readline()
    url = url.rstrip()
    if url == '':
        break
    else:
        print(url)

print('-'*40)
f.seek(0)

print(f.readlines())

# os.linesep: 系统行分隔符，Windows下为'\r\n'
f.write('http://baidu.com'  + os.linesep)
f.close()

f = open('./files/urls.txt','a+')
urlList = ['https://google.cn' + os.linesep,'http://jd.com' + os.linesep]
f.writelines(urlList)
f.seek(0)
print(f.readlines())
f.close()