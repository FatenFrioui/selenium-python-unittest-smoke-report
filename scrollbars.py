import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("http://www.uitestingplayground.com/")
driver.find_element_by_xpath("//a[contains(text(),'Scrollbars')]").click()
scroll=driver.find_element_by_xpath("//body/section[1]/div[1]/div[1]")

x=scroll(Keys.RIGHT)
y=scroll(Keys.DOWN)
time.sleep(3)
driver.find_element_by_xpath("//button[@id='hidingButton']").click()