# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 下午 04:14
# @Author  : Yuanxuan
# @FileName: news_page.py
# @Software: PyCharm
import allure
from selenium.webdriver.common.by import By

from pages import BasePage
from UI import NewsUI


class NewsPage(BasePage):
    """
    新闻页测试类
    """

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step("进入新闻页面")
    def dig_news(self):
        """
        跳转到news页面
        :return:
        """
        import warnings
        # warnings.warn("该方法不再维护", DeprecationWarning)
        dig_news_loc = (By.LINK_TEXT, '新闻')
        self.find_element(dig_news_loc).click()

        # 跳转窗口
        self.switch_windows()

    @allure.step("随机选择新闻")
    def switch_news(self, index):
        """
        选择新闻
        """
        loc = self.find_element(NewsUI.switch_news_loc(index))
        text = loc.text
        loc.click()
        # self.find_element(switch_news_loc).click()

        # 跳转窗口
        self.switch_windows()

        return text

    @allure.step("浏览新闻，移动到底部")
    def move_news_page(self):
        """
        浏览新闻，移动到底部
        :return:
        """
        js_code = 'window.scrollTo(0, document.body.scrollHeight)'
        self.script(js_code)

    @allure.step("评论新闻")
    def comment_news(self, text):
        """
        评论新闻
        :return:
        """

        # 转入评论输入框的frame
        # frame_loc = (By.ID, 'commentIframe')
        self.switch_frame(NewsUI.frame_loc)

        # 评论框输入数据
        # input_loc = (By.ID, 'J_Textarea')
        self.send_key(NewsUI.input_loc, text)

        # 点击确定按钮
        # 。。。。
