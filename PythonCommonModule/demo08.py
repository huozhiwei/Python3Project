# 堆（Heap）
# module: heapq
# 堆对象实际是以列表的形式存储的

from heapq import *
from random import *

data = [1,2,3,4,5,6,7,8,9]
heap = []
for n in data:
    value = choice(data) # random.choice(list)
    # 将值value添加到堆
    heappush(heap,value) # heap.heappush
print(heap) # list对象
heappush(heap,30)
heappush(heap,45)
print(heap)

# 弹出堆中最小值
print(heappop(heap))

data1 = [6,3,1,12,9]
# 将列表修改为堆对象,直接修改data1
heapify(data1)
print(type(data1))
print(data1)

# 将堆中最小值替换成给定的值
ret = heapreplace(data1,123)
print(ret)
print(data1)

# 得到堆中前n个最大的值
print(nlargest(1,data1)) # [123]
print(nlargest(3,data1)) # [123, 12, 9]

# 得到堆中前n个最小的值
print(nsmallest(1,data1)) # [3]
print(nsmallest(2,data1)) # [3, 6]
print(nsmallest(3,data1)) # [3, 6, 9]

print(list(merge([1,3,456,7],[0,1,-5,6],[1,7,4],[],[67])))

print(list(merge(['dog','horse'],['cat','fish','kangraoo'],key=len)))