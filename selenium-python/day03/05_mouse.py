from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
url = "file:///d:/workspace_test/selenium-python/html/注册A.html"
driver.get(url)
action = ActionChains(driver)
username = driver.find_element_by_css_selector("#userA")
ActionChains(driver).context_click(username).perform()
username.send_keys(Keys.ALT)
sleep(2)

pwd = driver.find_element_by_css_selector("#passwordA")
pwd.send_keys("admin")
ActionChains(driver).double_click(pwd).perform()
sleep(2)

ActionChains(driver).move_to_element(driver.find_element_by_css_selector("button")).perform()

sleep(2)
driver.quit()
