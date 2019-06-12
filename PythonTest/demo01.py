# 测试

'''
1. 测试的一些基础知识
2. 测试工具(doctest、unittest)
3. 检查代码(PyLint,Flake8)
4. 性能分析

1. 先测试，后编码
coding -> run -> testing -> find bug -> debug

为代码规定一个边界。abc > 20,a和b,a > b

测试驱动开发
步骤:
1. 确定代码要达到的预期，然后为这个预期编写测试代码。
2. 编写骨架代码。
3. 编写业务逻辑代码。
4. 修改或重构代码

'''
import math

def circleArea(r):
    return math.pi * r * r

r = 100

# 指定边界
# 第一个边界
if r <= 0:
    print('测试失败，圆半径必须大于0！！！')

else:
    area = circleArea(r)
    # 第2个边界
    if area > 1000:
        print('测试失败，圆面积不能大于1000!!!')
    else:
        print('测试成功!!!')






