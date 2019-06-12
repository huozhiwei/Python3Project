# 数据存储
'''
1. XML
2. JSON
3. SQLite
4. MySQL
5. ORM:（SQLAlxhemy、SQLObject）模型关系映射
6. 非关系型数据库(NoSQL) [MongoDB]

'''

# 读取与检索XML文件

# parse函数
from xml.etree.ElementTree import parse


doc = parse('./files/products.xml')
for item in doc.iterfind('products/product'):
    # 读取id节点的值,str类型
    id = item.findtext('id')
    # print(type(id))
    # 读取name节点的值，str类型
    name = item.findtext('name')
    # 读取price节点的值，str类型
    price = item.findtext('price')

    # 读取当前主节点(products)的属性值，str类型
    uuid = item.get('uuid')
    # print(type(uuid))
    print('uuid','=',uuid)
    print('id','=',id)
    print('name','=',name)
    print('price','=',price)
    print('-' * 40)

