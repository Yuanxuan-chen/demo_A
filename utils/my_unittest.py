# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 下午 02:30
# @Author  : Yuanxuan
# @FileName: my_unittest.py
# @Software: PyCharm
import unittest
from selenium import webdriver
from time import sleep


class MyUnitTest(unittest.TestCase):
    """
    自定义单元测试父类
    """

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        cls.driver.quit()
