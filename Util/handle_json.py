# coding=utf-8
import sys
import os

base_path = os.path.dirname(os.getcwd())
sys.path.append(base_path)
import json
from jsonpath_rw import jsonpath, parse


def read_json(file_name=None):
    """
    读取目标路径.json文件中的数据内容
    :param file_name: 相对项目路径
    :return: 返回dict对象
    """
    if file_name == None:
        file_path = os.path.abspath(base_path + "/Config/user_data.json")
    else:
        file_path = os.path.abspath(base_path + file_name)
    with open(file_path, encoding='UTF-8') as f:
        data = json.load(f)
    return data


def get_value(key, file_name=None):
    """
    查询json文件中的key 对应的值
    :param key: json 文件中key
    :param file_name: 相对路径
    :return: 返回key对应的value
    """
    data = read_json(file_name)
    return data.get(key)
    # return data[key]


def write_value(data, file_name=None):
    """
    .json 文件写入数据
    """
    data_value = json.dumps(data)# dict类型转string类型
    if file_name == None:
        path = os.path.abspath(base_path + "/Config/cookie.json")
    else:
        path = os.path.abspath(base_path + file_name)
    with open(path, "w") as f:
        f.write(data_value)


if __name__ == "__main__":
    data = {
        "app": {
            "aaaa": "bbbbbb"
        }
    }
    print(isinstance(data,dict))# True
