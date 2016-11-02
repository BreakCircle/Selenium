# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class Baidumap(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidumap(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"地图").click()
        driver.find_element_by_id("sole-input").clear()
        driver.find_element_by_id("sole-input").send_keys("zhonglou")
        driver.find_element_by_css_selector("li.ui3-suggest-item > a").click()
        driver.find_element_by_id("search-button").click()
        driver.find_element_by_link_text(u"钟楼").click()

if __name__ == "__main__":
    unittest.main()
