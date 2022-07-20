import unittest
from parameterized import parameterized

"""
    目标：parameterized 插件应用
    步骤：
        1. 导包 from parameterized import parameterized
        2. 修饰测试函数 @parmeterized.expand(列表类型数据)
        3. 在测试函数中使用变量接收，传递过来的值。
        
    语法：
        1. 单个参数：值为列表
        2. 多个参数：值为列表嵌套元组 如:[(1,2,3),(2,3,4)]
"""


# 定义测试类 并 继承
class Test01(unittest.TestCase):
    # 单个参数使用方法
    @parameterized.expand(["1", "2", "3"])
    def test_add_one(self, num):
        print("num:", num)

    # 多个参数使用方法 写法1
    @parameterized.expand([(1, 2, 3), (3, 0, 3), (2, 1, 3)])
    def test_add_more(self, a, b, result):
        print("{}+{}={}:".format(a, b, result))

    data = [(1, 2, 3), (3, 0, 3), (2, 1, 3)]

    # 写法2
    @parameterized.expand(data)
    def test_add_more(self, a, b, result):
        print("{}+{}={}:".format(a, b, result))

    # 写法 3 推荐
    def get_data(self):
        return [(1, 2, 3), (3, 0, 3), (2, 1, 3)]

    @parameterized.expand(get_data())
    def test_add_more(self, a, b, result):
        print("{}+{}={}:".format(a, b, result))
