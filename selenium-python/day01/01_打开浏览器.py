from time import sleep

from selenium import webdriver

# driver = webdriver.Firefox()
driver = webdriver.Firefox()
# river = webdriver.Edge()
# driver = webdriver.Safari()

driver.get('https://www.baidu.com')

sleep(10)
driver.quit()
