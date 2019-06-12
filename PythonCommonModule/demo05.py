# 用于获取和设置系统信息的函数和变量

# 在os模块

'''
1. sep变量: 用于返回当前操作系统(OS)的路径分隔符，Windows:反斜杠(\)
linux,Unix,Mac OS X:斜杠(/)。

2. pathsep变量: 返回环境变量中的路径之间的分隔符，Windows用分号(;)分隔多个路径
Linux和Mac OS X是冒号(:)。

3. name变量：返回当前OS的内核名称。

4. environ变量：以字典的形式返回系统中所有环境变量的值。

5. getenv函数: 获取指定的环境变量的值，通过参数可以指定环境变量名。

6. putenv函数: 设置指定环境变量的值，通过参数指定环境变量名和环境变量值。

7. system函数: 执行命令,通过参数指定要执行的命令。
'''

import os
import subprocess

print('路径分隔符：', os.sep)
print('环境变量路径之间的分隔符：', os.pathsep)
print('当前操作系统内核名：', os.name)
print(os.environ)

# 获取指定的环境变量值
print('PATH=',os.environ['PATH']) # 方法一
print('PATH=',os.getenv('PATH')) # 方法二

# 创建子进程执行testout.exe可执行程序
testout = subprocess.getstatusoutput('testout.exe')
print(testout)

# 以下这条语句在Windows下无效，在MAC OS X 下有效
# os.putenv('PATH', os.getenv('PATH') + os.pathsep + '.')
# 以下这条语句添加环境变量在Windows下同样是无效的，虽然在'PATH'的值的末尾添加进去了，同样没有用，在MAC OS X下有效
os.environ['PATH'] = os.getenv('PATH') + os.pathsep + \
                     'G:/资料/PythonCodes2018/Python3ProjectExperiment/Python中常用模块/test.exe'
print(os.getenv('PATH'))
testout_1 = subprocess.getstatusoutput('testout.exe')
print(testout_1)

# 执行可执行程序或者执行终端的命令行
os.system('testout.exe')
os.system('dir')


