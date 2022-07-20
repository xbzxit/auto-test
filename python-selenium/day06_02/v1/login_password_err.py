from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://demo.ruoyi.vip/login")

username = driver.find_element_by_name("username")
username.clear()
username.send_keys("admin")
password = driver.find_element_by_name("password")
password.clear()
password.send_keys("admin123")
driver.find_element_by_name("validateCode").send_keys("3")
driver.find_element_by_css_selector("#btnSubmit").click()
sleep(10)
driver.quit()
