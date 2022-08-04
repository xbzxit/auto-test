# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 设置元素等待  隐式等待 重要重要重要！！！
# 设置隐式等待10秒。
driver.implicitly_wait(10)
# 打开url
url = "file:///D:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)

"""
    目标：隐式等待使用
"""
# 给一个错误的id，不能知道，如果直接抛出异常，说明等待失效。如果在设置指定时长以外抛出说明等待生效。
driver.find_element_by_css_selector("#userA").send_keys("admin")

# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
