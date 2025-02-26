# -*- coding: utf-8 -*-
# @Time    : 2020-12-24 下午 05:12
# @Author  : Yuanxuan
# @FileName: get_yaml.py
# @Software: PyCharm
import yaml


class GetYaml:
    """
    yaml数据引用类
    """
    def __init__(self, file_path):
        self.path = file_path
        self.data = self.get_data()

    def get_data(self):
        """
        加载yaml数据文件
        :return: 返回数据
        """
        try:
            yaml_file = open(self.path, encoding='utf-8')
            data = yaml.safe_load(yaml_file)
            yaml_file.close()
            return data
        except Exception as msg:
            print("异常消息-> {0}".format(msg))

    def get_element_info(self, index):
        """
        获取testcase的element元素
        :param info:
        :return:
        """
        return self.data['testcase'][index]['element_info']

    def get_all_detail(self):
        """
        获取所有的detail信息
        :return:
        """
        return [d['detail'] for d in self.data]

    def all_data(self):
        """
        读取yaml文件数据，
        :return: 返回数据
        """
        return self.data

if __name__ == '__main__':
    import config
    test_case_data = GetYaml(config.TEST_DATA_PATH + '\\' + 'login_page_data.yaml')
    print(test_case_data.get_all_detail())
