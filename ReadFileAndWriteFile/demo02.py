# 管道输出
# | : 左边命令的输出作为右边命令的输入
# ls -a; |grep zzw
# grep:过滤
# 过滤包含关键字'zzw'的列表行

# 从标准输入读取所有的数据，并按行将数据保存到列表中，并过滤
# 过滤出所有包含'readme'的行，输出这些行

'''
ls -al ~
python demo02.py
sort

linux 下跳转到该py文件demo02.py的路径下,输入命令行:
ls -al ~ | python3 demo02.py | sort
'''
import sys
import os
import re

# 从标准输入读取全部数据
text = sys.stdin.read()

files = text.split(os.linesep) # 按行分割

for file in files:
    # .                    匹配任意字符（不包括换行符）
    # *                    匹配前一个元字符0到多次
    result = re.match('.*readme.*',file)
    if result != None:
        print(file)

