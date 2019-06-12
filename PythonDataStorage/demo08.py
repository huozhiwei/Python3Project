# 将JSON字符串转换成XML字符串

# json -> dict -> xml

import json
import dicttoxml
from xml.dom.minidom import parseString
import os
# from xml.dom.minidom import Document

with open('files/products_2.json','r',encoding='utf8') as f:
    jsonstr = f.read()
    # json -> dict
    dic = json.loads(jsonstr)
    print(dic)
    # dict -> xml
    xmlStr = dicttoxml.dicttoxml(dic).decode('utf-8')
    print(type(xmlStr))
    print(xmlStr)
    # 将xml字符串转换成可读的模式

    # 解析xml字符串
    dom = parseString(xmlStr)
    # print(type(dom)) # <class 'xml.dom.minidom.Document'>
    prettyxml = dom.toprettyxml(indent='\t')
    print(prettyxml)
    with open('files/products_2.xml','w',encoding='utf8') as file:
        file.write(prettyxml)