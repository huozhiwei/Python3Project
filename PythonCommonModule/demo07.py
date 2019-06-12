# 将集合作为集合的元素
# frozenset函数
# 集合的元素和字典中的key都不允许是可变类型的值，如集合、列表和字典，
# 元组,字符串,数字 既可以作集合的元素，也可以作字典的key


a = set([1, 2])
b = set([10, 20])
a.add('hello')
print(a)

# 直接将集合b作为a的元素会直接抛出异常，因为普通的集合是可变类型
# a.add(b)
a.add(frozenset(b))
print(a)

d = {'Bill':30,"John":34}
# d[a] = 10 # 抛出异常
d[frozenset(a)] = 10
print(d)

# b.add(d) # 抛出异常,因为集合的元素必须是不可变的
t = (1,2,3,4)
b.add(t)
d[t] = 25
print(b)
print(d)
