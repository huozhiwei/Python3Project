# 将JSON字符串转换为类实例(对象)

'''
loads()
"
hook:
n.钩;钓钩;挂钩;鱼钩;钩拳;曲线球
v.(使)钩住，挂住;(尤指用腿、胳膊、手指等)钩住，箍住;钓(鱼)
"
loads函数的object_hook关键字参数指定一个类或一个回调函数
1. 指定类: loads函数会自动创建指定类的实例,并将由json字符串
转换成的字典通过类的构造方法传入类实例,也就是说指定的类必须有一个
可以接收字典的__init__()构造方法.

2. 指定回调函数: loads函数会调用回调函数返回类的实例,并将由json
字符串转换成的字典传入回调函数,也就是说回调函数必须有一个参数可以接收
字典

JSON字符串 -> object_hook指定类或者调用类的函数 -> loads(jsonStr,object_hook=A()) (返回类实例对象)
'''

import json

class Product(object):
    def __init__(self,dic):
        self.__dict__ = dic
        # print(self.__dict__,'1')

with open('./files/products_1.json','r',encoding='utf-8') as f:
    jsonStr = f.read()
    my1 = json.loads(jsonStr,object_hook=Product)
    # print(type(my1))
    print('status','=',my1.status)
    print('message', '=', my1.message)
    print('data','=',my1.data.__dict__,'__dict__')
    print('data.title','=',my1.data.title)
    print('data.title.id','=',my1.data.title.id)
    print('data.title.name', '=', my1.data.title.name)
    print('data.products','=',my1.data.products)
    print('data.products[0].name','=',my1.data.products[0].name)
    print('data.products[0].price','=',my1.data.products[0].price)
    print('data.products[0].count','=',my1.data.products[0].count)
    print('data.products[1].name','=',my1.data.products[1].name)
    print('data.products[1].price','=',my1.data.products[1].price)
    print('data.products[1].count','=',my1.data.products[1].count)
    print('-' * 40)
    def json2Product(d):
        return Product(d)
    my2 = json.loads(jsonStr,object_hook=json2Product)
    # json -> dict -> Product对象
    # print(type(my2))
    print('status','=',my2.status)
    print('message', '=', my2.message)
    print('data','=',my2.data.__dict__,'__dict__')
    print('data.title','=',my2.data.title)
    print('data.title.id','=',my2.data.title.id)
    print('data.title.name', '=', my2.data.title.name)
    print('data.products','=',my2.data.products)
    print('data.products[0].name','=',my2.data.products[0].name)
    print('data.products[0].price','=',my2.data.products[0].price)
    print('data.products[0].count','=',my2.data.products[0].count)
    print('data.products[1].name','=',my2.data.products[1].name)
    print('data.products[1].price','=',my2.data.products[1].price)
    print('data.products[1].count','=',my2.data.products[1].count)

