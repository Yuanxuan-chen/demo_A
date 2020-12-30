# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 上午 09:47
# @Author  : Yuanxuan
# @FileName: test_login_page.py
# @Software: PyCharm

import ddt
import unittest
from utils import MyUnitTest
from time import sleep

import config
from pages import LoginPage
from utils import GetYaml

test_case_data = GetYaml(config.TEST_DATA_PATH + '\\' + 'login_data.yaml')


@ddt.ddt
class TestLoginPage(MyUnitTest):
    """
    抽屉登录测试类
    """

    def setUp(self) -> None:
        self.lp = LoginPage(self.driver, config.URL)
        self.lp.open()

    @ddt.data(*test_case_data.data)
    def test_login(self, test_data):
        """生成测试报告测试第一册"""
        self.lp.dig_login()
        self.lp.login_phone(test_data['data']['phone'])
        self.lp.login_password(test_data['data']['password'])
        sleep(2)


if __name__ == '__main__':
    unittest.main()
