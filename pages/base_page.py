# -*- coding: utf-8 -*-
# @Time    : 2020-12-15 下午 05:21
# @Author  : Yuanxuan
# @FileName: base_page.py
# @Software: PyCharm
import warnings

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import \
    NoSuchFrameException, NoSuchWindowException, NoAlertPresentException, NoSuchElementException, TimeoutException
import logging
from time import sleep


class BasePage:
    """
    基础类
    """
    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url
        self.timeout = 5

    def open(self):
        """
        打开url
        """
        self.driver.get(self.base_url)

    def close(self, sleep_time=2):
        """
        关闭浏览器
        :param sleep_time: 等待时间，默认2秒
        :return:
        """
        # 添加删除标记
        warnings.warn("该方法不再维护", DeprecationWarning, stacklevel=2)
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
            WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except TimeoutException:
            logging.error("{}未能找到元属{}".format(self, loc))

    def find_elements(self, loc):
        """
        批量元素定位
        :param loc: 定位元素方法
        :return: 元素地址
        """
        try:
            # 显示等到
            WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except TimeoutException:
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
            # 如果为true，则清空输入框
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
            # 获取需要切换地方
            frame_loc = self.find_element(loc)
            return self.driver.switch_to.frame(frame_loc)
        except NoSuchFrameException as msg:
            logging.error("查找iframe异常-> {0}".format(msg))

    def switch_windows(self):
        """
        多窗口切换
        :return:
        """
        try:
            # 跳转窗口
            all_windows = self.driver.window_handles
            self.driver.close()
            self.driver.switch_to.window(all_windows[1])
        except NoSuchWindowException as msg:
            logging.error("查找窗口句柄handle异常-> {0}".format(msg))

    def switch_alert(self):
        """
        警告框处理, 没什么用
        :return:
        """
        try:
            return self.driver.switch_to.alert()
        except NoAlertPresentException as msg:
            logging.error("查找alert弹出框异常-> {0}".format(msg))

    def get_title(self):
        """
        获取标题
        :return: 标题信息
        """
        return self.driver.title

    def get_current_url(self):
        """
        获取当前页面url
        :return:
        """
        return self.driver.current_url

    @staticmethod
    def get_loc_text(loc):
        """
        获取当前定位loc的文本性质
        :param loc:
        :return:
        """
        warnings.warn("该方法不再维护", DeprecationWarning, stacklevel=2)
        return loc.text

    @staticmethod
    def sleeping(time=1):
        """
        强制等待函数
        """
        sleep(time)
