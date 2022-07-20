import time
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化方法
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """
        :param loc:  元素的定位信息，格式为元祖
        :param timeout: 默认超时时间30秒
        :param poll: 访问频率，默认0.5查找一次元素
        :return: 返回查找到的元素
        """
        # 显示等待
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击
    def base_click(self, loc):
        # 调用查找元素 并 进行点击
        self.base_find_element(loc).click()

    # 获取value属性方法封装
    def base_get_value(self, loc):
        # 使用get_attribute()方法获取指定的元素属性值
        # 注意：返回
        return self.base_find_element(loc).get_attribute("value")

    # 截图
    def base_get_img(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
