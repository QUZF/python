#!/usr/bin/python
# Author: QUZF
# Datetime: 2019/1/25 15:48

import unittest


class MyTest01(unittest.TestCase):

    def setUp(self):                    # 此类中，每个方法用例执行前先执行一次setUp
        print('setUp')

    def test_case01(self):            # 根据用例的名称来顺序执行的。
        print('test_case01')

    def test_case03(self):             # 根据用例的名称来顺序执行的。
        print('test_case03')

    def test_case02(self):              # 根据用例的名称来顺序执行的。
        print('test_case02')

    def tearDown(self):                  # 此类中，每个方法用例执行完均执行一次tearDown
        print('tearDown')


class MyTest02(unittest.TestCase):

    def test_case04(self):             # 这个类没有前置后置方法，按用例名称顺序正常执行即可；
        print('test_case04')


if __name__ == '__main__':
    unittest.main()
