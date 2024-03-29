# coding=utf-8
import sys
import os
import configparser

base_path = os.getcwd()
sys.path.append(base_path)


class HandleInit:

    def __init__(self):
        pass

    def load_ini(self):
        file_path = base_path + "/Config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    def get_value(self, key, node=None):
        """
        获取.ini 文件里面的value
        :param key: 对应节点下的key
        :param node: 对应节点
        :return:
        """
        if node == None:
            node = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except Exception:
            print("没有获取到值")
            data = None
        return data


handle_ini = HandleInit()


if __name__ == "__main__":
    hi = HandleInit()
    print(hi.get_value("password"))
