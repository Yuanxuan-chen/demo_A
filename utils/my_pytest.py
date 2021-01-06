# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 下午 02:30
# @Author  : Yuanxuan
# @FileName: my_pytest.py
# @Software: PyCharm
from selenium import webdriver
from time import sleep


class MyPyTest:
    """
    自定义单元测试父类
    """
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        sleep(3)
        cls.driver.quit()
