# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)
# 打开url
url = "file:///d:/workspace_python/python-selenium/html/注册A.html"
driver.get(url)

"""
    需求：
        1. 点击 alert按钮
        2. 输入用户名 admin
"""
# 定位 alert按钮 并 点击
driver.find_element_by_css_selector("#alerta").click()
# 定位 用户名 输入admin
driver.find_element_by_css_selector("#userA").send_keys("admin")


# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
