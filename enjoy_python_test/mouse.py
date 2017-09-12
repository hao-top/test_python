# Author:Mr浩

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

# 定位到要悬停的元素
above=driver.find_element_by_link_text("设置")
# 对定位的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
time.sleep(2)
driver.find_element_by_id("kw").send_keys("seleniums")
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
time.sleep(2)
driver.find_element_by_id("kw").send_keys("jiaocheng")
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
time.sleep(2)
test=driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")