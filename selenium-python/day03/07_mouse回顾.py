# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 打开url
url = "file:///d:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)
"""
    目标：基于selenium完成 鼠标事件操作
    说明：
        1. selenium框架中将鼠标操作的一系列方法封装在 ActionChains类中
    方法：
        1. 双击 double_click()
        2. 右击 context_click()
        3. 悬停 move_to_element()
        4. 拖拽 drag_and_drop()
        5. 执行 perform()
    操作：
        1. 导入 ActionChains类  位置：from selenium.webdriver.common.action_chains import ActionChains
        2. 实例化
            匿名：ActionChains(driver).double_click(element).perform()
            匿名：ActionChains(driver).context_click(element).perform()
            实名：action = ActionChains(driver)
        3. 调用响应的方法：
            如：
                1. ActionChains(driver).double_click(element).perform()
                2. action.double_click(element).perform()
    注意：
        鼠标操作方法，必须调用perform()才能执行
"""

# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()
