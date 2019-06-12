# 格式化日期和时间

# 由日期格式转化为字符串格式的函数为: datetime.datetime.strftime()
# 由字符串格式转化为日期格式的函数为: datetime.datetime.strptime()
# d1 = datetime.datetime.strptime('2019-1-1','%Y-%m-%d')

# time.strftime函数，参数1：格式化字符串 参数2：时间元组
# strftime 全称：strformattime

# locale: n.发生地点;现场
# locale 这个单词中文翻译成地区或者地域
import time
import locale
# locale.setlocale(locale.LC_ALL,'zh_CN.UTF-8')
# 语言符号及其分类(LC_CTYPE)
locale.setlocale(locale.LC_CTYPE,'chinese')

# 2019-6-05 19:56:35
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(time.strftime('%Y年%m月%d日 %H时%M分%S秒',time.localtime()))

# 输出星期的完整名称
print(time.strftime('today is %A',time.localtime(time.time())))
print(time.strftime('今天是%A',time.localtime(time.time())))