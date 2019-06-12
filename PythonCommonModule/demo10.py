'''
时间元组
共9个变量
'''
import time

'''
返回值：
floating point number

返回值解释：
Return the current time in seconds since the Epoch.
'''
# print(time.time())
# 获取当前时间
localtime = time.localtime(time.time())
print(localtime) # localtime是一个对象
print(type(localtime))

st = time.struct_time((1,2,3,4,5,6,7,8,9))
print(st)
# abc = (1,2,3,4)
# print(abc[1])

print('年','=',localtime.tm_year)
print('月','=',localtime.tm_mon)
print('日','=',localtime.tm_mday)
print('一年的第%d天' % localtime[7])

# 获取一个可读的时间
localtime = time.asctime(localtime)
print(localtime)

'''
tm_year: 4位数字的年
tm_mon: 月
tm_mday: 日
tm_hour: 小时
tm_min: 分钟
tm_sec: 秒
tm_wday: 一周的第几日
tm_yday: 一年的第几日
tm_isdst: 夏令时 1:夏令时，0:不是夏令时，-1:未知，默认值是-1
'''