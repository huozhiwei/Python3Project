# unittest
# unittest比doctest在使用上复杂一些,但更灵活
# 类似于Java测试框架JUnit

'''
1. 导入unittest模块
2. 编写测试类,测试类必须从unittest.TestCase或其子类继承
3. 编写测试用例
4. 调用unittest模块中的main函数开始测试

'''

import unittest,demo02
# 定义测试类
class MyTest(unittest.TestCase):
    # 用于测试demo02.square()函数的方法
    def testSquare(self):
        # 使用一段连续的整数测试square函数
        for x in range(-20,20):
            result = demo02.square(x)
            self.assertEqual(result,x * x,'%d的二次方失败' %x)

    def testAdd(self):
        for x in range(-20,20):
            for y in range(-10,10):
                result = demo02.add(x,y)
                self.assertEqual(result, x + y, '%d + %d不正确' %(x,y))

if __name__ == '__main__': # 测试时一定加上这一条 if __name__ == '__main__':,否则无法导入测试案例
    print('begin')
    unittest.main()
    print('finished')