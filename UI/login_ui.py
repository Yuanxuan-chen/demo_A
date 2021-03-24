# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 下午 03:59
# @Author  : Yuanxuan
# @FileName: login_ui.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


class LoginUI:
    """
    登录页元素
    """
    # 点击首页登录按钮
    dig_login_button_loc1 = (By.CLASS_NAME, 'l-login')
    # 切换表单
    dig_login_button_loc2 = (By.ID, 'ptlogin_iframe')
    # 切换到账号密码登录方式
    dig_login_button_loc3 = (By.LINK_TEXT, '帐号密码登录')

    # 输入账号
    login_phone_loc = (By.ID, 'u')

    # 输入密码
    login_pwd_loc = (By.ID, 'p')

    # 登录按钮
    login_loc = (By.ID, 'login_button')

    # 提示完文字的loc
    check_loc = (By.ID, 'err_m')
