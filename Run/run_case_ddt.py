# coding=utf-8
# import sys
import os
#
# base_path = os.getcwd()
# sys.path.append(base_path)
import ddt
import unittest
import json
from Util.handle_excel import excel_data
from Util.handle_header import HandleHeader
from Util.handle_result import HandleResult
from Util.handle_cookie import HandleCookie
from Util.codition_data import get_data
from Base.base_request import request
import HTMLTestRunner

data = excel_data.get_excel_data()  # 数据源
base_path = os.path.dirname(os.getcwd())


#
# ddt数据驱动模式
# 封装好需要
#
@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):

    @ddt.data(*data)
    def test_main_case(self, data):
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        case_id = data[0]
        is_run = data[2]
        i = excel_data.get_rows_number(case_id)
        if is_run == 'yes':
            is_depend = data[3]  # 前置条件
            data1 = json.loads(data[7])  # 请求体
            try:
                if is_depend:  # 是否存在前置条件
                    """
                    获取依赖数据
                    """
                    depend_key = data[4]  # 依赖key
                    depend_data = get_data(is_depend)
                    # print(depend_data)
                    data1[depend_key] = depend_data

                url = data[5]  # 目前不完全url
                method = data[6]  # 请求方式
                cookie_method = data[8]  # cookie 操作方式
                is_header = data[9]  # 是否需要请求头
                excepect_method = data[10]  # 预期结果方式
                excepect_result = data[11]  # 预期结果
                if cookie_method == 'yes':
                    cookie = HandleCookie().get_cookie_value('app')
                if cookie_method == 'write':
                    """
                    必须是获取到cookie
                    """
                    get_cookie = {"is_cookie": "app"}
                if is_header == 'yes':
                    header = HandleHeader().get_header()

                # ---->发起请求
                res = request.run_main(method, url, data1, cookie, get_cookie, header)
                # ---->结果
                # print(res)
                code = str(res['errorCode'])
                message = res['errorDesc']
                # message+errorcode

                if excepect_method == 'mec':
                    config_message = HandleResult().handle_result(url, code)
                    """
                        if message == config_message:
                            excel_data.excel_write_data(i,13,"通过")
                        else:
                            excel_data.excel_write_data(i,13,"失败")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                    """
                    try:
                        self.assertEqual(message, config_message)
                        excel_data.excel_write_data(i, 12, "通过")
                        excel_data.excel_write_data(i, 13, json.dumps(res))
                    except Exception as e:
                        excel_data.excel_write_data(i, 12, "失败")
                        raise e

                if excepect_method == 'errorcode':
                    """
                    if excepect_result == code:
                        excel_data.excel_write_data(i,14,"通过")
                    else:
                        excel_data.excel_write_data(i,13,"失败")
                        excel_data.excel_write_data(i,14,json.dumps(res))
                    """
                    try:
                        self.assertEqual(excepect_result, code)
                        excel_data.excel_write_data(i, 12, "通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 12, "失败")
                        raise e

                if excepect_method == 'json':
                    if code == 1000:
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    excepect_result = HandleResult().get_result_json(url, status_str)
                    result = HandleResult().handle_result_json(res, excepect_result)
                    """
                    if result:
                        excel_data.excel_write_data(i,13,"通过")
                    else:
                        excel_data.excel_write_data(i,13,"失败")
                        excel_data.excel_write_data(i,14,json.dumps(res))   
                    """
                    try:
                        self.assertTrue(result)
                        excel_data.excel_write_data(i, 13, "通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "失败")
                        raise e
            except Exception as e:
                excel_data.excel_write_data(i, 13, "失败")
                raise e


if __name__ == "__main__":
    case_path = os.path.abspath(base_path + "/Run")  # 查找的测试目录
    report_path = os.path.abspath(base_path + "/Report/report.html")  # 输出报告路径
    discover = unittest.defaultTestLoader.discover(case_path, pattern="run_case_*.py")  # 批量
    # unittest.TextTestRunner().run(discover)
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="Mushishi", description="this is test")
        runner.run(discover)
