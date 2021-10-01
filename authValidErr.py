import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("http://www.uitestingplayground.com/")

driver.find_element_by_xpath("//a[contains(text(),'Sample App')]").click()


username=driver.find_element_by_name("UserName")
username.send_keys("Faten")
password=driver.find_element_by_name("Password")
password.send_keys("xyz")
time.sleep(2)
driver.find_element_by_id("login").click()


msg = driver.find_element_by_id('loginstatus').text
assert msg in 'Invalid username/password'



print('hi')