# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox(executable_path="C:\webdriver\geckodriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.find_element_by_name("q").click()
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("zara tunisie")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//div[@id='theme-modal-container']/div/div").click()
        driver.find_element_by_css_selector("path").click()
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
        driver.find_element_by_xpath("//aside[@id='sidebar']/div/nav/div/ul/li/a/span").click()
        driver.find_element_by_xpath("//aside[@id='sidebar']/div/nav/div/ul/li/ul/li[3]/ul/li[2]/a/span").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'https://static.zara.net/photos///2021/I/T/1/p/0267/420/800/2/w/600/0267420800_1_1_1.jpg?ts=1632730334059')]").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'https://static.zara.net/photos///2021/I/T/1/p/0909/670/613/2/w/600/0909670613_1_1_1.jpg?ts=1632477721462')]").click()
        driver.find_element_by_id(
            "product-detail-size-selector-product-detail-product-size-selector-130971697-toggle-button").click()
        driver.find_element_by_id(
            "product-detail-size-selector-product-detail-product-size-selector-135028209-toggle-button").click()
        driver.find_element_by_xpath(u"//img[@alt='ROBE À VOLANTS LIMITED EDITION']").click()
        driver.find_element_by_xpath(u"//img[@alt='ROBE À VOLANTS LIMITED EDITION']").click()
        driver.find_element_by_xpath(
            "//li[@id='product-detail-size-selector-product-detail-product-size-selector-139866654-item-3']/div/div/span").click()
        driver.find_element_by_xpath(
            "//li[@id='product-detail-size-selector-product-detail-product-size-selector-139866654-item-2']/div/div/span").click()
        driver.find_element_by_xpath("//main[@id='main']/article/div[2]/div[2]/div/div[5]/button/div/span").click()
        driver.find_element_by_xpath(
            "//div[@id='theme-modal-container']/div/div/div/div/div[3]/div[2]/button/div/span").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
