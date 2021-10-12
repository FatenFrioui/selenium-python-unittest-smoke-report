import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

class MyScroll(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
    def test_dragdrop(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://www.uitestingplayground.com/")
        driver.find_element_by_xpath("//a[contains(text(),'Scrollbars')]").click()
        blue_button = driver.find_element_by_id("hidingButton")
        time.sleep(3)
        actions = ActionChains(driver)
        actions.move_to_element(blue_button).perform()
        # methode2
        # driver.execute_script("arguments[0].scrollIntoView();", blue_button)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


