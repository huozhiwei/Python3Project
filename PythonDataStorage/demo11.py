# ORM(SQLAlchemy)
# ORM(Object Relational Mapping)
# SQL
# ORM: 抽象SQL，或者说将SQL语句直接映射成Python对象
# SQLAlchemy,SQLObject
# 安装第三方模块: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple SQLAlchemy

'''
phpmyadmin打开步骤:
1. 启动Apache: 管理员运行cmd:输入:net start Apache2.4 (启动Apache服务) net stop Apache2.4 (停止Apache服务)
2. 启动MySql: 任务管理器 -> 服务(列表里面罩MySQL80,右键启动)
3. 浏览器里面输入网址: www.myphpadmin.com 打开phpmyadmin（因为在C:\Windows\System32\drivers\etc\hosts文件中已经配置了DNS映射，
   故直接输入该网址即可）
4. Navicat for MySQL也可以打开相关MySQL数据库
数据库:username:root password:12345678
'''

from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,Float,exc,orm
from sqlalchemy.ext.declarative import declarative_base
import pymysql.cursors
from sqlalchemy.ext.declarative.api import DeclarativeMeta
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.query import Query

# test:databasename
mysql = 'mysql+pymysql://root:12345678@localhost:3306/test?charset=utf8'
tableName = 'persons1'
engine = create_engine(mysql, encoding='utf-8')
# 连接MySQL数据库
engine.connect()
metadata = MetaData(engine)
persons = Table(tableName, metadata,
                Column('id',Integer,primary_key=True),
                Column('name',String(30)),
                Column('age',Integer),
                Column('address',String(100)),
                Column('salary',Float))
metadata.create_all(engine)

# 声明一个Base类，其实Base是一个类
Base = declarative_base()
# print(type(Base)) # <class 'sqlalchemy.ext.declarative.api.DeclarativeMeta'>
class Person(Base):
    __tablename__ = tableName # 必须写成__tablename__
    id = Column('id',Integer,primary_key=True)
    # print(type(id)) # <class 'sqlalchemy.sql.schema.Column'>
    name = Column('name',String(30))
    age = Column('age',Integer)
    address = Column(String(100))
    salary = Column(Float)

# Session为一个<class 'sqlalchemy.orm.session.sessionmaker'> 类对象
Session = orm.sessionmaker(bind=engine)
print(type(Session)) # <class 'sqlalchemy.orm.session.sessionmaker'>

# 一个 <class 'sqlalchemy.orm.session.Session'> object(对象)，调用sqlalchemy.orm.session.sessionmaker里面的__call__()方法
# 进行类中创建新子类subclass Session类(<class 'sqlalchemy.orm.session.Session'>)
# session = Session.__call__()
session = Session()
print(type(session)) # <class 'sqlalchemy.orm.session.Session'>

# 先删除person1表中的所有记录
session.query(Person).delete()
session.commit()

person1 = Person(id=10,name='Bill',age=30,address='地球',salary=1234)
# print(type(person1.id),person1.name,person1.age,person1.address,person1.salary) # person1.id<class 'int'>
# print(Person.id,Person.name,Person.age,Person.address,Person.salary) # Person.id Person.name Person.age Person.address Person.salary
person2 = Person(id=20,name='Mike',age=34,address='火星',salary=5432)
# print(person2.id,person2.name,person2.age,person2.address,person2.salary)
# print(Person.id,Person.name,Person.age,Person.address,Person.salary)
person3 = Person(id=30,name='John',age=24,address='月球',salary=15666.32)
# print(person3.id,person3.name,person3.age,person3.address,person3.salary)
# print(Person.id,Person.name,Person.age,Person.address,Person.salary)

session.add(person1)
session.add(person2)
session.add(person3)

session.commit()
print('成功插入记录。')

session.query(Person).filter(Person.name == 'Mike').update({'address':'千星之城'})
query = session.query(Person).filter(Person.name == 'John')
print(query) # SQL语句
print(type(query)) # <class 'sqlalchemy.orm.query.Query'>
session.commit()
print('更新完成。')
# scalar:adj.纯量的;标量的;无向量的 n.数量，标量
# scalar()将查询的SQL语句转换成单一的对象，查询SQL语句结果必须只能是一条结果，否则抛出异常
person = query.scalar()
print(type(person)) # <class '__main__.Person'>
print(person.name) # John
person.age = 55
person.salary = 4546798.0986
session.commit()
print('成功更新记录。')

# 使用组合条件查询person1表中的记录
persons_1 = session.query(Person).filter((Person.age >= 10) & (Person.salary >= 2000))
print(persons_1) # SQL语句
print(type(persons_1)) # <class 'sqlalchemy.orm.query.Query'>
print(list(persons_1))
print(persons_1[0])
for person in persons_1:
    print('name','=',person.name,end=' ')
    print('age','=',person.age,end=' ')

print()
# Query.first()
print(persons_1.first().name)
# Query.offset

# scalar:adj.纯量的;标量的;无向量的 n.数量，标量
# scalar()将查询的SQL语句转换成单一的对象，查询SQL语句结果必须只能是一条结果，否则抛出异常
# 查询第二条记录
print(persons_1.offset(1).scalar().name)

# 删除一条记录
session.delete(person2)
session.commit()
session.close()







