"""
练习题1：
    编写一个Python程序，将/files/products.xml文件的内容保存到MongoDB中，
并且可以查找到每一个product。
"""
import xmltodict
from pymongo import *

client = MongoClient()
# 创建MongoDB数据库
db = client.data
# 创建（不存在该文档）或打开（存在该文档）一个数据库文档
products = db.products
# gt:greater than
products.delete_many({'price': {'$gt': 0}})
with open('./files/products.xml','rt',encoding='utf-8') as f:
    xml = f.read()
# xml字符串 -> dict
dic = xmltodict.parse(xml)
# print(dic)
productList = dic['root']['products']['product']
'''
[
 OrderedDict([('@uuid', '1234'), ('id', '10000'), ('name', 'iPhone XSMAX'), ('price', '9999')]), 
 OrderedDict([('@uuid', '4321'), ('id', '20000'), ('name', '特斯拉'), ('price', '1000000')]), 
 OrderedDict([('@uuid', '5678'), ('id', '30000'), ('name', 'MacBook Pro2018'), ('price', '40000')])
]
'''
# print(productList)

for product in productList:
    product['price'] = int(product['price'])
    productId = products.insert_one(product).inserted_id
    print(productId)

for product in products.find({'price':{'$gt':10000}}):
    print(product)
