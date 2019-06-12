# 集合(Set)

'''
集合,必须满足下面的3个条件
1. 无须性: 集合中每一个元素的值都是平等的，元素之间是无序的
2. 互异性: 集合中任意两个元素都是不同的,每个元素只能在集合中出现一次
3. 确定性: 集合中每个元素都是确定的，对于一个值来说，要么属于该集合，
要么不属于该集合。所以集合、列表、字典都不能作为集合的元素值，因为他们都是可变的。

集合的操作:
创建集合、合并集合、集合相交、集合的差 等
'''
# 创建有10个元素的集合
set1 = set(range(10)) # 0-9十个数
print(set1)

set2 = set('helloabc')
print(set2)

set3 = set(['Bill','John','Mike','John'])
print(set3)

a = set((1,2,3))
b = set([3,5,1,6])
# 集合的合并
print(a.union(b))
print(a | b)
# 求a和b的交集
print(a.intersection(b))
print(a & b)

# 判断集合的子集
c = set([2,3])
print('c =',c)
print(c.issubset(a))
print(a.issubset(c))

# 判断集合的超集
print(a.issuperset(c))
print(c.issuperset(a))

# 判断集合是否相等
d = set([1,3,2])
print(a == d) # True

# 计算集合的差集 a - c
print(a.difference(b))
print(a - b)

# 计算集合之间的对称差
# 对称差：只在一个集合中出现的元素组成的新集合
"""
a = set((1,2,3))
b = set([3,5,1,6])
对称差为新集合:set(2,5,6)
"""
print(a.symmetric_difference(b))
print(a ^ b)

# 等效为(a-b) union (b-a)
print((a-b) | (b-a))
print((a.difference(b)).union((b.difference(a))))

# 集合的copy
x = a.copy()
y = a
print(y is a) # y是a的引用 True
print(x is a) # 两个完全不一样的集合，虽然元素值一模一样 False

x.add(30)
y.add(100)
print(x)
print(y)
print(a)

print(1 in a) # True
print(10 in a) # False

