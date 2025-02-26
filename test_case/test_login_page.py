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


@allure.epic('登录页')
@allure.feature('腾讯网登录页功能测试')
class TestLoginPage(MyPyTest):
    """
    腾讯登录测试类
    """
    test_case_data = GetYaml(config.TEST_DATA_PATH + '\\' + 'login_page_data.yaml')

    def setup(self):
        with allure.step("进入{}".format(config.URL)):
            self.lp = LoginPage(self.driver, config.URL)
            self.lp.open()

    def teardown(self):
        """
        后置动作
        :return:
        """
        self.lp.sleeping()

    @allure.story("账号密码登录")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("data", test_case_data.all_data())
    def test_login_window(self, data):
        """
        测试腾讯网的账号密码的跳转
        """
        # 跳转到登录，进入账号密码登录页面
        self.lp.dig_login_page()

        with allure.step("输入账号和密码，点击登录"):
            self.lp.login_username(data['data']['id'])
            self.lp.login_password(data['data']['pwd'])
        #     self.lp.login_button()
        #
        # with allure.step("对比提示信息"):
        #     assert self.lp.login_check_info() == data['check']


if __name__ == '__main__':
    pytest.main()
