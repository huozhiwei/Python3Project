# 类实例列表与Json字符串互相转换

import json

class Product(object):
    def __init__(self,d):
        self.__dict__ = d
        # print(Product.__dict__)
        # print(self.__dict__)

with open('./files/products_2.json','r',encoding='utf-8') as f:
    jsonStr = f.read()
    # json字符串转成Product对象 列表
    products = json.loads(jsonStr,object_hook=Product)
    # print(type(products)) # list列表
    i = 1
    for item in products:
        print('item' + str(i))
        print('products',':')
        for product in item.data.products:
            print('product name','=',product.name)
            print('product price','=',product.price)
            print('product count','=',product.count)
        i += 1

    # Product对象列表转成json字符串
    # def productList2Dict(product):
    #     return {
    #         'status':product.status,
    #         'message':product.message,
    #         'data':product.data
    #     }
    # jsonStr = json.dumps(products,default=productList2Dict,ensure_ascii=False)
    '''
    lambda obj: obj.__dict__
    会将任意的对象，转换成字典的方式

    sort_keys = True
    会按照字典中的键来按照ASCII方式来排序

    indent = 4
    会按照键值对以间隔4来直观的显示
    '''
    jsonStr = json.dumps(products,default=lambda obj:obj.__dict__,ensure_ascii=False)
    print(jsonStr)


class Person(object):
    def __init__(self,dic):
        self.__dict__ = dic

with open('files/persons_1.json','r',encoding='utf-8') as f:
    jsonStr = f.read()
    # json字符串转成Product对象 列表
    persons = json.loads(jsonStr,object_hook=Person)

    # Product对象列表转成json字符串
    def personList2Dict_1(person):
        return {
            'name':person.name,
            'age':person.age,
            'salary':person.salary
        }

    jsonStr = json.dumps(persons,default=personList2Dict_1,ensure_ascii=False)
    print(jsonStr)

