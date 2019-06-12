# 用Python操作SOLite数据库
# (SQLite3)

# SQLite数据库与MySQL数据库都是基于 Python DB API 2.0 标准的，操作都是差不多的
# 查询python网址看Python提供的数据库API有哪些:https://www.python.org/dev/peps/pep-0249/

'''
1. connect函数: 连接数据库。返回Connection对象
2. cursor方法(Connection类下的方法): 获取操作数据库的Cursor对象，是Connection类中的方法
3. execute方法: 用于执行SQL语句，是Cursor类中的方法
4. commit方法: 在修改数据库后，需要调用该方法提交对数据库的修改(提交事务)，是Cursor类中的方法
5. rollback方法: 如果修改数据库失败，可以调用该方法进行数据库回滚
'''

# 使用工具: DB Browser for SQLite

import sqlite3
import os

sqlite3.Cursor

dbPath = './files/data.sqlite3'
if not os.path.exists(dbPath):
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE persons
        ( id INT PRIMARY KEY NOT NULL,
          name TEXT NOT NULL,
          age INT NOT NULL,
          address CHAR(50),
          salary REAL );
    ''')
    conn.commit()
    conn.close()
    print('数据库创建成功。')

conn  = sqlite3.connect(dbPath) # <class 'sqlite3.Connection'>
# print(type(conn),'1')
c = conn.cursor()
# 删除表中所有数据
c.execute('delete from persons')
c.execute("insert into persons(id,name,age,address,salary)\
          values(1,'Bill',32,'California',20000.12)")
c.execute("insert into persons(id,name,age,address,salary)\
          values(2,'Mary',26,'Textas',122451.56)")
c.execute("insert into persons(id,name,age,address,salary)\
          values(3,'John',36,'Norway',556.56)")
c.execute("insert into persons(id,name,age,address,salary)\
          values(4,'Joe',16,'Rich-Mona',66978.56)")
conn.commit()
print('数据插入成功。')

personsResult = c.execute("select name,address,age,salary from persons order by age")
# print(type(personsResult)) # <class 'sqlite3.Cursor'>
result = []
# print(personsResult)    # <sqlite3.Cursor object at 0x0000023B6A4E4A40>
for person in personsResult:
    # print(person)
    # print(type(person)) # <class 'tuple'>
    value = {}
    value['name'] = person[0]
    value['address'] = person[1]
    value['age'] = person[2]
    value['salary'] = person[3]
    result.append(value)
conn.close()
print(result)

# 列表转成json字符串
import json
resultStr = json.dumps(result)
print(resultStr)
print('type(resultStr):',type(resultStr))