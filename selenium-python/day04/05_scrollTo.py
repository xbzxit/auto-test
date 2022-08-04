# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)
# 打开url
url = "file:///d:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)

"""
    目标：滚动条操作
    
    需求：
        1. 启动暂停2秒
        2. 滚动条拉倒最底下
"""
sleep(2)
# 第一步 设置js控制滚动条语句
js = "window.scrollTo(0, 10000)"
# 第二步 调用执行js语句方法
driver.execute_script(js)

# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
