import unittest

from parameterized import parameterized


def add(x, y):
    return x + y


"""
    问题：
        如果有三组数据需要测试？
        [(1,1,2), (1,2,3), (0,3,3)]
"""


def get_data():
    return [(1, 2, 3), (3, 0, 3), (2, 1, 3)]


# 定义测试类 并 继承
class Test01(unittest.TestCase):
    # 定义测试方法 注意：以test字母开头
    @parameterized.expand(get_data())
    def test_add(self, a, b, expect):
        # 调用 要是的函数
        result = add(a, b)
        assert result == expect
