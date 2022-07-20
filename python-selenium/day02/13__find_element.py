"""
    目标：
        driver.find_element()

    需求：
        1. 使用driver.find_element()方法
        2. 输入用户名：admin
        3. 输入密码：123456
"""

from time import sleep

# 导包
from selenium import webdriver
# 获取 浏览器驱动对象
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# 打开 注册A.html
url = r"file:///d:/workspace_python/python-selenium/html/注册A.html"
driver.get(url)

# 使用find_element()定位用户名
driver.find_element(By.ID, "userA").send_keys("admin")
# 使用find_element()定位密码
driver.find_element(By.CSS_SELECTOR, "#passwordA").send_keys("123456")

# 暂停 3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
