from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化方法
    def __init__(self):
        # 获取driver
        self.driver = webdriver.Firefox()
        # 最大化
        self.driver.maximize_window()
        # 打开url
        self.driver.get("http://localhost")

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        # 使用显示等待
        """
        :param loc: 元素的配置信息，格式为元组 如：login_link = By.PartialLink, "登录"
        :param timeout: 默认超时时间为30，可以通过传入参数进行修改
        :param poll: 默认访问频率 0.5秒
        :return: 查找到的元素
        """
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 元素点击
    def base_click(self, loc):
        # 获取元素 并 进行点击
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)
