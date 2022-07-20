"""
    目标：unittest框架--TestCase使用
    步骤：
    案例：
        编写 求和测试函数
"""
# 导包
import unittest


# 编写求和函数
def add(x, y):
    return x + y


# 定义测试类 并 继承
class Test01(unittest.TestCase):

    # 定义测试方法 注意：以test字母开头
    def test_add(self):
        # 调用要用的函数
        result = add(1, 1)
        print("结果为：", result)

    def test_add02(self):
        result = add(1, 2)
        print("结果为：", result)
        # 文件名
        print("__name__内置变量获取当前运行的模块名称：", __name__)

    def eest_add03(self):
        result = add(1, 2)
        print("结果为：", result)


# 可以这么使用
# unittest.main("test01_testcase")

if __name__ == '__main__':
    test = Test01()
    test.test_add()
