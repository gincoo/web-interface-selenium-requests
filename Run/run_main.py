#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from collections.abc import Iterable
from Util.handle_excel import excel_data
import json
from Util.handle_header import get_header
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Util.handle_cookie import write_cookie,get_cookie_value
from Util.codition_data import get_data
from Base.base_request import request
#['imooc_001', '登陆', 'yes', None, 'login', 'post', '{"username":"111111"}', 'yes', 'message', None]
class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            cookie=None
            get_cookie = None
            header = None
            depend_data = None
            data = excel_data.get_rows_value(i+2)
            is_run = data[2]
            if is_run == 'yes':
                is_depend = data[3]
                data1 = json.loads(data[7])
                if is_depend:
                    '''
                    获取依赖数据
                    '''
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    #print(depend_data)
                    data1[depend_key] = depend_data

                method = data[6]
                url = data[5]
                
                is_header = data[9]
                excepect_method = data[10]
                excepect_result = data[11]
                cookie_method = data[8]
                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    '''
                    必须是获取到cookie
                    '''
                    get_cookie={"is_cookie":"app"}
                if is_header == 'yes':
                    header = get_header()
                res = request.run_main(method,url,data1,cookie,get_cookie,header)
                #print(res)
                code = str(res['errorCode'])
                message = res['errorDesc']
                if excepect_method == 'mec': 
                    config_message = handle_result(url,code)
                    if message == config_message:
                        excel_data.excel_write_data(i+2,13,"通过")
                    else:
                        excel_data.excel_write_data(i+2,13,"失败")
                        excel_data.excel_write_data(i+2,14,json.dumps(res))
                if excepect_method == 'errorcode':
                    if excepect_result == code:
                        excel_data.excel_write_data(i+2,14,"通过")
                    else:
                        excel_data.excel_write_data(i+2,13,"失败")
                        excel_data.excel_write_data(i+2,14,json.dumps(res))
                if excepect_method == 'json':
                    if code == 1000:
                        status_str='sucess'
                    else:
                        status_str='error'
                    excepect_result = get_result_json(url,status_str)
                    result = handle_result_json(res,excepect_result)
                    if result:
                        excel_data.excel_write_data(i+2,13,"通过")
                    else:
                        excel_data.excel_write_data(i+2,13,"失败")
                        excel_data.excel_write_data(i+2,14,json.dumps(res))   
                
if __name__ == "__main__":
    run = RunMain()
    run.run_case()
