# 双端队列
# 导入类deque

from collections import deque

# 将列表转换为双端队列
# List = list(range(10))
dq = deque(range(10))
print(dq)

# 将123追加到队列dq的队尾
dq.append(123)
dq.append(-32)
print(dq)

# 列表左端队首，右端队尾
# 将30添加到dq的队首
dq.appendleft(30)
print(dq)

# 弹出队尾的值
print(dq.pop())
# 弹出队首的值
print(dq.popleft())

print(dq)

# 双端队列的元素全部向左移动两个位置
# 将dq向左循环移动2个位置
dq.rotate(-2)
print(dq)

# 将dq向右循环移动4个位置
dq.rotate(4)
print(dq)

# 创建一个双端队列dq1
dq1 = deque(['a','b'])
# 向dq队尾添加双端队列dq1
dq.extend(dq1)
print(dq)

# 向dq队首添加双端队列dq1
dq.extendleft(dq1)
print(dq)
