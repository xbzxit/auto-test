# 导包
from selenium import webdriver
from time import sleep
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
    目标： 为什么要切换frame表单
    需求：
        1. 打开注册实例.html
        2. 填写主页面 页面信息
        3. 填写注册A 页面信息
        4. 填写注册B 页面信息
    
"""
"""填写主页面"""
# 用户名
driver.find_element_by_css_selector("#user").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#password").send_keys("admin")
# 电话
driver.find_element_by_css_selector(".tel").send_keys("18611112222")
# 邮件
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

# 切换到注册A 使用name
driver.switch_to.frame("myframe1")
# 使用id
# driver.switch_to.frame("idframe1")

"""填写注册A"""
# 用户名
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#passwordA").send_keys("admin")
# 电话
driver.find_element_by_css_selector(".telA").send_keys("18611112222")
# 邮件
driver.find_element_by_css_selector("#emailA").send_keys("122223@qq.com")

# 切换到默认目录
driver.switch_to.default_content()

# 切换到注册B 使用name
driver.switch_to.frame("myframe2")
# 使用元素切换
# driver.switch_to.frame(driver.find_element_by_css_selector("[name='myframe2']"))

"""填写注册B"""
# 用户名
driver.find_element_by_css_selector("#userB").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#passwordB").send_keys("admin")
# 电话
driver.find_element_by_css_selector(".telB").send_keys("18611112222")
# 邮件
driver.find_element_by_css_selector("#emailB").send_keys("1223223232323233@qq.com")

# 暂停 2
sleep(4)
# 关闭驱动对象
driver.quit()
