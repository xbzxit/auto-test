# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
# driver.implicitly_wait(30)
# 打开url
url = "file:///d:/workspace_test/selenium-python/html/注册实例.html"
driver.get(url)

"""
    目标： 为什么要切换窗口
    需求：
        1. 打开注册实例.html
        2. 点击 注册A网页
        3. 填写 注册A网页 内容
        
        
    
"""

# 点击注册A网页
driver.find_element_by_partial_link_text("A网页").click()

"""填写注册A"""
# 用户名
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#passwordA").send_keys("admin")
# 电话
driver.find_element_by_css_selector(".telA").send_keys("18611112222")
# 邮件
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")

# 暂停 2
sleep(3)
# 关闭驱动对象
driver.quit()
