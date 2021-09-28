import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")



driver.get("https://www.google.com/")

input_box=driver.find_element_by_name("q")
# input_box.send_keys("selenium")
# driver.find_element_by_name("btnK").submit()
input_box.send_keys("selenium",Keys.ENTER)


driver.quit()