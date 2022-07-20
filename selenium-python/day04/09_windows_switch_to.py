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
url = "file:///d:/workspace_python/python-selenium/html/注册实例.html"
driver.get(url)

"""
    目标： 切换窗口
    需求：
        1. 打开注册实例.html
        2. 点击 注册A网页
        3. 填写 注册A网页 内容
        
        
    
"""

# 获取当前窗口句柄  -->目的：判断只要不是当前主窗口句柄，就一定是新开的窗口句柄
current_handle = driver.current_window_handle
print("当前窗口句柄为：", current_handle)
# 点击注册A网页
driver.find_element_by_partial_link_text("A网页").click()

# 获取所有窗口句柄
handles = driver.window_handles
print("所有窗口句柄：", handles)

# 判断 不是 当前窗口句柄
for h in handles:
    if h != current_handle:
        # 切换
        driver.switch_to.window(h)
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
sleep(2)
# 关闭驱动对象
driver.quit()
