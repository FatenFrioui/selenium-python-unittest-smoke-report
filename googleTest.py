import time
import unittest

from selenium import webdriver


class MyGoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
    def test_google(self):
        driver=self.driver
        driver.get("http://www.google.com/")
        driver.find_element_by_name("q").send_keys("python")
        time.sleep(2)


    def tearDown(self):
        driver = self.driver
        driver.quit()



if __name__ == '__main__':
    unittest.main()
