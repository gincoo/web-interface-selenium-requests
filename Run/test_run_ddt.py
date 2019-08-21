#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from collections.abc import Iterable
from Util.handle_excel import excel_data
import json
import unittest
#from ddt import ddt,data,file_data,unpack
import ddt
import HTMLTestRunner
from Util.handle_header import get_header
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Util.handle_cookie import write_cookie,get_cookie_value
from Base.base_request import request
#['imooc_001', '登陆', 'yes', None, 'login', 'post', '{"username":"111111"}', 'yes', 'message', None]

data = excel_data.get_excel_data()
@ddt.ddt
class TestRunMain(unittest.TestCase):

    @ddt.data(*data)
    def testrun_case(self,data):
        #rows = excel_data.get_rows()
        #for i in range(rows):
        cookie=None
        get_cookie = None
        header = None
        #data = excel_data.get_rows_value(i+2)
        is_run = data[2]
        if is_run == 'yes':
            method = data[5]
            url = data[4]
            data1 = data[6]
            is_header = data[8]
            excepect_method = data[9]
            excepect_result = data[10]
            codition = data[3]
            if codition:
                pass
            cookie_method = data[7]
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
                self.assertEqual(message,config_message)
                '''
                if message == config_message:
                    excel_data.excel_write_data(i+2,12,"通过")
                else:
                    excel_data.excel_write_data(i+2,12,"失败")
                    excel_data.excel_write_data(i+2,13,json.dumps(res))
                '''
            if excepect_method == 'errorcode':
                self.assertEqual(excepect_result,code)
                '''
                if excepect_result == code:
                
                    excel_data.excel_write_data(i+2,12,"通过")
                else:
                    excel_data.excel_write_data(i+2,12,"失败")
                    excel_data.excel_write_data(i+2,13,json.dumps(res))
                '''
            if excepect_method == 'json':
                if code == 1000:
                    status_str='sucess'
                else:
                    status_str='error'
                excepect_result = get_result_json(url,status_str)
                result = handle_result_json(res,excepect_result)
                self.assertTrue(result)
                '''
                if result:
                    excel_data.excel_write_data(i+2,12,"通过")
                else:
                    excel_data.excel_write_data(i+2,12,"失败")
                    excel_data.excel_write_data(i+2,13,json.dumps(res)) 
                '''  
            
def add_case():
    case_path = os.path.join(base_path, "Run")
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test_run_*.py')
    return discover
                
if __name__ == "__main__":
    file_path = base_path+'/Report/report.html'
    with open(file_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="this is test",description="Mushishi test")
        runner.run(add_case())
    f.close()
