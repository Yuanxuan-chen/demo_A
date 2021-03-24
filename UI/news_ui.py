# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 下午 04:00
# @Author  : Yuanxuan
# @FileName: news_ui.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


class NewsUI:
    """
    新闻详情页元素
    """

    # 选择新闻
    @staticmethod
    def switch_news_loc(index):
        return By.XPATH, '/html/body/div/div[4]/div[2]/div/div/ul[1]/li[' + str(index) + ']/div/h3/a'

    # 转入评论输入框的frame
    frame_loc = (By.ID, 'commentIframe')

    # 评论框输入数据
    input_loc = (By.ID, 'J_Textarea')
