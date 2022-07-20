# 导包
import time
from time import strftime
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
    目标： 截屏
    方法：
        driver.get_screenshot_as_file()
    需求：
        1. 输入用户名
        2. 截图 当前目录下 admin.png
"""
# 输入 admin
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 调用截图方法
driver.get_screenshot_as_file("./admin.png")
# 存放指定目录
driver.get_screenshot_as_file("./admin02.png")

# 动态获取文件名称 使用时间戳
# driver.get_screenshot_as_file("./%s.png" % (time.strftime("%Y_%m_%d %H_%M_%S")))
# driver.get_screenshot_as_file("./%s.jpg" % (time.strftime("%Y_%m_%d %H_%M_%S")))
# 报错
driver.get_screenshot_as_file("./%s.jpg" % (strftime("%Y_%m_%d %H_%M_%S")))
# 正确
driver.get_screenshot_as_file("./%s.png" % (strftime("%Y_%m_%d %H_%M_%S")))

# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
