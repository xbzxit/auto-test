"""
    需求：
        1. 使用partial_link_text定位方式，使用注册A.html页面，点击 访问 新浪 网站 连接地址
    方法：
        1. driver.find_element_by_partial_link_text("") # 定位元素方法
        2. click() # 点击方法
    注意：
        partial_link_text：
            1. 只能定位a标签
            2. partial_link_text定位元素的内容可以模糊部分值，但是必须能代表唯一性
"""

# 导包
from selenium import webdriver
from time import sleep


# 获取 浏览器驱动对象
driver = webdriver.Firefox()

# 打开 注册A.html
url = "file:///d:/workspace_python/python-selenium/html/注册A.html"
driver.get(url)

# 使用partial_link_text定位 使用模糊 唯一代表关键词
#driver.find_element_by_partial_link_text("访问").click()

driver.find_element_by_partial_link_text("问 新").click()

# 没有使用唯一代表词  默认操作符合条件的第一个元素
#driver.find_element_by_partial_link_text("新浪").click()

# 使用全部匹配
#driver.find_element_by_partial_link_text("访问 新浪 网站").click()

# 暂停 3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
