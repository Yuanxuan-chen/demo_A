# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 上午 09:47
# @Author  : Yuanxuan
# @FileName: test_login_page.py
# @Software: PyCharm

import pytest
from utils import MyPyTest

import config
from pages import LoginPage
from utils import GetYaml

test_case_data = GetYaml(config.TEST_DATA_PATH + '\\' + 'login_data.yaml')


class TestLoginPage(MyPyTest):
    """
    抽屉登录测试类
    """
    def setup(self):
        self.lp = LoginPage(self.driver, config.URL_tencent)
        self.lp.open()

    @pytest.mark.parametrize("data", test_case_data.all_data())
    def test_login_window(self, data):
        """
        测试腾讯网的账号密码的跳转
        :return:
        """
        self.lp.dig_login()
        self.lp.login_phone(data['data']['id'])
        self.lp.login_password(data['data']['pwd'])
        self.lp.login_button()


if __name__ == '__main__':
    pytest.main()
