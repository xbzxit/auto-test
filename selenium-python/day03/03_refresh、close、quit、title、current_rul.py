# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 将浏览器 最大化
# driver.maximize_window()
# 打开url
url = "file:///d:/workspace_test/selenium-python/html/注册实例.html"
driver.get(url)

# 用户名输入 admin  目的：刷新完成--清空
driver.find_element_by_css_selector("#user").send_keys("admin")

# 暂停2秒
sleep(2)
# 刷新
driver.refresh()
# 获取title
title = driver.title
print("当前页面title为：", title)

# 获取当前url
current_rul = driver.current_url
print("当前页面url地址为：", current_rul)

# 点击 注册A网页 打开新窗口
# driver.find_element_by_partial_link_text("注册A网页").click()

# 暂停 3秒
sleep(3)
# 关闭主窗口
driver.close()

# 暂停 2
sleep(2)
# 关闭驱动对象
# driver.quit()
