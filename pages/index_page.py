# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 下午 03:51
# @Author  : Yuanxuan
# @FileName: index_page.py
# @Software: PyCharm
import allure
from selenium.webdriver.common.by import By

from pages import BasePage
from UI import IndexUI


class IndexPage(BasePage):
    """
    主页：
    https://www.qq.com/
    """
    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step("导航栏选择")
    def navigate_main(self, navi):
        """
        主导航栏
        :return:
        """
        #导航栏元素定位
        # navigate_loc = (By.LINK_TEXT, navi)
        self.find_element(IndexUI.navigate_loc(navi)).click()

        # 跳转窗口
        self.switch_windows()
