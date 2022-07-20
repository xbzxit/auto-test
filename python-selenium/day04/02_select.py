# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器驱动对象
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)
# 打开url
url = "file:///d:/workspace_python/python-selenium/html/注册A.html"
driver.get(url)


"""
    目标： 使用Select类实现操作option选项
    
    需求：
        暂停2秒
        1. 定位 A上海
        2. 暂停2秒
        3. 定位 A广州
        
    步骤：
        1. 导包 Select类
        2. 获取Select对象
            匿名：Select(element).select_by_index() # 通过下标
            实名：select = Select(element)
                调用：select.select_by_index()
    注意：
        1. Select类是通过select标签来控制其下的option元素
        2. element:只能是select标签
"""
"""方式2：使用Select完成需求"""
el = driver.find_element_by_css_selector("#selectA")
sleep(2)
"""通过 下标形式访问"""
# 切换 上海
# Select(el).select_by_index(1)
# sleep(2)
# Select(el).select_by_index(2)

"""通过 value值形式访问"""
# 获取Select引用对象
# sel = Select(el)
# # 切换 上海
# sel.select_by_value("sh")
# sleep(2)
# # 切换 广州
# sel.select_by_value("gz")

"""通过 显示文本切换"""
sleep(2)
# 切换 上海
Select(el).select_by_visible_text("A上海")
sleep(2)
# 切换广州
Select(el).select_by_visible_text("A广州")

# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
