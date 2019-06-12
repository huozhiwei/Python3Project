#
# 练习题1:
#     编写一个Python程序,使用doctest模块测试下面factorial函数(阶乘函数).
#

'''
    测试factorial函数
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(4)
    24
    >>> factorial(6)
    720
'''

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return factorial(n-1) * n + 1

if __name__ == '__main__':
    import doctest,demo08
    doctest.testmod(demo08)


