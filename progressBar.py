import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("http://www.uitestingplayground.com/progressbar")
driver.find_element_by_id("startButton").click()
barprog = driver.find_element_by_id("progressBar").text
valeur=0
while True:

    valeur=driver.find_element_by_xpath("//div[@id='progressBar']")
    if valeur=="75%":
        driver.find_element_by_xpath("//button[@id='startButton']").click()
        break


