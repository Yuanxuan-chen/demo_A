# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 下午 02:28
# @Author  : Yuanxuan
# @FileName: run_start.py.py
# @Software: PyCharm
import pytest
import config
import os

if __name__ == '__main__':
    raw = '../report/raw_file'
    report = '../report/report_file/'  + config.now_time # 需要保存的时候就去掉注释
    pytest.main(["test_login_page.py::TestLoginPage", "--alluredir={}".format(raw), "--clean-alluredir"])
    os.system("allure generate {} -o {} --clean".format(raw, report))
