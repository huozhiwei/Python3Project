# SQLObject

# dropTable: 删除表
# createTable: 创建表

# 安装第三方模块: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple sqlobject

# 不需要调用commit方法就可以修改数据库
# SQLObject的每一个方法调用都会自动commit()来更新数据库表
from sqlobject import *
from sqlobject.sresults import SelectResults
# builder()
from sqlobject.mysql import builder

mysql = 'mysql://root:12345678@localhost:3306/test?charset=utf8'
# 设置连接数据库驱动
sqlhub.processConnection = connectionForURI(mysql,driver='pymysql')

class Person(SQLObject):
    class sqlmeta:
        table = 'persons1'
    name = StringCol(length=30)
    age = IntCol()
    address = StringCol(length=100)
    salary = FloatCol()

try:
    # dropTable()方法调用后直接更新数据库表
    Person.dropTable()
except Exception as e:
    print(e)

# createTable()方法调用后直接更新数据库表
Person.createTable()
print('成功创建了persons1表。')

# 创建person1后就更新数据库表
person1 = Person(name='Bill',age=55,address='地球',salary=1234.256)
# 创建person2后就更新数据库表
person2 = Person(name='Mike',age=23,address='火星',salary=456789.26)
# 创建person3后就更新数据库表
person3 = Person(name='John',age=45,address='月球',salary=77879.7789744)

# 更新数据库表
person2.name = '钟志炜'
# 更新数据库表
person2.address = '南昌'

# 更新数据库表
# persons = Person.selectBy(name='Bill')
persons = Person.select(Person.q.age > 30)
print(type(persons)) #<class 'sqlobject.sresults.SelectResults'>
# 因为实现了__getitem__魔法方法，所以可以这么使用索引
print(persons[0])
print(persons[1])
# 列出查询记录的数量
print(persons.count())

print(persons[0].id)
print(persons[0].name)
print(persons[0].age)
print(persons[0].address)
print(persons[0].salary)

# object -> dict -> json
def person2Dict(obj):
    return {
        'id':obj.id,
        'name':obj.name,
        'address':obj.address,
        'salary':obj.salary
    }
import json
print(persons[0].__dict__)
# personStr = json.dumps(persons[0],default=lambda obj:obj.__dict__,ensure_ascii=False)
personStr = json.dumps(persons[0],default=person2Dict,ensure_ascii=False)
print(personStr)

# 删除一条记录
# 更新数据库表
# persons[0].destroySelf()


