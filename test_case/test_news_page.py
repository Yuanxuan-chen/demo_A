# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 下午 04:38
# @Author  : Yuanxuan
# @FileName: test_news_page.py
# @Software: PyCharm
from utils import MyPyTest
from pages import NewsPage
import config

import pytest


class TestNewsPage(MyPyTest):
    """
    新闻页测试类
    """
    def setup(self):
        self.np = NewsPage(self.driver, config.URL)
        self.np.open()

    def test_read_news(self):
        self.np.dig_news()
        self.np.switch_news()
        self.np.move_news_page()
        self.np.comment_news()

if __name__ == '__main__':
    pytest.main()