# 时间戳的增量

import time
curtime = time.time() # 单位s
futtime = curtime + 60 # 向后加上60s,即1min
print(futtime)
# 未来1h
futtime1 = curtime + 60 * 60 # 3600s, 1h
futtime1 = time.localtime(futtime1)
print(futtime1)
print(time.strftime('%Y-%m-%d %H:%M:%S',futtime1))

# 过去1h
futtime2 = curtime - 60 * 60
futtime2 = time.localtime(futtime2)
print(futtime2)
print(time.strftime('%Y-%m-%d %H:%M:%S',futtime2))