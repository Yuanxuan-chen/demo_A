# -*- coding: utf-8 -*-
# @Time    : 2020-12-15 下午 05:21
# @Author  : Yuanxuan
# @FileName: base_page.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException, NoSuchWindowException, NoAlertPresentException, NoSuchElementException
import logging
from time import sleep

S = """
        多个元素定位
        :param loc: 定位元素方法
        :return: 元素地址集
        """


class BasePage:
    """
    基础类
    """
    def __init__(self, driver, url, parent=None):
        self.driver = driver
        self.base_url = url
        self.parent = parent
        self.timeout = 5

    def open(self):
        """
        打开url，并最大化窗口
        """
        self.driver.get(self.base_url)

    def close(self, sleep_time = 2):
        """
        关闭浏览器
        :param sleep_time: 等待时间，默认2秒
        :return:
        """
        sleep(sleep_time)
        self.driver.quit()

    def find_element(self, loc):
        """
        单个元素定位
        :param loc: 定位元素方法
        :return: 元素地址
        """
        try:
            # 隐式等待
            #   self.driver.implicitly_wait(10)
            # 显示等待
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            logging.error("{}未能找到元属{}".format(self, loc))

    def find_elements(self, loc):

        try:
            # 显示等到
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            logging.error("{}未能找到元素{}".format(self, loc))

    def script(self, js_code):
        """
        执行JavaScript代码
        :param js_code: js代码
        :return: 我也不知道，模板是这样写的，应该有用

        # js脚本定位点击
        # 应对错误:
        # 1. selenium.common.exceptions.ElementClickInterceptedException
        # 2. Message: element click intercepted
        # 3. 当前元素被其他元素遮挡
        element = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].click();", element)
        """
        return self.driver.execute_script(js_code)

    def send_key(self, loc, value, clear=True):
        """
        重新定义send_keys方法
        :param loc: 元素定位
        :param value: 传输的值
        :param clear: 是否空输入框，默认清空
        :return:
        """
        try:
            locator = self.find_element(loc)
            if clear:
                locator.clear()
            locator.send_keys(value)
        except AttributeError:
            logging.error("{}页面未能找到元素{}".format(self, loc))

    def switch_frame(self, loc):
        """
        多表单嵌套切换
        :return:
        """
        try:
            return self.driver.switch_to.frame(loc)
        except NoSuchFrameException as msg:
            logging.error("查找iframe异常-> {0}".format(msg))

    def switch_windows(self, loc):
        """
        多窗口切换, 没什么用
        :param loc:
        :return:
        """
        try:
            return self.driver.switch_to_window(loc)
        except NoSuchWindowException as msg:
            logging.error("查找窗口句柄handle异常-> {0}".format(msg))

    def switch_alert(self):
        """
        警告框处理, 没什么用
        :return:
        """
        try:
            return self.driver.switch_to_alert()
        except NoAlertPresentException as msg:
            logging.error("查找alert弹出框异常-> {0}".format(msg))
