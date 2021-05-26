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
    news_page_frame_loc = (By.ID, 'commentIframe')

    # 评论框输入数据
    input_loc = (By.ID, 'J_Textarea')

    # 评论发表按钮
    submit_comment_button_loc = (By.ID, 'J_PostBtn')

    # 新闻评论总页面
    news_comment_loc = (By.CLASS_NAME, 'comment-count')

    # 评论总页转换frame表单
    commnet_page_frame_loc = (By.ID, 'commentIframe')

    # 获取当前页的所有评论
    list_comment_loc = (By.CLASS_NAME, 'comment-content.J_CommentContent')

    # 获取当前页所有的点赞按钮
    list_like_button_loc = (By.CLASS_NAME, 'J_Vote.comment-operate-item.comment-operate-up')