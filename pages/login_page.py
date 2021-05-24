# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 下午 03:08
# @Author  : Yuanxuan
# @FileName: login_page.py
# @Software: PyCharm
import allure

from pages import BasePage
from UI import LoginUI


class LoginPage(BasePage):
    """
    用户登录界面
    """
    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step("跳转到登录，进入账号密码登录页面")
    def dig_login_page(self):
        """
        首页登录，弹出登录框
        :return:
        """
        # 点击首页登录按钮
        self.find_element(LoginUI.home_page_login_button_loc).click()
        # 切换表单
        self.switch_frame(LoginUI.switch_frame_loc)
        # 切换到账号密码登录方式
        self.find_element(LoginUI.switch_user_password_login_loc).click()

    @allure.step("输入账号")
    def login_username(self, username):
        """
        账号输入框
        :param username:
        :return:
        """
        self.send_key(LoginUI.login_phone_loc, username)

    @allure.step("输入密码")
    def login_password(self, pwd):
        """
        密码输入框
        :return:pwd
        """
        self.send_key(LoginUI.login_pwd_loc, pwd)

    @allure.step("点击登录按钮")
    def login_button(self):
        """
        登录按钮
        :return:
        """
        self.find_element(LoginUI.login_button_loc).click()

    @allure.step("校验验证信息是否正确")
    def login_check_info(self):
        """
        获取断言需要的信息
        :return:
        """
        # 提示完文字的loc
        text = self.find_element(LoginUI.check_loc)
        return self.get_loc_text(text)
