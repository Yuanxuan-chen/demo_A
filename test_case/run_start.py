# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 下午 02:28
# @Author  : Yuanxuan
# @FileName: run_start.py.py
# @Software: PyCharm
import pytest
import config
import os

if __name__ == '__main__':
    #文件保存路径
    raw = '../report/raw_file'
    report = '../report/report_file/' # + config.now_time # 需要保存的时候就去掉注释

    # 生成测试报告
    pytest.main(["test_login_page.py::TestLoginPage", "--alluredir={}".format(raw), "--clean-alluredir" ])
    # 启动测试报告
    os.system("allure serve {}".format(raw))
    # 测试报告转html，并保存
    os.system("allure generate {} -o {} --clean".format(raw, report))
