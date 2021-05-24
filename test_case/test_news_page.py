# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 下午 04:38
# @Author  : Yuanxuan
# @FileName: test_news_page.py
# @Software: PyCharm
from utils import MyPyTest
from pages import NewsPage
import config
from utils import GetYaml

import pytest
import allure
import logging

test_case_data = GetYaml(config.TEST_DATA_PATH + '\\' + 'news_page_data.yaml')


@allure.epic("新闻页")
@allure.feature("浏览新闻")
class TestNewsPage(MyPyTest):
    """
    新闻页测试类
    """

    def setup(self):
        with allure.step("进入{}".format(config.URL)):
            self.np = NewsPage(self.driver, config.URL)
            self.np.open()

    def teardown(self):
        """
        后置动作
        :return:
        """
        self.np.sleeping()

    @pytest.mark.parametrize("data", test_case_data.all_data())
    def test_read_news(self, data):
        """
        浏览新闻,对新闻进行评论
        :return:
        """
        # 进入新闻页面
        self.np.dig_news()
        # 随机选择新闻
        text = self.np.switch_news(data['data']['index'])
        # 浏览新闻，移动到底部
        self.np.move_news_page()
        # 评论新闻
        self.np.comment_news(data['data']['comment'])
        # assert self.np.get_title()[:-5] in text


if __name__ == '__main__':
    pytest.main()
