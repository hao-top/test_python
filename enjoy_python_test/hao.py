
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://www.baidu.com"+"/")
driver.find_element_by_id("kw").clear()
size=driver.find_element_by_id("kw").size
text=driver.find_element_by_id("cp").text
result=driver.find_element_by_id("kw").is_displayed()
print(size)
print(text)
print(result)
driver.find_element_by_xpath("//*[@id='kw']").send_keys("good")
# driver.find_element_by_id("kw").send_keys("浩")
driver.find_element_by_id("su").click()
driver.close()
