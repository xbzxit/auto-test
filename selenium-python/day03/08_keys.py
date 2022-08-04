# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开url
url = "file:///d:/workspace_test/selenium-python/html/注册A.html"

driver.get(url)
"""
    目标：学习使用基于selenium完成键盘操作
    案例：
        1. 输入用户名admin1
        2. 删除 1 
        3. 全选 用户名 "admin"  Ctrl+A
        4. 复制 admin Ctrl+C
        5. 粘贴 将复制的admin粘贴到密码框
    分析：
        1. 导包 Keys
        2. 调用 send_keys(Keys.XXX,'a')
        
"""
# 定位 用户名
username = driver.find_element_by_css_selector("#userA")
# 输入 admin1
username.send_keys("admin1")
sleep(2)
# 删除1
username.send_keys(Keys.BACK_SPACE)
username.send_keys(Keys.BACK_SPACE)
username.send_keys(Keys.BACK_SPACE)
sleep(2)

# 全选 admin Ctrl+a
username.send_keys(Keys.CONTROL, "a")
sleep(2)

# 复制 Ctrl+c
username.send_keys(Keys.CONTROL, "c")
sleep(2)

# 定位密码框 并执行 Ctrl+v
driver.find_element_by_css_selector("#passwordA").send_keys(Keys.CONTROL, "v")

# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
