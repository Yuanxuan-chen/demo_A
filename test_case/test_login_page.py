# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 上午 09:47
# @Author  : Yuanxuan
# @FileName: test_login_page.py
# @Software: PyCharm

import pytest
import allure

import config
from pages import LoginPage
from utils import GetYaml
from utils import MyPyTest

test_case_data = GetYaml(config.TEST_DATA_PATH + '\\' + 'login_data.yaml')


@allure.feature('腾讯网登录页功能测试')
class TestLoginPage(MyPyTest):
    """
    腾讯登录测试类
    """
    def setup(self):
        self.lp = LoginPage(self.driver, config.URL)
        self.lp.open()

    @allure.story("账号密码登录")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("data", test_case_data.all_data(), ids=test_case_data.get_all_detail())
    def test_login_window(self, data):
        """
        测试腾讯网的账号密码的跳转
        """
        with allure.step("1.跳转到测试登录页面"):
            self.lp.dig_login()

        with allure.step("2.输入账号和密码，点击登录"):
            self.lp.login_username(data['data']['id'])
            self.lp.login_password(data['data']['pwd'])
            # self.lp.login_button()

        # with allure.step("3.对比提示信息"):
        #     # 注释掉，防止被腾讯官方认为是攻击行为
        #     assert self.lp.login_check_info() == data['check']


if __name__ == '__main__':
    pytest.main()
