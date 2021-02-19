# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 下午 02:30
# @Author  : Yuanxuan
# @FileName: my_pytest.py
# @Software: PyCharm
from selenium import webdriver
import allure
import config

options = webdriver.ChromeOptions()
# 添加参数进行去除浏览器检测框: Chrome正在受到自动测试软件的控制
options.add_experimental_option("excludeSwitches", ['enable-automation'])


class MyPyTest:
    """
    自定义单元测试父类
    """
    driver = None

    @classmethod
    def setup_class(cls):
        with allure.step("打开Chrome浏览器"):
            cls.driver = webdriver.Chrome(chrome_options=options)
            cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        config.sleeping()
        with allure.step("关闭浏览器"):
            cls.driver.quit()
