# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 下午 04:38
# @Author  : Yuanxuan
# @FileName: test_news_page.py
# @Software: PyCharm
from utils import MyPyTest, MyPyTest_user
from pages import NewsPage
import config
from utils import GetYaml

import pytest
import allure
import logging

test_case_data = GetYaml(config.TEST_DATA_PATH + '\\' + 'news_page_data.yaml')


@allure.epic("新闻页")
@allure.feature("已登录，浏览新闻,并评论")
class TestNewsPage(MyPyTest_user):
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

    @allure.story("评论新闻，添加评论")
    @allure.severity(allure.severity_level.NORMAL)
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
        self.np.submit_comment()

    like_comment_data = [
        '已登录的情况下，是否可以进入评论管理界面',
        '未登录的情况下，是否可以进入评论管理界面',
        '是否可以进入查看所有的评论',
        '是否可以点赞别人的评论',
        '是否可以点赞自己的评论',
        '是否可以重复点赞',
    ]

    @allure.story("浏览评论并赞")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("data", like_comment_data)
    def test_like_comment(self, data):
        """
        浏览评论并赞
        :param data:
        :return:
        """
        self.np.dig_news()
        self.np.switch_news(1)
        # 进入所有评论页面
        self.np.dig_news_comment()
        self.np.comment_page_switch_frame()
        # 获取所有评论信息
        comment = self.np.list_comment()
        logging.info(comment)
        with allure.step('判断评论是否存在？'):
            if comment:
                # 获取所有点赞按钮
                like_button_loc = self.np.list_like_button()[1]
                # 点击点赞按钮
                self.np.dig_like_button(like_button_loc)


@allure.feature("未登录，浏览新闻,并评论")
class TestNewsPage_no_user(MyPyTest):
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

    list_comment = [
        ['未登录是否能够评论成功', '1', 'sadsadasd'],
    ]

    @allure.story("评论新闻，添加评论")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("info, index, data", list_comment)
    def test_read_news(self, info, index, data):
        """
        浏览新闻,对新闻进行评论
        :return:
        """
        # 进入新闻页面
        self.np.dig_news()
        # 随机选择新闻
        text = self.np.switch_news(index)
        # 浏览新闻，移动到底部
        self.np.move_news_page()
        # 评论新闻
        self.np.comment_news(data)
        self.np.submit_comment_no_user()
        text = self.np.get_title()
        assert text == 'QQ帐号安全登录'

if __name__ == '__main__':
    pytest.main()
