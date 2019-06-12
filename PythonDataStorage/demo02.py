# 将字典转换为XML字符串
# 安装第三方模块: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple dicttoxml
# dict -> xml字符串,格式化xml字符串，write person.xml

import dicttoxml
# parseString()函数
from xml.dom.minidom import parseString
import os
# from xml.dom.minidom import Document

# 定义一个包含字典的列表
d = [20,'names',{'name':'Bill','age':30,'salary':2000},
                {'name': '钟志炜','age':24,'salary':200004},
                {'name': 'John','age':20,'salary':1234}]

# 将列表中的字典转换为XML格式(bytes类型)
bxml = dicttoxml.dicttoxml(d,custom_root='persons')
# print(bxml)
xml = bxml.decode('utf8')
# print(xml)
# 解析xml字符串
dom = parseString(xml)
# print(type(dom)) # <class 'xml.dom.minidom.Document'>

# indent:缩进
# v.将(印刷或书写的行)缩进，缩格，缩排
# n.订单;订购
prettyxml = dom.toprettyxml(indent='\t') # str类型
# print(type(prettyxml))
# print(prettyxml)

os.makedirs('./files',exist_ok=True)
f = open('./files/persons.xml','w',encoding='utf-8')
f.write(prettyxml)
f.close()


