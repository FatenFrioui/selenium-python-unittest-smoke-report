import time
import unittest

from selenium import webdriver


class MyWikiTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
    def test_wiki(self):
        driver=self.driver
        driver.get("https://en.wikipedia.org/")
        driver.find_element_by_id("searchInput").send_keys("python")
        time.sleep(2)
        driver.find_element_by_id("searchButton").click()
        time.sleep(2)

    def tearDown(self):
        driver=self.driver
        driver.quit()



if __name__ == '__main__':
    unittest.main()
