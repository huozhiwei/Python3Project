# 计算日期和时间的差

# datatime.timedelta 类

import datetime

# 定义第一个日期
d1 = datetime.datetime(2017,4,12)

# 定义第二个日期
d2 = datetime.datetime(2018,12,25)

# 相差的天数622天
print((d2-d1).days)

# year,month,day,hour,min,sec
d3 = datetime.datetime(2017,4,12,10,10,10)

d4 = datetime.datetime(2018,12,25,10,10,40)

print(d4-d3)
print(type(d4-d3))
print((d4-d3).seconds)

# 获取当前日期
d5 = datetime.datetime.now()
# 向后推10h(小时)
d6 = d5 + datetime.timedelta(hours=10)
print(d6)
# 向前移动10h(小时)
d7 = d5 + datetime.timedelta(hours=-10)
print(d7)