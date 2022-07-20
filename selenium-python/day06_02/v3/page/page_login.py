"""
页面对象层：
    页面对象编写技巧：
        类名：使用大驼峰将模块名称抄进来，有下滑线去掉下划线
        方法：根据业务需求每个操作步骤单独封装一个方法
            方法名 page_XXX

"""
from selenium import webdriver


class PageLogin:
    def __init__(self):
        # 获取driver对象
        self.driver = webdriver.Chrome()
        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(30)
        # 打开url
        self.driver.get("http://localhost")

    # 点击登录 连接
    def page_click_login_link(self):
        self.driver.find_element_by_partial_link_text("登录").click()

    # 输入用户名
    def page_input_username(self, username):
        self.driver.find_element_by_css_selector("#username").send_keys(username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.driver.find_element_by_css_selector("#password").send_keys(pwd)

    # 输入验证码
    def page_input_verify_code(self, code):
        self.driver.find_element_by_css_selector("#verify_code").send_keys(code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.driver.find_element_by_css_selector(".J-login-submit").click()

    # 获取异常提示信息
    def page_get_text(self):
        return self.driver.find_element_by_css_selector(".layui-layer-content").text

    # 点击提示框确定按钮
    def page_click_err_btn_ok(self):
        self.driver.find_element_by_css_selector(".layui-layer-btn0").click()

    # 组装登录业务方法  给业务层调用
    def page_login(self, usrename, pwd, code):
        self.page_click_login_link()
        self.page_input_username(usrename)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()
