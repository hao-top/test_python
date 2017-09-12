# Author:Mr浩

from selenium import webdriver
import time
driver=webdriver.Ie()
first_url="http://www.baidu.com"
print("first_url %s" %(first_url))
driver.get(first_url)
time.sleep(1)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("tian")
driver.find_element_by_id("su").click()
time.sleep(1)
driver.quit()


