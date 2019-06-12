# 软链接与硬链接
# 软链接（符号链接 Symbolic link），相当于Windows的快捷方式
# 硬链接，是文件的副本
# 注意：该脚本文件必须在管理员模式下运行，否则权限不够,python3 demo04.py

# 只是要记住:
#   source 的 relative path是相对于 destination的
#   destination的relative path是相对于 当前路径的
# os.symlink(src,dst)
import os

# print(os.getcwd())
# 创建软链接
if os.path.exists('link/data.txt') and not os.path.exists('link/slink_data.txt'):
    # 建立软链接文件
    # 都是绝对路径保险一些
    os.symlink('G:/资料/PythonCodes2018/Python3ProjectExperiment/Python中常用模块/link/data.txt','G:/资料/PythonCodes2018/Python3ProjectExperiment/Python中常用模块/link/slink_data.txt')
    # os.symlink('../link/data.txt','./link/slink_data.txt')

# 创建硬链接
if os.path.exists('link/data.txt') and not os.path.exists('link/link_data.txt'):
    # 建立硬链接文件
    os.link('link/data.txt','link/link_data.txt')
