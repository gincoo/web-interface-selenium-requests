# coding=utf-8
# import sys
# import os
# base_path = os.getcwd()
# sys.path.append(base_path)

from Util.handle_json import HandleJson


def get_cookie_value(cookie_key):
    """
    获取cookie
    :param cookie_key:
    :return: 返回cookie
    """
    data = HandleJson().read_json("/Config/cookie.json")
    return data[cookie_key]


def write_cookie(data, cookie_key):
    """
    写入cookie
    :param data: 写入的cookie 内容
    :param cookie_key: cookie key
    """
    data1 = HandleJson().read_json("/Config/cookie.json")
    data1[cookie_key] = data
    HandleJson().write_value(data1)


if __name__ == "__main__":
    data = {
        "aaaa": "1111111111111111"
    }
    print(write_cookie(data, 'web'))
