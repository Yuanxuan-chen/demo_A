# -*- coding: utf-8 -*-
# @Time    : 2021/5/22 022 04:40
# @Author  : Yuanxuan
# @FileName: comment_page.py
# @Software: PyCharm
import allure

from pages import BasePage
from UI import CommentUI


class CommentPage(BasePage):
    """
    评论管理页面
    """
    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('跳转到评论管理页面')
    def dig_comment_page(self):
        """
        跳转到评论管理页面
        :return:
        """
        self.find_element(CommentUI.dig_comment_page_loc).click()

    def comment_switch_frame(self):
        """
        定位评论前先切换表单
        :param loc:
        :return:
        """
        self.switch_frame(CommentUI.switch_frame_loc)

    def nums_comment(self):
        """
        获取评论数量
        :return:
        """
        ele = self.find_element(CommentUI.nums_comment_loc)
        return ele.text

    @allure.step("浏览评论信息")
    def list_comment(self):
        """
        获取所有评论信息
        :return:
        """
        ele = self.find_elements(CommentUI.list_comment_loc)
        if not ele:
            return []
        return [ele.text for ele in ele]

    def list_delete_button(self):
        """
        获取所有评论的删除按钮
        :return:
        """
        return self.find_elements(CommentUI.delete_comment_loc)

    @allure.step('点击删除按钮')
    def dig_delete_button(self, data, loc):
        """
        点击选择的删除按钮
        :param loc:
        :return:
        """
        # 点击删除
        loc.click()

    @allure.step('选择是否确认删除')
    def delete_enter_or_cancel(self, enter_or_cancel=2):
        # 点击确认删除
        if enter_or_cancel == 1:
            self.find_element(CommentUI.delete_enter_loc).click()
        elif enter_or_cancel == 2:
            self.find_element(CommentUI.delete_cancel_loc).click()