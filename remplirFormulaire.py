import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

driver.get("https://www.nxtgenaiacademy.com/demo-site/")

driver.find_element_by_xpath("//input[@id='vfb-5']").send_keys("Faten")
time.sleep(2)

driver.find_element_by_xpath("//input[@id='vfb-7']").send_keys("Frioui")
time.sleep(2)

driver.find_elements_by_xpath("//input[@value='Female']")[0].click()
time.sleep(2)

driver.find_element_by_xpath("//input[@id='vfb-13-address']").send_keys("H sousse")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='vfb-13-address-2']").send_keys("menchiya")
time.sleep(2)
driver.find_element_by_name("vfb-13[city]").send_keys("Hammam Sousse")
time.sleep(2)

driver.find_element_by_id("vfb-13-state").send_keys("Sousse")
time.sleep(2)

driver.find_element_by_name("vfb-13[zip]").send_keys("4011")
time.sleep(2)

pays=Select(driver.find_element_by_id('vfb-13-country'))
pays.select_by_visible_text("Tunisia")
time.sleep(2)

hour=Select(driver.find_element_by_id('vfb-16-hour'))
hour.select_by_visible_text("02")
time.sleep(2)

min=Select(driver.find_element_by_id('vfb-16-min'))
min.select_by_visible_text("30")
time.sleep(2)

ampm=Select(driver.find_element_by_id('vfb-16-ampm'))
ampm.select_by_visible_text("PM")
time.sleep(2)

driver.find_element_by_id('vfb-14').send_keys("faten.frioui.1@gmail.com")
time.sleep(2)


date=driver.find_element_by_id('vfb-18').click()
elements=driver.find_elements_by_xpath("//div[@id='ui-datepicker-div']")
for dates in elements:
    dates.click()
time.sleep(2)
driver.find_element_by_id("vfb-19").send_keys("97958198")
time.sleep(2)


driver.find_element_by_xpath("//input[@id='vfb-20-0']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='vfb-20-4']").click()
time.sleep(2)


driver.find_element_by_xpath("//textarea[@id='vfb-23']").send_keys("Bonjouuuur c moi fattouna etta7founa")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='vfb-3']").send_keys("83")
time.sleep(2)

driver.save_screenshot("C:\captures\cap_formulaire.png")
driver.find_element_by_xpath("//input[@id='vfb-4']").click()
