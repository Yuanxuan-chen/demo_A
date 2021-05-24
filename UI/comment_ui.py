# -*- coding: utf-8 -*-
# @Time    : 2021/5/22 022 04:38
# @Author  : Yuanxuan
# @FileName: comment_ui.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


class CommentUI:
    """
    评论管理页面定位
    """
    # 进入评论管理页的元素, 需要在已登录的情况下
    dig_comment_page_loc = (By.ID, 'userPic_s')
    # 切换表单
    switch_frame_loc = (By.ID, 'commentIframe')
    # 获取有多少条的评论
    nums_comment_loc = (By.CLASS_NAME, 'news_short_num')
    # 获取所有评论
    list_comment_loc = (By.CLASS_NAME, 'np-post-content.font16')
    # 删除按钮位置
    delete_comment_loc = (By.CLASS_NAME, 'np-btn-delete.delete')
    # 删除按钮-确认
    delete_enter_loc = (By.CLASS_NAME, 'del-enter')
    # 删除按钮-取消
    delete_cancel_loc = (By.CLASS_NAME, 'del-cancel')