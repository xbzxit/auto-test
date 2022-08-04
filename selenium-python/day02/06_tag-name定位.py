"""
    需求：
        1. 使用tag_name定位方式，使用注册A.html页面，用户名输入admin
    方法：
        1. driver.find_element_by_tag_name("") # 定位元素方法
        2. send_keys() # 输入方法
        3. driver.quit() # 退出方法
"""

from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "file:///d:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)

driver.find_element_by_tag_name("input").send_keys("admin1234")

sleep(10)

driver.quit()
