from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "file:///d:/workspace_test/selenium-python/html/注册A.html"

driver.get(url)

driver.find_element_by_class_name("telA").send_keys("1111111")

sleep(10)

driver.quit()
