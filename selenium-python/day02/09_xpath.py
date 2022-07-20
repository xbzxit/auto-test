"""
    需求：
        1. 使用绝对路径定位 用户名 输入 admin
        2. 暂停2秒钟
        3. 使用相对路径定位 密码框 输入 123

    方法：
        driver.find_element_by_xpath()
"""

from time import sleep

# 导包
from selenium import webdriver

# 获取 浏览器驱动对象
driver = webdriver.Firefox()

# 打开 注册A.html
url = "file:///d:/workspace_python/python-selenium/html/注册A.html"
driver.get(url)

# 使用绝对路径定位 用户名 admin
# driver.find_element_by_xpath("/html/body/form/div/fieldset/p[1]/input").send_keys("admin")

# 使用层级结合属性 定位用户名：  //p[@id='p1']/input
driver.find_element_by_xpath("//p[@id='userA']").send_keys("admin")

# 暂停2秒
sleep(2)

# 使用相对路径 定位 密码  123
# driver.find_element_by_xpath("//input[@id='passwordA']").send_keys("123")


# 使用逻辑结合
driver.find_element_by_xpath("//input[@id='passwordA' and @placeholder='密码A']").send_keys("123")
# 暂停 3秒
sleep(113)
# 退出浏览器驱动
driver.quit()
