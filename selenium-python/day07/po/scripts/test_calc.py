import unittest

from parameterized import parameterized

from day07.po.base.get_driver import GetDriver
from day07.po.page.page_calc import PageCalc
from day07.po.tool.read_json import read_json


def get_data():
    datas = read_json("calc.json")

    # 新建空列表
    arrs = []
    for data in datas.values():
        arrs.append((data['a'], data['b'], data['expect']))
    return arrs


class TestCalc(unittest.TestCase):
    driver = None

    # setupclass
    @classmethod
    def setUpClass(cls):
        # 获取driver
        cls.driver = GetDriver().get_driver()
        # 初始化 计算页面对象
        cls.calc = PageCalc(cls.driver)

    # teardown
    @classmethod
    def tearDownClass(cls):
        # 关闭driver
        GetDriver().quit_driver()

    # 测试加法 方法
    @parameterized.expand(get_data())
    def test_add_calc(self, a, b, expect):
        # 调用计算业务方法
        self.calc.page_add_calc(a, b)
        print("预期结果为：", expect, "实际计算结果为：", self.calc.page_get_value())
        try:
            # 断言
            self.assertEqual(self.calc.page_get_value(), str(expect))
        except:
            # 截图
            self.calc.page_get_image()
            raise
