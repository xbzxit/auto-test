from day06_02.v5 import page

from day06_02.v5.base.base import Base


class PageLogin(Base):

    # 点击 登录连接地址 封装
    def page_lick_login_link(self):
        self.base_click(page.login_link)

    # 输入 用户名 封装
    def page_input_username(self):
        pass

    # 输入 密码 封装
    def page_input_pwd(self):
        pass

    # 输入 验证码 封装
    def page_input_code(self):
        pass

    # 点击登录按钮 封装
    def page_click_login_btn(self):
        pass

    # 组装 封装
    def page_login(self):
        pass