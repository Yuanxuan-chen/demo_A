# -*- coding: utf-8 -*-
# @Time    : 2020-12-17 下午 07:04
# @Author  : Yuanxuan
# @FileName: test_base_page.py
# @Software: PyCharm
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from pages import BasePage


class TestBasePage(unittest.TestCase):
    """
    基础类测试集
    """

    driver = webdriver.Chrome()
    url = "https://www.baidu.com"
    URL = "https://dig.chouti.com"

    @classmethod
    def setUpClass(cls) -> None:
        """
        选择浏览器
        :return:
        """
        cls.bp = BasePage(cls.driver, cls.URL)
        cls.bp.open()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        关闭浏览器
        :return:
        """
        sleep(1)
        cls.driver.quit()

    def test_find_element(self):
        self.bp.find_element((By.ID, '666')).send_keys("sddd")
        sleep(1)
        self.bp.find_element((By.ID, 'su')).click()
        sleep(1)

    def test_find_elements(self):
        self.test_find_element()
        test = self.bp.find_elements((By.XPATH, "//div[@tpl='se_com_default']/h3/a"))

        print(len(test))
        for t in test:
            print(t.text)

    def test_script(self):
        js = "window.scrollTo(100,950);"
        self.test_find_element()
        test = self.bp.script(js)
        print(test)

    def test_send_key(self):
        self.bp.send_key((By.ID, 'kw'), "sss")

    def test_switch_windows(self):
        """
        测试多窗口切换
        :return:
        """
        # 获取当前页的窗口句柄
        current_window = self.driver.current_window_handle
        self.bp.find_element((By.LINK_TEXT, '登录')).click()
        self.bp.find_element((By.LINK_TEXT, "立即注册")).click()

        #获取所有页的句柄
        all_windows = self.driver.window_handles
        for handle in all_windows:
            if handle != current_window:
                # 切换到新的句柄
                self.driver.switch_to.window(handle)
                self.driver.find_element_by_name("userName").send_keys('username')
                self.driver.find_element_by_name('phone').send_keys('138xxxxxxx')
                sleep(2)
                # 页面用完记得关闭
                self.driver.close()
        self.driver.switch_to.window(current_window)
        sleep(2)

    def test_switch_windows2(self):
        """
        测试多窗口切换2
        :return:
        """
        self.bp.find_element((By.LINK_TEXT, '登录')).click()
        self.bp.find_element((By.LINK_TEXT, "立即注册")).click()

        # 获取所有页的句柄
        all_windows = self.driver.window_handles

        # 切换到新的句柄
        self.driver.switch_to.window(all_windows[1])
        sleep(2)
        self.driver.switch_to.window(all_windows[0])
        sleep(2)


if __name__ == '__main__':
    unittest.main()
