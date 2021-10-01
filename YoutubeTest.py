import time
import unittest

from selenium import webdriver


class MyYoutubeTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
    def test_youtube(self):
        driver=self.driver
        driver.get("http://www.youtube.com/")
        driver.find_element_by_name("search_query").send_keys("metalica")
        time.sleep(2)
        driver.find_element_by_id("search-icon-legacy").click()
        time.sleep(3)

    def tearDown(self):
        driver = self.driver
        driver.quit()



if __name__ == '__main__':
    unittest.main()
