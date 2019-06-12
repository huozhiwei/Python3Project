# 随机数
'''

randint(m,n):用于产生m到n之间的随机整数，包括m和n。
random(): 用于产生0到1之间的随机浮点数，包括0，但不包括1。
uniform(m,n): 用于产生m到n之间的随机浮点数,m和n可以是浮点数，包括m和n。
randrange(m,n,step): 在一个递增的序列中随机选择一个整数,其中step是步长。
例如: randrange(1,6,2),该函数就会在列表[1,3,5]中随机选择一个整数。
choice(seq): 从seq指定的序列中随机选择一个元素值。seq指定的列表元素可以是任意类型的值。
sample(seq,k): 从seq指定的序列中随机选取k个元素，然后生成一个新的序列。
洗牌：shuffle(seq): 把seq指定的序列中元素的顺序打乱，该函数直接修改原有的序列。
'''

import random
# 产生1到100之间的随机整数
print(random.randint(1,100))

# 产生0到1之间的随机数
print(random.random())

# 从[1,4,7,10,13,16,19]中随机选择一个元素
print(random.randrange(1,20,3))

# 产生一个从1到100.5的随机浮点数
print(random.uniform(1,100.5))

# 从一个列表中随机选择一个元素
intList = [1,2,5,7,76,10,4,8]
print(random.choice(intList))

# 从一个列表(intlist)中随机选择3个元素，然后将这3个元素组成一个新的列表(newlist)
newList = random.sample(intList,3)
print(newList)

# 随机洗牌操作，随机打乱一个列表中的元素顺序
random.shuffle(intList)
print(intList)