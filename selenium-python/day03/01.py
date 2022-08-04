# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url
url = "file:///d:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)
# 输入 admin
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 输入 密码 123456
driver.find_element_by_css_selector("#passwordA").send_keys("123456")

# 输入 电话 18611112222
driver.find_element_by_css_selector(".telA").send_keys("18611112222")

# 输入 邮箱 123@qq.com
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")

# 暂停2秒
sleep(2)

# 修改电话号码 18622223333  -->清空操作
# driver.find_element_by_css_selector(".telA").clear()
driver.find_element_by_css_selector(".telA").send_keys("18622223333")
# 暂停2秒
sleep(2)
# 点击注册按钮
driver.find_element_by_css_selector("button").click()
# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()