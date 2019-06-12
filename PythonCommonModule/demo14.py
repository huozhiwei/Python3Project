# 获取某月和末年的日历
import calendar
import locale

# 返回2019年1月份的日历
cal = calendar.month(2019,1)
print(cal)

locale.setlocale(locale.LC_ALL,'english')

# 返回2019年一整年的日历
print(calendar.calendar(2019))