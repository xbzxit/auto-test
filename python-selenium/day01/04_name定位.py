from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
url = "file:///d:/workspace_python/python-selenium/html/注册A.html"
driver.get(url)

driver.find_element_by_name("userA").send_keys("admin")

driver.find_element_by_name("passwordA").send_keys("123456")

sleep(10)
driver.quit()
