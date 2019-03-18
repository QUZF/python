#!/usr/bin/python
# Author: QUZF
# Datetime: 2019/1/25 15:47

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class BlogHome(unittest.TestCase):
    """博客首页"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://www.cnblogs.com/JenniferQZF/")
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

    def test_01(self):
        """验证元素存在：博客园"""
        locator = ("id", "blog_nav_sitehome")
        text = "博客园"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

    def test_02(self):
        """验证元素存在：首页"""
        locator = ("id", "blog_nav_myhome")
        text = "首页"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
