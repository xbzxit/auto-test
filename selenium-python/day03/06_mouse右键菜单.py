# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
# driver = webdriver.Ie()
# 谷歌浏览器不支持 --> 粘贴快捷键
# driver = webdriver.Chrome()
# 打开url
url = "file:///D:/workspace_test/selenium-python/html/注册A.html"

driver.get(url)

# 实例化并获取 ActionChains类
action = ActionChains(driver)
# 定位用户名 在用户名上 右击鼠标  预期：粘贴
# 获取用户名元素  admin123
username = driver.find_element_by_css_selector("#userA")
# 点击右键
action.context_click(username).perform()
# 发送p
username.send_keys("p")

# 暂停 2

# sleep(2)
# 关闭驱动对象
driver.quit()
