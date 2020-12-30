import unittest
import time

from utils import HTMLTestRunner
from utils import SMTP
import config

# 批量导入测试用例
suite = unittest.defaultTestLoader.discover(start_dir=config.TEST_CASE_PATH, pattern='test_login*.py')

# 运行器
# runner = unittest.TextTestRunner()
# runner.run(suite)
# 生成html测试报告

# html测试报告名称 + 时间戳
now_time = time.strftime("%Y-%m-%d %H_%M_%S")
fp = open(config.TEST_REPORT_PATH + "\\" + now_time + "test_report.html", "wb")

# stream: 输出目标文件, title: 报告标题, description: 备注
runner = HTMLTestRunner(stream=fp, title="first_report", description="试一试: first_report")
runner.run(suite)
fp.close()
