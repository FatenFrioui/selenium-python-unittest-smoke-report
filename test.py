from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")


# driver=webdriver.Firefox(executable_path="C:\webdriver\geckodriver.exe")
# driver=webdriver.Ie("C:\webdriver\IEDriverServer.exe")
# driver=webdriver.Opera(executable_path="C:\webdriver\operadriver.exe")
print('le webdriver est implementé')



driver.get("https://www.google.com/")
print('le site web est lancé')

# input_box=driver.find_element_by_id("input").click()
# input_box.send_keys("selenium",Keys.ARROW_DOWN)
# button=driver.find_element_by_id("input").click()



driver.quit()
print('on a fermé la dernière fenetre')

# driver.title
# driver.forward()
# driver.back()
# driver.refresh()
# driver.close()
# driver.quit()