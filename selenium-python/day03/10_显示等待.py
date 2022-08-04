# 导包
from time import sleep

from selenium import webdriver
# 获取浏览器驱动对象
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.maximize_window()
# 设置元素等待  隐式等待 重要重要重要！！！
# 打开url
url = "file:///D:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)

"""
    目标：显示等待使用
    操作：
        1. 导包 WebDriverWait()类
        2. 实例化WebDriverWait()类并调用until(method)方法
        method：匿名函数
        lambda x:x.find_element_by_id()
        
    需求：
        定位用户名输入admin
"""
# 实例化WebDriverWait()并调用until方法
# 注意：调用until方法返回的一定是一个元素
WebDriverWait(driver, timeout=10, poll_frequency=0.5).until(lambda x: x.find_element_by_id("#user")).send_keys("admin")
# 注意：此时username还不是元素，只有代码运行起来才是元素
# username.send_keys("admin")


# 写法2
# 获取 WebDriverWait示例对象
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
# 获取元素
username = wait.until(lambda x: x.find_element_by_id("#user"))
# 发送内容
username.send_keys("admin")
# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
