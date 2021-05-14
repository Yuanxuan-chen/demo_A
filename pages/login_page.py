# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 下午 03:08
# @Author  : Yuanxuan
# @FileName: login_page.py
# @Software: PyCharm
import allure
from selenium.webdriver.common.by import By

from pages import BasePage
from UI import LoginUI


class LoginPage(BasePage):
    """
    用户登录界面
    """
    def __init__(self, driver, url):
        super().__init__(driver, url)
        # self.elements = GetYaml(config.ELEMENT_PATH + '\\' + 'login_page.yaml')

    @allure.step("跳转到登录，进入账号密码登录页面")
    def dig_login(self):
        """
        首页登录，弹出登录框
        :return:
        """
        # 点击首页登录按钮
        # dig_login_button_loc = (By.CLASS_NAME, 'l-login')
        self.find_element(LoginUI.dig_login_button_loc1).click()
        # 切换表单
        # dig_login_button_loc = (By.ID, 'ptlogin_iframe')
        self.switch_frame(LoginUI.dig_login_button_loc2)
        # 切换到账号密码登录方式
        # dig_login_button_loc = (By.LINK_TEXT, '帐号密码登录')
        self.find_element(LoginUI.dig_login_button_loc3).click()

    @allure.step("输入账号")
    def login_username(self, username):
        """
        登录账号
        :param username:
        :return:
        """
        # login_phone_loc = (By.ID, 'u')
        self.send_key(LoginUI.login_phone_loc, username)

    @allure.step("输入密码")
    def login_password(self, pwd):
        """
        登录密码
        :return:pwd
        """
        # login_pwd_loc = (By.ID, 'p')
        self.send_key(LoginUI.login_pwd_loc, pwd)

    @allure.step("点击登录按钮")
    def login_button(self):
        """
        登录按钮
        :return:
        """
        # login_loc = (By.ID, 'login_button')
        self.find_element(LoginUI.login_loc).click()

    @allure.step("校验验证信息是否正确")
    def login_check_info(self):
        """
        获取断言需要的信息
        :return:
        """
        # 提示完文字的loc
        # check_loc = (By.ID, 'err_m')
        text = self.find_element(LoginUI.check_loc)
        return self.get_loc_text(text)
