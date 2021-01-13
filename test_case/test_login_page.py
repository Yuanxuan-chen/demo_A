# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 上午 09:47
# @Author  : Yuanxuan
# @FileName: test_login_page.py
# @Software: PyCharm

import pytest

import config
from pages import LoginPage
from utils import GetYaml
from utils import MyPyTest

test_case_data = GetYaml(config.TEST_DATA_PATH + '\\' + 'login_data.yaml')


class TestLoginPage(MyPyTest):
    """
    腾讯登录测试类
    """
    def setup(self):
        self.lp = LoginPage(self.driver, config.URL)
        self.lp.open()

    @pytest.mark.parametrize("data", test_case_data.all_data())
    def test_login_window(self, data):
        """
        测试腾讯网的账号密码的跳转
        :return:
        """
        self.lp.dig_login()
        self.lp.login_username(data['data']['id'])
        self.lp.login_password(data['data']['pwd'])
        # 注释掉，防止被腾讯官方认为是攻击行为
        # self.lp.login_button()
        # assert self.lp.login_check_info() == data['check']


if __name__ == '__main__':
    pytest.main()
