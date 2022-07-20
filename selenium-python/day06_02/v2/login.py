import unittest

from selenium import webdriver


class TestLogin(unittest.TestCase):

    # 初始化 setUp
    def setUp(self):
        def setUp(self):
            # 获取driver对象
            self.driver = webdriver.Chrome()
            # 最大化浏览器
            self.driver.maximize_window()
            # 隐式等待
            self.driver.implicitly_wait(30)
            # 打开url
            self.driver.get("http://localhost")
            # 点击登录连接
            self.driver.find_element_by_partial_link_text("登录").click()

    # 结束 tearDown
    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()

    # 新建测试方法 用户名不存在
    def test_login_username_not_exist(self):
        driver = self.driver
        # 输入用户名
        driver.find_element_by_css_selector("#username").send_keys("13011112222")
        # 输入密码
        driver.find_element_by_css_selector("#password").send_keys("123456")
        # 输入验证码
        driver.find_element_by_css_selector("#verify_code").send_keys("8888")
        # 点击登录按钮
        driver.find_element_by_css_selector(".J-login-submit").click()
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
        driver.find_element_by_css_selector("#username").send_keys("13800001111")
        # 输入密码
        driver.find_element_by_css_selector("#password").send_keys("123123")
        # 输入验证码
        driver.find_element_by_css_selector("#verify_code").send_keys("8888")
        # 点击登录按钮
        driver.find_element_by_css_selector(".J-login-submit").click()
        # 获取错误提示信息
        msg = driver.find_element_by_css_selector(".layui-layer-content").text
        print("msg:", msg)
        try:
            # 断言
            self.assertEqual(msg, "密码!")
            # 点击提示框确定按钮
            driver.find_element_by_css_selector(".layui-layer-btn0").click()
        except AssertionError:
            # 截图
            driver.get_screenshot_as_file("../image/fail.png")
