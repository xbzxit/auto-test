import unittest


class Test02(unittest.TestCase):
    def test001(self):
        print("test001被执行")

    def test002(self):
        print("test002被执行")

    def test003(self):
        print("test003被执行")

    def test004(self):
        print("__name__的值：", __name__)
        print("test004被执行")

if __name__ == '__main__':
    print("__name__的值：", __name__)


"""
    __name__: 为python中内置变量
        值：
            1. 如果当前运行的模块为当前模块，那么__name__的值为：__main__
            2. 如果当前运行的模块不是主模块，那么__name__的值为：模块名称
"""