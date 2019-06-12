# 获取与改变工作目录
import os

# 获取当前的工作目录
print('当前工作目录：',os.getcwd())

# 列出当前工作目录的所有目录和文件，但是不递归地列出以下的子目录和子文件
print(os.listdir(os.getcwd())) # 返回值是一个列表

# 修改当前的工作目录
# 修改当前的工作目录到上一层
os.chdir('../')
print('改变后的工作目录：',os.getcwd())
print(os.listdir(os.getcwd()))