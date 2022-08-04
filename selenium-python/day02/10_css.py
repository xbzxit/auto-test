"""
    需求：
        1. 使用css id选择器 定位用户名 输入admin
        2. 使用css 属性选择 定位密码框 输入123456
        3. 使用 css class 选择器 定位电话号码： 18611112222
        4. 使用css 元素选择器 定位span标签获取文本值
        5. 使用层级选择器 定位email 输入 123@qq.com

    方法：
        driver.find_element_by_css_selector()
        获取文本的方法 元素.text
"""

from time import sleep

# 导包
from selenium import webdriver

# 获取 浏览器驱动对象
driver = webdriver.Firefox()

# 打开 注册A.html
url = "d:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)

# 1. 使用css id选择器 定位用户名 输入admin
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 2. 使用css 属性选择 定位密码框 输入123456
driver.find_element_by_css_selector("[name='passwordA']").send_keys("123456")
# 3. 使用 css class 选择器 定位电话号码： 18611112222
driver.find_element_by_css_selector(".telA").send_keys("18611112222")
# 4. 使用css 元素选择器 定位span标签获取文本值
span = driver.find_element_by_css_selector("span").text
print("获取的span标签文本值：", span)

# 5. 使用层级选择器 定位email 输入 123@qq.com
driver.find_element_by_css_selector("p>input[placeholder='电子邮箱A']").send_keys("123@qq.com")

# 暂停 3秒
sleep(3)
# 退出浏览器驱动
driver.quit()


##