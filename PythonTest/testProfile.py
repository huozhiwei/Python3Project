'''
ncalls:调用次数
tottime:函数的总执行时间(不包括调用子函数的时间)
第一个percall: tottime除以ncalls的值
cumtime: 函数的总执行时间(包括调用子函数的时间)
第2个percall: cumtime除以ncalls的值
filename:lineno(function): 提供每个函数的数据(函数名以及其他信息)

'''

import math
import profile
def circlfArea(r):
    return math.pi * r * r

def sub(x,y):
    return x - y

def test():
    for i in range(10, 2000):
        print(circlfArea(i))
        if i % 2 == 0:
            print(sub(circlfArea(i * i), 10))

profile.run('test()','./files/test.profile')
