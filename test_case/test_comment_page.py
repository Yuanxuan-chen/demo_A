# -*- coding: utf-8 -*-
# @Time    : 2021/5/22 022 04:50
# @Author  : Yuanxuan
# @FileName: test_comment_page.py
# @Software: PyCharm
import allure
import pytest
import config
import logging
from pages import CommentPage
from utils import MyPyTest_user


@allure.epic('评论管理')
class TestCommentPage(MyPyTest_user):
    """
    评论管理页测试类
    """

    def setup(self):
        self.cp = CommentPage(self.driver, config.URL)
        self.cp.open()

    def teardown(self):
        self.cp.sleeping()

    list_comment_data = [
        '已登录的情况下，是否可以进入评论管理界面',
        '未登录的情况下，是否可以进入评论管理界面',
        '是否可以进入查看所有的评论',
    ]

    @allure.story("评论浏览，评论查看")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("data", list_comment_data)
    def test_list_comment(self, data):
        """
        评论浏览，评论查看
        :param data:
        :return:
        """
        self.cp.dig_comment_page()
        self.cp.comment_switch_frame()
        num1 = int(self.cp.nums_comment())
        num2 = len(self.cp.list_comment())
        # logging.info(data)
        if not num2:
            num2 = 0
        # 对比信息是否一致
        assert num1 == num2

    delete_comment_data = [
        ['信息不存在', '2', '1'],
        ['信息存在，确认删除', 'Asdasdasd123123.。、，、。，、。，《》《》《：“：”；', '1'],
        ['信息存在，确认删除', '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '1'],
        ['信息存在，取消删除', '1', '0']
    ]

    @allure.story("评论删除")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("info, data, enter_or_cancel", delete_comment_data)
    def test_delete_comment(self, info, data, enter_or_cancel):
        """
        评论删除
        :param data: 选择的新闻
        :param enter_or_cancel: 是否确认删除，1是，2否
        :return:
        """
        # 跳转到评论管理页面
        self.cp.dig_comment_page()
        self.cp.comment_switch_frame()
        # 获取所有评论信息
        comment = self.cp.list_comment()
        # 判断是否有评论，并且想要删除的评论是否存在
        with allure.step('判断评论是否存在？'):
            if comment and data in comment:
                # 定位想要删除的评论
                delete_loc = self.cp.list_delete_button()[comment.index(data)]
                # 点击删除
                self.cp.dig_delete_button(data, delete_loc)
                # 是否确认删除
                self.cp.delete_enter_or_cancel(enter_or_cancel)
