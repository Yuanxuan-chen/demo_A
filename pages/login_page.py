# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 下午 03:08
# @Author  : Yuanxuan
# @FileName: login_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


from pages import BasePage
from utils import GetYaml
import config


class LoginPage(BasePage):
    """
    用户登录界面
    """
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.elements = GetYaml(config.ELEMENT_PATH + '\\' + 'login_page.yaml')

    def dig_login(self):
        """
        首页登录，弹出登录框
        :return:
        """
        # 点击首页登录按钮
        dig_login_button_loc = (By.CLASS_NAME, self.elements.get_element_info(0))
        self.find_element(dig_login_button_loc).click()
        # 切换表单
        dig_login_button_loc = (By.ID, self.elements.get_element_info(1))
        self.switch_frame(self.find_element(dig_login_button_loc))
        # 切换到账号密码登录方式
        dig_login_button_loc = (By.LINK_TEXT, self.elements.get_element_info(2))
        self.find_element(dig_login_button_loc).click()

    def login_username(self, username):
        """
        登录账号
        :param username:
        :return:
        """
        login_phone_loc = (By.ID, self.elements.get_element_info(3))
        self.send_key(login_phone_loc, username)

    def login_password(self, pwd):
        """
        登录密码
        :return:pwd
        """
        login_pwd_loc = (By.ID, self.elements.get_element_info(4))
        self.send_key(login_pwd_loc, pwd)

    def login_button(self):
        """
        登录按钮
        :return:
        """
        login_loc = (By.ID, self.elements.get_element_info(5))
        self.find_element(login_loc).click()

    def login_check_info(self):
        """
        获取断言需要的信息
        :return:
        """
        # 提示完文字的loc
        check_loc = self.find_element((By.ID, self.elements.get_element_info(6)))
        return self.get_loc_text(check_loc)
