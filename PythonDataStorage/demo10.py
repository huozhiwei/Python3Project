# 用Python操作MySQL数据库,web版本的sql
# 安装第三方模块: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql

# SQLite数据库与MySQL数据库都是基于 Python DB API 2.0 标准的，操作都是差不多的
# 查询python网址看Python提供的数据库API有哪些:https://www.python.org/dev/peps/pep-0249/

'''
1. connect函数: 连接数据库。返回Connection对象
2. cursor方法(Connection类下的方法): 获取操作数据库的Cursor对象，是Connection类中的方法
3. execute方法: 用于执行SQL语句，是Cursor类中的方法
4. commit方法: 在修改数据库后，需要调用该方法提交对数据库的修改(提交事务)，是Cursor类中的方法
5. rollback方法: 如果修改数据库失败，可以调用该方法进行数据库回滚
'''
# 使用工具phpmyadmin
# 网址: 'http://localhost:8080/phpmyadmin/'
# 12345678，短语密码：zzw
# 启动Apache:
# net start Apache2.4
# 停止Apache:
# net stop Apache2.4

# apache,php,mysql

# mysql和NavicatForMySQL安装网址和安装软件
# https://www.cnblogs.com/zhangqie/p/8003996.html

# mysql:username:zzw password:12345678 ip:localhost port:3306
# Apache: localhost:80

'''
phpmyadmin打开步骤:
1. 启动Apache: 管理员运行cmd:输入:net start Apache2.4 (启动Apache服务) net stop Apache2.4 (停止Apache服务)
2. 启动MySql: 任务管理器 -> 服务(列表里面罩MySQL80,右键启动)
3. 浏览器里面输入网址: www.myphpadmin.com 打开phpmyadmin（因为在C:\Windows\System32\drivers\etc\hosts文件中已经配置了DNS映射，
   故直接输入该网址即可）
4. Navicat for MySQL也可以打开相关MySQL数据库
数据库:username:root password:12345678
'''
import pymysql
import json

def connectDB():
    # pymysql.connect(ip,username,password,databasename)
    db = pymysql.connect('127.0.0.1','root','12345678','test',charset='utf8') # 只能写'utf8',不能写'utf-8',否则会报错
    return db # Connection对象

db = connectDB()
# 创建persons表
def createTable(db):
    cursor = db.cursor()
    sql ='''
        CREATE TABLE persons
        ( id INT PRIMARY KEY NOT NULL,
          name TEXT NOT NULL,
          age INT NOT NULL,
          address CHAR(50),
          salary REAL );'''
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
        return False

# 向persons表插入4条记录
def insertRecords(db):
    cursor = db.cursor()
    try:
        cursor.execute('delete from persons')
        cursor.execute("insert into persons(id,name,age,address,salary)\
                  values(1,'Bill',32,'California',20000.12)")
        cursor.execute("insert into persons(id,name,age,address,salary)\
                  values(2,'Mary',26,'Textas',122451.56)")
        cursor.execute("insert into persons(id,name,age,address,salary)\
                  values(3,'John',36,'Norway',556.56)")
        cursor.execute("insert into persons(id,name,age,address,salary)\
                  values(4,'Joe',16,'Rich-Mona',66978.56)")
        db.commit()
        return True
    except:
        db.rollback()
        return False

# persons的查询函数
def selectRecord(db):
    cursor = db.cursor()
    sql = 'select name,age,salary from persons order by age desc' # 按照age降序排列
    cursor.execute(sql)
    # 获得所有查询记录
    results = cursor.fetchall()
    # print(results,'results') # (('John', 36, 556.56), ('Bill', 32, 20000.12), ('Mary', 26, 122451.56), ('Joe', 16, 66978.56))
    fields = ['name','age','salary']
    records = []
    for row in results:
        # print(row,'row') # ('John', 36, 556.56)
        print(list(zip(fields,row)),"zip(fields,row)")
        records.append(dict(zip(fields,row)))
    return json.dumps(records)

if createTable(db):
    print('成功创建persons表。')
else:
    print('persons表已经存在。')

if insertRecords(db):
    print('成功插入记录')
else:
    print('插入记录失败')

print(selectRecord(db))
db.close()


