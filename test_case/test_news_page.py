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

    @pytest.mark.parametrize("data", test_case_data.all_data())
    def test_read_news(self, data):
        """
        浏览新闻
        :return:
        """
        self.np.dig_news()
        text = self.np.switch_news(data['data']['index'])
        self.np.move_news_page()
        self.np.comment_news(data['data']['comment'])

        # logging.info(text)
        # logging.warning(self.np.get_title()[:-5])
        assert self.np.get_title()[:-5] == text


if __name__ == '__main__':
    pytest.main()
