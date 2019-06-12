# -*- coding:utf-8 -*-
import subprocess
# 导入子进程模块,并创建子进程
output = subprocess.getstatusoutput('python3 demo01.py John')
print(output)
print(output[0])