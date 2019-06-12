# 将类实例转换为JSON字符串

# dumps(): 将字典(or列表)转换为JSON字符串
# default关键字参数指定一个回调函数,该回调函数会接收一个类实例
# 回调函数需要返回一个字典,最后dumps函数会将这个字典转换为JSON
# 字符串
# 类实例 -> default (返回dict)-> dumps (返回JSON字符串)
# object -> dict -> Json

import json
class Product(object):
    def __init__(self,name,price,count):
        self.name = name
        self.price = price
        self.count =count

def product2Dict(obj):
    return {
        'name':obj.name,
        'price':obj.price,
        'count':obj.count
    }

product1 = Product('特斯拉',1000000,200)
jsonStr = json.dumps(product1,default=product2Dict,ensure_ascii=False)
print(jsonStr)