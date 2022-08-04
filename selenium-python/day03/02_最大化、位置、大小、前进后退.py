# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开url
url = "file:///d:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)

# 将浏览器 最大化
driver.maximize_window()

# 暂停2秒
sleep(2)
# 设置固定大小 300,200
driver.set_window_size(300, 200)

# 暂停2秒
sleep(2)
# 移动浏览器窗口位置 x:320，y:150
driver.set_window_position(320, 150)

# 暂停2秒
sleep(2)
# 最大化
driver.maximize_window()

# 点击 访问新浪网站  注意：要演示后退功能，必须先执行打开新的网站
driver.find_element_by_partial_link_text("访问").click()

# 暂停2秒
sleep(2)
# 执行后退 ---> 注册A.html
driver.back()
# 暂停2秒
sleep(2)
# 执行前进 -->新浪 注意：前进必须放到后退操后执行
driver.forward()


# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
