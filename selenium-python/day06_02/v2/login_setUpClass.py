# 导包
import unittest

from selenium import webdriver


# 新建测试类 并继承
class TestLogin(unittest.TestCase):
    driver = None

    # 初始化 setUp
    @classmethod
    def setUpClass(cls):
        # 获取driver对象
        cls.driver = webdriver.Firefox()
        # 最大化浏览器
        cls.driver.maximize_window()
        # 隐式等待
        cls.driver.implicitly_wait(30)
        # 打开url
        cls.driver.get("http://localhost")
        # 点击登录连接
        cls.driver.find_element_by_partial_link_text("登录").click()

    # 结束 tearDown
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.driver.quit()

    # 新建测试方法 用户名不存在
    def test_login_username_not_exist(self):
        driver = self.driver
        # 输入用户名
        username = driver.find_element_by_css_selector("#username")
        username.clear()
        username.send_keys("13011112222")
        # 输入密码
        pwd = driver.find_element_by_css_selector("#password")
        pwd.clear()
        pwd.send_keys("123456")
        # 输入验证码
        code = driver.find_element_by_css_selector("#verify_code")
        code.clear()
        code.send_keys("8888")
        # sleep(2)
        # 点击登录按钮
        driver.find_element_by_css_selector(".J-login-submit").click()
        # sleep(2)
        # 获取错误提示信息
        msg = driver.find_element_by_css_selector(".layui-layer-content").text
        print("msg:", msg)
        try:
            # 断言
            self.assertEqual(msg, "账号不存在!")
            # 点击提示框确定按钮
            driver.find_element_by_css_selector(".layui-layer-btn0").click()
        except AssertionError:
            # 截图
            driver.get_screenshot_as_file("../image/fail.png")

    # 新建测试方法 密码错误
    def test_login_password_err(self):
        driver = self.driver
        # 输入用户名
        username = driver.find_element_by_css_selector("#username")
        username.clear()
        username.send_keys("13800001111")
        # 输入密码
        pwd = driver.find_element_by_css_selector("#password")
        pwd.clear()
        pwd.send_keys("123123")
        # 输入验证码
        code = driver.find_element_by_css_selector("#verify_code")
        code.clear()
        code.send_keys("8888")
        # sleep(2)
        # 点击登录按钮
        driver.find_element_by_css_selector(".J-login-submit").click()
        # sleep(2)
        # 获取错误提示信息
        msg = driver.find_element_by_css_selector(".layui-layer-content").text
        print("msg:", msg)
        try:
            # 断言
            self.assertEqual(msg, "密码错误!")
            # 点击提示框确定按钮
            driver.find_element_by_css_selector(".layui-layer-btn0").click()
        except AssertionError:
            # 截图
            driver.get_screenshot_as_file("../image/fail.png")
