'''
练习题2：
    编写一个Python程序，从控制台输入两个日期，格式：2011-1-1，
然后计算这两日期之间相差多少天，并输出计算结果。如果日期格式错误，
会抛出异常，并输出这个异常。
'''

# 由日期格式转化为字符串格式的函数为: datetime.datetime.strftime()
# 由字符串格式转化为日期格式的函数为: datetime.datetime.strptime()

import datetime
while True:
    try:
        d1 = input('请输入第1个日期：')
        d1 = datetime.datetime.strptime(d1,'%Y-%m-%d')
        d2 = input('请输入第2个日期：')
        d2 = datetime.datetime.strptime(d2,"%Y-%m-%d")
        # print(type(d2))
        d = d2-d1
        print('两个日期之间相距%d天'%d.days)
    except Exception as e:
        print(e)