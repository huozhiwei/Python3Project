# doctest

#
# doctest模块用来检测文档，也可以用来编写测试代码，
# 这些代码必须写在多行注释中。要测试这些代码，前面需要加3个大于号(>),
# 然后返回值会放到下一行。最后可以通过doctest模块中的testmod函数
# 测试指定的模块，测试结果会通过Console输出。
#
#
# square,add

'''
    测试square函数
    >>> square(2)
    4
    >>> square(6)
    36

    测试add函数
    >>> add(2,2)
    4
    >>> add(4,5)
    9
'''
def square(x):
    return x ** x

def add(x,y):
    return x + y

import doctest
import demo02
# doctest.testmod(demo02)
# print('end')

'''

1. testmod函数只会处理模块中第1个多行注释，并且不能在第1个多行注释前面。
有任何Python代码。
2. >>>与要执行的代码之间要有空格，不能连在一起。
3. 函数返回值(多行注释里面要测试的结果)后面不要有空格，否则无法通过测试。
4. 用于注释的文本和函数返回值之间要有空行，否则系统会将注释当作函数返回值处理。

'''

