# 非关系型数据库: MongoDB
# NoSQL, 关系型数据库：SQLite(本地)和MySQL(Web)
# 关系型数据库将数据保存到二位表中
# NoSQL类型: 对象数据库、键值数据库(key-value),文档数据库
# 图形数据库、表格数据库
# MongoDB: 文档数据库

# 博文(blogs)
# t_blogs、t_comments
# 如果使用MongoDB，可以将博文和博文下的评论都保存到一个文档中

# 安装第三方模块: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pymongo

from pymongo import *
# 连接MongoDB数据库
Client = MongoClient()

# 打开或创建名为hello的collection,collection相当于关系型数据库中的数据库
db = Client.hello # 或者db = Client['hello']

person1 = {"name":"Bill","age":25,"address":'地球',"salary":145.69}
person2 = {'name':"Mary","age":22,"address":"火星","salary":4565798.5897}

# 创建或打开一个名为persons的文档，persons相当于关系型数据库中的表
persons = db.persons

# $gt:greater than $lt:less than
persons.delete_many({'age':{'$gt':0}})
personId1 = persons.insert_one(person1).inserted_id
personId2 = persons.insert_one(person2).inserted_id
print(personId2)

'''
personList = [person1,person2]
result = person.insert_many(personList)
print(result.inserted_ids)
'''
print(persons.find_one())
print(persons.find_one()['name'])

# 搜索所有数据
for person in persons.find():
    print(person)

print('-' * 40)

# 更新数据
persons.update_one({'age':{'$lt':23}},{'$set':{'name':'超人'}})

# 搜索所有数据
for person in persons.find():
    print(person)

print('-' * 40)

# 删除
persons.delete_one({'age':{'$gt':23}})
# 搜索所有数据
for person in persons.find({'age':{'$lt':30}}):
    print(person)

# 获得persons里面文档总数：
print('总数', '=', persons.count())