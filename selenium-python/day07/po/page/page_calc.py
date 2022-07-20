from selenium.webdriver.common.by import By

from day07.po import page
from day07.po.base.base import Base


class PageCalc(Base):

    # 点击数字方法
    def page_click_num(self, num):
        for n in str(num):
            # 拆开单个按钮的定位方式
            loc = By.CSS_SELECTOR, "#simple{}".format(n)
            self.base_click(loc)

    # 点击加号
    def page_click_add(self):
        self.base_click(page.clac_add)

    # 点击 等号
    def page_click_eq(self):
        self.base_click(page.clac_eq)

    # 获取结果方法
    def page_get_value(self):
        return self.base_get_value(page.clac_result)

    # 点击清屏
    def page_click_clear(self):
        self.base_click(page.clac_clear)

    # 截图
    def page_get_image(self):
        self.base_get_img()

    # 组装加法业务方法
    def page_add_calc(self, a, b):
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_eq()
