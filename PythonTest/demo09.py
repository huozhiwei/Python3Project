'''
编写一个Python程序,使用unittest模块测试第1题(demo08.py)的factorial函数.
'''
import unittest,demo08
import numpy as np

class TestCase(unittest.TestCase):
    def testFactorial(self):
        for x in range(0, 10):
            result = demo08.factorial(x)
            self.assertEqual(result, np.math.factorial(x),'%d的阶乘失败' %x)

        if __name__ == '__main__':
            unittest.main()