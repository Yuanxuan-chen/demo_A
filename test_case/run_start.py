# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 下午 02:28
# @Author  : Yuanxuan
# @FileName: run_start.py.py
# @Software: PyCharm
import pytest
import config
import os
import shutil

if __name__ == '__main__':
    #文件保存路径
    raw = '../report/raw_file'
    report = '../report/report_file/' # + config.now_time # 需要保存的时候就去掉注释，不然下次运行会覆盖旧数据

    # 生成测试报告
    pytest.main(["test_login_page.py::TestLoginPage",
                 "test_news_page.py::TestNewsPage",

    "--alluredir={}".format(raw), "--clean-alluredir" ])
    # 将运行环境拷贝到测试报告中
    shutil.copy('../config/environment.properties', '{}/environment.properties'.format(raw))

    # 启动测试报告
    # os.system("allure serve {}".format(raw))

    # 测试报告转html，并保存
    os.system("allure generate {} -o {} --clean".format(raw, report))
