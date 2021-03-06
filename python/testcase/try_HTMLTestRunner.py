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
import HTMLTestRunner
import baidumap


class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try:
            driver.find_element_by_id("kw").click()
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys("python")
            driver.find_element_by_id("su").click()
            driver.get_screenshot_as_file("D:\\python\\report\\python.png")
        except Exception as e:
            raise
        else:
            print u"搜索成功"
        finally:
            print u"最后执行"
            pass

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    utest = unittest.TestSuite()
    # utest.addTest(unittest.makeSuite(baidumap.Baidumap))
    utest.addTest(Baidu("test_baidu"))
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    filename = "D:\\python\\report\\" + now + " baidu.html"
    fp = file(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title=u"百度搜索", description=u"搜索python")
    runner.run(utest)
