'''
练习题1：
    编写一个Python程序，从一个列表中随机抓取3个元素值，
并按取值顺序将元素值组成3级目录，然后创建这个3级目录。
例如，有一个列表['a','b','c','d','e']
现在随机取的值依次是‘a’,'b','c',组成的3级目录是'a/b/c',
然后使用相应的函数创建这个3级目录即可。
'''
import random
import os

strList = ['abc','bbb',30,'xyz','ddd','ok','666']

newList = random.sample(strList,3)
dirStr = ''
for dir in newList:
    dir += os.sep
    dirStr += dir
print(dirStr)
os.makedirs(dirStr,exist_ok=True)
# os.removedirs(dirStr)