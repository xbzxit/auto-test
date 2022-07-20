# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(3)
# 打开url
url = "file:///d:/workspace_python/python-selenium/html/注册实例.html"
driver.get(url)

"""
    目标： 为什么要切换frame表单
    需求：
        1. 打开注册实例.html
        2. 填写主页面 页面信息
        3. 填写注册A 页面信息
        4. 填写注册B 页面信息
    
"""
"""填写主页面"""
# 用户名
# driver.find_element_by_css_selector("#user").send_keys("admin")
# # 密码
# driver.find_element_by_css_selector("#password").send_keys("admin")
# # 电话
# driver.find_element_by_css_selector(".tel").send_keys("18611112222")
# # 邮件
# driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

"""填写注册A"""
# 用户名
# driver.find_element_by_css_selector("#userA").send_keys("admin")
# # 密码
# driver.find_element_by_css_selector("#passwordA").send_keys("admin")
# # 电话
# driver.find_element_by_css_selector(".telA").send_keys("18611112222")
# # 邮件
# driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")

"""填写注册B"""
# 用户名
driver.find_element_by_css_selector("#userB").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#passwordB").send_keys("admin")
# 电话
driver.find_element_by_css_selector(".telB").send_keys("18611112222")
# 邮件
driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")

# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
