#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_json import get_value
import json_tools
import json
def cmp(src_data,dst_data):
    if isinstance(src_data, dict):
        """若为dict格式"""
        for key in dst_data:
            if key not in src_data:
                print("src不存在这个key")
        for key in src_data:
            if key in dst_data:
                thiskey = key
                """递归"""
                cmp(src_data[key], dst_data[key])
            else:
                src_data[key] = ["dst不存在这个key"]
    elif isinstance(src_data, list):
        """若为list格式"""
        if len(src_data) != len(dst_data):
            print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            """递归"""
            cmp(src_list, dst_list)
    else:
        if str(src_data) != str(dst_data):
            print(src_data)
        
dict1 = get_value("api3/newcourseskill")
dict2 = get_value("api3/getbanneradvertver2")
cmp(dict1,dict2)