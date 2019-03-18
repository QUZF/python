#!/usr/bin/python
# Author: QUZF
# Datetime: 2019/1/25 15:47

from selenium import webdriver
import unittest
import time


class Blog(unittest.TestCase):
    """登录博客"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://passport.cnblogs.com/user/signin")
        self.driver.implicitly_wait(5)

    def login(self, username, psw):
        """写了一个登录的方法，帐号和密码参数化"""
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)

    def is_login_sucess(self):
        """判断是否获取到登录帐号名称"""
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print(text)
            return True
        except:
            return False

    def test_01(self):
        """登录用例1"""
        self.login("JenniferQZF", "4731210377qu!")        # 调用登录方法
        time.sleep(2)
        # 判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)

    def test_02(self):
        """登录用例2：测试时用不同的账号密码登录"""
        self.login("JenniferQZF", "4731210377qu!")        # 调用登录方法
        time.sleep(2)
        # 判断结果
        text = self.driver.find_element_by_id("lnk_current_user").text
        print(text)
        self.assertEqual(text, "风中花")

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()