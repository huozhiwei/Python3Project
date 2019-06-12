"""
练习题2：
    编写一个Python程序，通过循环向SQLite数据库的persons表中录入数据。从控制台输入'exit:'
后退出循环，然后输出persons表中的所有数据。

"""
import sqlite3
from sqlite3 import Cursor
import os

dbPath = './files/persons.sqlite3'
# 如果不存在该Sqlite数据库文件
if not os.path.exists(dbPath):
    # 创建Sqlite数据库
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    c.execute('''create table persons
        (id int primary key not null,
         name text not null,
         age int not null)
    ''')
    conn.commit()
    conn.close()

conn = sqlite3.connect(dbPath)
c = conn.cursor()
c.execute("delete from persons")
while True:
    id = input('id: ')
    if id == 'exit:':
        break
    id = int(id)
    name = input('name: ')
    if name == 'exit:':
        break
    age = input('age: ')
    if age == 'exit:':
        break
    age = int(age)
    c.execute("insert into persons(id,name,age)\
               values({},'{}',{})".format(id, name, age))
conn.commit()
persons = c.execute("select id,name,age from persons order by age ")
print(type(persons)) # <class 'sqlite3.Cursor'>
result = []
for person in persons:
    value = {}
    value['id'] = person[0]
    value['name'] = person[1]
    value['age'] = person[2]
    result.append(value)
conn.close()
print(result)