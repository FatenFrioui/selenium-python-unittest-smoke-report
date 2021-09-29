import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\webdriver\chromedriver.exe")


for i in range(0,5):
    driver.get("https://www.nxtgenaiacademy.com/demo-site/")
    driver.maximize_window()
    inputs=driver.find_elements_by_xpath("//input[@type='text']")
    for input in inputs:
        input.send_keys("test")

    driver.find_elements_by_xpath("//input[@value='Female']")[0].click()

    driver.find_element_by_id('vfb-14').send_keys("faten.frioui.1@gmail.com")

    date=driver.find_element_by_id('vfb-18').click()

    pays=Select(driver.find_element_by_id('vfb-13-country'))
    pays.select_by_visible_text("Tunisia")

    hour=Select(driver.find_element_by_id('vfb-16-hour'))
    hour.select_by_visible_text("02")

    min=Select(driver.find_element_by_id('vfb-16-min'))
    min.select_by_visible_text("30")

    ampm=Select(driver.find_element_by_id('vfb-16-ampm'))
    ampm.select_by_visible_text("PM")

    elements=driver.find_elements_by_xpath("//div[@id='ui-datepicker-div']")
    for dates in elements:
        dates.click()

    checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
    for checkbox in checkboxes:
        checkbox.click()

    driver.find_element_by_xpath("//textarea").send_keys("hello honey")

    time.sleep(2)
    driver.find_element_by_name("vfb-13[zip]").clear()
    time.sleep(2)
    driver.find_element_by_name("vfb-13[zip]").send_keys("4011")

    time.sleep(2)
    driver.find_element_by_id("vfb-19").clear()
    time.sleep(2)
    driver.find_element_by_id("vfb-19").send_keys("97958198")

    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='vfb-3']").clear()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='vfb-3']").send_keys("83")
    time.sleep(2)
    driver.save_screenshot("C:\captures\cap_form_v2.png")
    driver.find_element_by_xpath("//input[@id='vfb-4']").click()

