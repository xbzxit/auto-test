# 导包
import unittest
from parameterized import parameterized

from v3.page.page_login import PageLogin

# 新建测试类
class TestLogin(unittest.TestCase):

    # 初始化方法
    def setUp(self):
        # 获取登录页面对象
        self.login = PageLogin()

    # 结束方法
    def tearDown(self):
        # 关闭驱动对象
        self.login.driver.quit()

    # 新建测试方法
    @parameterized.expand([("13822223333","123456","8888","账号不存在!"), ("13800001111","123123","8888","密码错误!")])
    def test_login(self, username, pwd, code, expect):
        # 调用测试登录方法
        self.login.page_login(username, pwd, code)
        # 获取登录后的信息
        msg = self.login.page_get_text()
        try:
            # 断言
            self.assertEqual(msg, expect)
            # 点击确定
            self.login.page_click_err_btn_ok()
        except AssertionError:
            # 截图
            pass