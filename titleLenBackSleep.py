import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("http://www.uitestingplayground.com/")
title=driver.title
print('le titre est ',title)
print('la longueur du titre est ',len(title))

driver.back()
driver.forward()
time.sleep(3)
driver.refresh()
driver.quit()


