# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)
# 打开url
# 设置cookie
url = "http://www.baidu.com"
driver.get(url)
driver.add_cookie({"name": "BDUSS", "value":"05VkJaelAtblhuV2hIQncxS0p2N1l4MVNrdmctZGxWREUwNWdYTjRwV1N3Y1pjRVFBQUFBJCQAAAAAAAAAAAEAAAD82ggPMTUwNjkxNTU1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJI0n1ySNJ9ca0"})

# 获取所有的cookies信息
# cookies = driver.get_cookies()
# print("cookies内容为：", cookies)
# for co in cookies:
#     print(co['name'])

# cookie = driver.get_cookie("BDUSS")
# print("cookie:", cookie)

# 暂停2秒
# sleep(2)
# 刷新 必须进行刷新才能看到效果
# driver.refresh()

"""
    目标： cookie操作
    案例：
        使用cookie绕过百度登录
    步骤：
        1. 手动登录百度网站
        2. 手动获取登录后的cookies 'BDUSS'
        3. 使用selenium内的add_cookie(name='BDUSS', value='xxxx')
"""

# 暂停 2
sleep(5)
# 关闭驱动对象
driver.quit()
