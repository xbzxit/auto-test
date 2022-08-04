# 导包

from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
# 打开url
url = "file:///d:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)

# 实例化并获取 ActionChains类
action = ActionChains(driver)
# 定位用户名 在用户名上 右击鼠标  预期：粘贴
# 获取用户名元素
username = driver.find_element_by_css_selector("#userA")
# 调用右击方法
ActionChains(driver).context_click(username).perform()
username.send_keys(Keys.ALT)
sleep(2)

# 发送用户名 admin 并进行双击  预期：选中admin
pwd = driver.find_element_by_css_selector("#passwordA")
pwd.send_keys("admin")
ActionChains(driver).double_click(pwd).perform()
sleep(2)
# 移动到注册按钮上  预期：按钮变色 出现 加入会员A
ActionChains(driver).move_to_element(driver.find_element_by_css_selector("button")).perform()


# 暂停 2
# sleep(2)
# 关闭驱动对象
driver.quit()
