# 导包
import unittest
from time import sleep

from parameterized import parameterized

from day07_02.base.get_driver import GetDriver
from day07_02.page.page_login import PageLogin
from day07_02.tool.read_json import read_json


def get_data():
    arrs = []
    for data in read_json("login.json").values():
        arrs.append((data.get("username"),
                     data.get("password"),
                     data.get("verify_code"),
                     data.get("expect_result"),
                     data.get("success")))
    return arrs  # 注意：必须进行return 返回


# 新建测试类 并 继承
class TestLogin(unittest.TestCase):
    login = None

    # setUp

    @classmethod
    def setUpClass(cls):
        # 实例化 获取页面对象 PageLogin
        cls.login = PageLogin(GetDriver().get_driver())
        # 点击登录连接
        cls.login.page_click_login_link()

    # tearDown
    @classmethod
    def tearDownClass(cls):
        sleep(3)
        # 关闭 driver驱动对象
        GetDriver().quit_driver()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, expect_result, success):
        # 调用登录方法
        self.login.page_login(username, pwd, code)
        if success:
            try:
                # 判断安全退出是否存在
                self.assertTrue(self.login.page_is_login_success())
                # 点击退出
                self.login.page_click_logout()
                try:
                    self.assertTrue(self.login.page_is_logout_success)
                except:
                    # 截图
                    self.login.page_get_img()
                # 点击登录连接
                self.login.page_click_login_link()
            except:
                # 截图
                self.login.page_get_img()
        else:
            # 获取登录提示信息
            msg = self.login.page_get_error_info()
            try:
                # 断言
                self.assertEqual(msg, expect_result)

            except AssertionError:
                # 截图
                self.login.page_get_img()
            # 点击 确认框
            self.login.page_click_err_btn_ok()
