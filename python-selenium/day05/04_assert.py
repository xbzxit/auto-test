import unittest
"""
    目标：unittest常用断言
        1. assertTrue : 如果结果为True通过，否则失败
        
"""

class Test02(unittest.TestCase):
    def test001(self):
        # 断言是否为True
        flag = True
        flag = False
        self.assertTrue(flag)
        # self.assertFalse(flag)

        # 判断两个字符串是否相等
        # self.assertEqual("你好，斑马！", "你好，奥码！")
        # self.assertEqual("你好，斑马！", "你好，斑马！")

        # 判断后边的字符串是否包含前边的字符串
        # self.assertIn("hello bama", "hello bama,wahaha")
        # self.assertIn("hello wahaha", "hello bama,wahaha")

        # 判断是否为None
        # flag = None
        # # self.assertIsNone(flag)
        # self.assertIsNotNone(flag)