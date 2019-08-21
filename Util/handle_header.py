#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_json import read_json

def get_header():
    data = read_json("/Config/header.json")
    return data

def header_md5():
    '''
    
    '''
    data = get_header()
    key = data['imooc_key']
