# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器对象
driver = webdriver.Firefox()
# 打开 url
url = "file:///d:/workspace_python/python-selenium/html/注册A.html"
driver.get(url)
# 查找元素 用户名 并 输入admin
driver.find_element_by_id("userA").send_keys("admin")
# 查找元素 密码框 并 输入123456
driver.find_element_by_id("passwordA").send_keys("123456")
# 暂停3秒
sleep(3)
# 关闭浏览器驱动对象
driver.quit()
