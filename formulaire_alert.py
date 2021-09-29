import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
driver.maximize_window()
time.sleep(3)
driver.refresh()
driver.find_element_by_xpath("//button[contains(text(),'Button')]").submit()


a=driver.switch_to.alert

time.sleep(3)
#accept alert
a=Alert(driver)
a.accept()
# a.dismiss()
# driver.fullscreen_window("alert")