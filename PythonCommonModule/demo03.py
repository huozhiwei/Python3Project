# 文件与目录操作

'''
1. mkdir(dirname,permissions)
permissions:r,w,x （可读，可写，可执行）
如果dirname存在，会抛出OSError异常

2. makedirs(dirname,permissions,exist_ok)
permissions:r,w,x （可读，可写，可执行）
(1) mkdir('a') mkdir('a/b') 如果a目录不存在,则不会创建a目录，也不会创建b目录
    makedirs('a/b/c') 如果a目录不存在，则会创建a目录,之后创建b目录,然后创建c目录
(2) 当exist_ok == false时,如果目录存在，抛出OSError异常；
    当exist_ok == True时，如果目录存在，什么都不做，不会抛出异常

3. rmdir(dirname): 删除目录
rmdir('a'),如果a目录不为空，会抛出OSError异常

4. removedirs(dirname): 删除目录
可以指定多级目录
removedirs('a/b/c')
b目录中含有:c目录,test.txt 只删除c目录，b目录和a目录保留

5. remove(filename): 删除filename指定的文件

6. rename(src,dst): 将src参数指定的文件(目录)改名为dst参数指定的文件名(目录名)

7. renames(src,dst):
a/b/c -> x/y/z
'''

import os
if not os.path.exists("newdir1"):
    os.mkdir('newdir1')
# os.mkdir('a/b/c') # 由于a目录不存在，所以会抛出FileNotFoundError异常
# 创建多级目录
os.makedirs('x/y/z',0o733,True) # ('0o100', '0x40', '0b1000000') 8进制，16进制，2进制
try:
    # 删除单个目录
    os.rmdir('newdir1')
    pass
except OSError as e:
    print(e) # [WinError 145] 目录不是空的。: 'newdir1'

# 删除多级目录
os.removedirs('x/y/z')

if not os.path.exists('mydir'):
    os.mkdir('mydir')
    os.rename('mydir','yourdir')

if os.path.exists('x/y/z'):
    # 重命名多级目录
    os.renames('x/y/z','bill/mike/john')

# 删除文件
if os.path.exists('newdir1/test.txt'):
    os.remove('newdir1/test.txt')