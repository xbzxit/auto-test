# 导包
from time import sleep

from selenium import webdriver

# 获取 浏览器对象
# 如果是Firefox 需要主要驱动与浏览器版本的问题， 谷歌浏览器下没有问题
driver = webdriver.Firefox()

# 打开url
# 注意：\反斜杠在python是转义字符  r:修饰的字符串，如果字符串中有转义字符，不进行转义使用
url = r"D:\workspace_python\python-selenium\html\注册A.html"

# 使用双反斜杠 进行转义操作
# url = "D:\\workspace_python\\python-selenium\\html\\注册A.html"

# 使用本地浏览模式 前缀必须添加 file:///
# url = "file:///D:/workspace_python/python-selenium/html/注册A.html"

# 复制浏览器地址
# url = "D:/workspace_python/python-selenium/html/注册A.html"
driver.get(url)

# 查找 用户名元素
username = driver.find_element_by_id("userA")

# 查找 密码元素
password = driver.find_element_by_id("passwordA")

# 用户名输入 admin  send_keys("内容")d
username.send_keys("admin")

# 密码 输入 123456
password.send_keys("123456")

# 暂停3秒
sleep(13)

# 退出浏览器驱动
driver.quit()
