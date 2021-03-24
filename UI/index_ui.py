# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 下午 03:55
# @Author  : Yuanxuan
# @FileName: index_ui.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


class IndexUI:
    """
    首页元素
    """

    # 导航栏元素定位
    @staticmethod
    def navigate_loc(navi):
        return By.LINK_TEXT, navi
