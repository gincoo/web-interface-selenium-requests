# coding=utf-8
import sys
import os

base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_excel import excel_data
from jsonpath_rw import parse
import json


#
# ddt 依赖数据操作类
#
class HandleData():

    def __split_data(self, data):
        """
        拆分单元格数据
        :param data:
        :return:
        """
        # imooc_005>data:banner:id
        case_id = data.split(">")[0]
        rule_data = data.split(">")[1]
        return case_id, rule_data

    def __depend_data(self, data):
        """
        获取依赖结果集
        :param data:
        :return:
        """
        case_id = self.__split_data(data)[0]
        row_number = excel_data.get_rows_number(case_id)
        data = excel_data.get_cell_value(row_number, 14)
        return data

    def __get_depend_data(self, res_data, key):
        """
        获取依赖字段
        :param res_data:
        :param key:
        :return:
        """
        res_data = json.loads(res_data)
        json_exe = parse(key)
        madle = json_exe.find(res_data)
        return [math.value for math in madle][0]

    def get_data(self, data):
        """
        获取依赖数据
        :param data:
        :return:
        """
        res_data = self.__depend_data(data)
        rule_data = self.__split_data(data)[1]
        return self.__get_depend_data(res_data, rule_data)


if __name__ == "__main__":
    # print(depend_data("imooc_007>data:banner:id"))
    data = {
        "a": "a1",
        "b": "b1",
        "c": [
            {
                "d": "d1"
            },
            {
                "d": "d2"
            }
        ]
    }
    key = 'c.[1].d'
    # print(__get_depend_data(data, key))
