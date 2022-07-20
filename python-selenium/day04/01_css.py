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
url = "file:///d:/workspace_python/python-selenium/html/注册A.html"
driver.get(url)

"""
    目标： 默认北京A
        暂停2秒
        1. 定位 A上海
        2. 暂停2秒
        3. 定位 A广州
"""
"""方式1：使用CSS定位"""
sleep(2)
# 使用css定位来操作 A上海
driver.find_element_by_css_selector("[value='sh']").click()
sleep(2)
# 使用css定位 A广州
driver.find_element_by_css_selector("[value='gz']").click()

# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
