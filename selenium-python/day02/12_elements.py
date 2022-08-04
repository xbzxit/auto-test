"""
    目标：
        driver.find_elements_by_xxx
"""

from time import sleep

# 导包
from selenium import webdriver

# 获取 浏览器驱动对象
driver = webdriver.Firefox()

# 打开 注册A.html
url = "file:///d:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)

# 获取所有的input元素
# elements = driver.find_elements_by_tag_name("input")

elements = driver.find_elements_by_id("userA")
print(len(elements))
print("elements的类型为：", type(elements))

# 输入内容
# elements[0].send_keys("admin")

# 通过遍历来输入
for el in elements:
    el.send_keys("admin")

# 暂停 3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
