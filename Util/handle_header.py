# coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)

from Util.handle_json import HandleJson

class HandleHeader:

    def get_header(self):
        data = HandleJson().read_json("/Config/header.json")
        return data


    def header_md5(self):
        data = self.get_header()
        key = data['imooc_key']
