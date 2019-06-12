# -*- coding:utf-8 -*-
# Python中的常用模块: sys模块

import sys
# print(sys.path)
# 将模块所在的路径添加到sys.path列表中
sys.path.append("./test")
import my

my.greet('zzw')
print(sys.modules['my'])
print(type(sys.modules['my']))
print(sys.platform)

# 命令行参数
# 输出当前脚本文件的完整路径
# 在Run-> Edit Configurations里面输入参数值zzw
# 或者cmd,cd到当前py文件所在路径之后,输入命令:python3 demo01 zzw
print(sys.argv[0])
if len(sys.argv) == 2:
    print(sys.argv[1])
    my.greet(sys.argv[1])

# 标准输入输出流
s = sys.stdin.read(6) # 6个字符
print(s)
sys.stdout.writelines("hello world\n钟志炜")
# 标准错误流
sys.stderr.writelines('error') # 标准输出流和标准错误流是异步执行的，不知道谁在前谁在后执行

sys.exit(123)