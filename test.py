from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")


# driver=webdriver.Firefox(executable_path="C:\webdriver\geckodriver.exe")
# driver=webdriver.Ie("C:\webdriver\IEDriverServer.exe")
# driver=webdriver.Opera(executable_path="C:\webdriver\operadriver.exe")
print('le webdriver est lancé')



driver.get("https://www.google.com/")
print('le site web est lancé')


driver.quit()
print('on a quitté la dernière fenetre')