# 导包
import unittest

from parameterized import parameterized
from day06_02.v4.page.page_login import PageLogin


def get_data():
    return [("13822223333", "123456", "8888", "账号不存在!"),
            ("13800001111", "123123", "8888", "密码错误!")]


# 新建测试类 并 继承
class TestLogin(unittest.TestCase):
    login = None

    # setUp
    # classmethod
    @classmethod
    def setUpClass(cls):
        # 实例化 获取页面对象 PageLogin
        cls.login = PageLogin()
        # 点击登录连接
        cls.login.page_click_login_link()

    # tearDown
    @classmethod
    def tearDownClass(cls):
        # 关闭 driver驱动对象
        cls.login.driver.quit()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, expect_result):
        # 调用登录方法
        self.login.page_login(username, pwd, code)
        # 获取登录提示信息
        msg = self.login.page_get_error_info()
        try:
            # 断言
            self.assertEqual(msg, expect_result)
        except AssertionError:
            # 截图
            self.login.page_get_img()
