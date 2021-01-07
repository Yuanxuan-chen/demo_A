# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 下午 02:35
# @Author  : Yuanxuan
# @FileName: __init__.py.py
# @Software: PyCharm
import os
"""
笔记
os.getcwd() 获取当前文件的路径
os.path.dirname() 获取当前文件的文件夹的路径，即上一级的路径
os.path.join() 拼接路径
"""
# 项目文件夹的路径
BASE_DIR_PATH = os.path.dirname(os.getcwd())
# 元素控件
ELEMENT_PATH = os.path.join(BASE_DIR_PATH, "yaml", "element")
# 测试数据
TEST_DATA_PATH = os.path.join(BASE_DIR_PATH, "yaml", "test_data")
# 测试报告
TEST_REPORT_PATH = os.path.join(BASE_DIR_PATH, "report", "report_file")
# 测试用例
TEST_CASE_PATH = os.path.join(BASE_DIR_PATH, "test_case")

# WebURL地址
URL_chouti = 'https://dig.chouti.com'
URL_baidu = "https://www.baidu.com"
URL_tencent = 'https://www.qq.com/'
URL_126 = 'https://www.126.com/'
# url选择器
URL = URL_tencent
