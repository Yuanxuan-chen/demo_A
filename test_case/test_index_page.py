# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 下午 03:51
# @Author  : Yuanxuan
# @FileName: test_index_page.py
# @Software: PyCharm
import allure

from utils import MyPyTest
from utils import GetYaml
from pages import IndexPage
import config

import pytest

@allure.epic("首页")
@allure.feature("导航栏")
class TestIndexPage(MyPyTest):
    """
    主页测试类
    """

    def setup(self):
        self.ip = IndexPage(self.driver, config.URL_tencent)
        self.ip.open()

    # 主页导航栏测试数据
    navi_test_case_data = GetYaml(config.TEST_DATA_PATH + '\\index_page\\' + 'navi_data.yaml')

    @pytest.mark.parametrize("data", navi_test_case_data.all_data())
    def test_navigate_main(self, data):
        """
        主页导航栏测试
        首页点击顶部分类，是否能够跳转到对应的主题界面（新闻、视频、图片…）
        :param data:
        :return:
        """
        with allure.step("导航栏选择"):
            self.ip.navigate_main(data)
            self.ip.sleeping()
            # 获取当前页面的标题
            text = self.ip.get_title()
            # 断言data的数据在text里
        assert data in text


if __name__ == '__main__':
    pytest.main()

