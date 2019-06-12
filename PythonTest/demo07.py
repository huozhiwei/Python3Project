# 性能分析

# profile内建模块

import pstats
# 读取对应目录下的profile文件
p = pstats.Stats('./files/test.profile')
p.print_stats()
