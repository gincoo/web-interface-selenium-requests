# coding=utf-8
import sys
import os

# base_path = os.getcwd()
# sys.path.append(base_path)
import unittest
import json
import mock
import HTMLTestRunner
from Base.base_request import request
from Util.handle_json import HandleJson
from Util.handle_init import HandleInit

host = HandleInit().get_value(key='host')  # 'http://www.imooc.com/'

base_path = os.path.dirname(os.getcwd())
path = os.path.abspath(base_path + "/Config/user_data.json")


# def read_json():
#     with open(base_path + "/Config/user_data.json") as f:
#         data = json.load(f)
#     return data
#
# def get_value(key):
#     data = read_json()
#     return data[key]


class ImoocCase(unittest.TestCase):

    def test_banner(self):
        url = host + 'api3/getbanneradvertver2'
        data = {
            'timestamp': '1561269343481',
            'uid': '7213561',
            'token': '7ad09430cbaf927af642ab843ec374ef',
            'type': '1',
            'marking': 'androidbanner',
            'uuid': '41b650ef846688193728ff7381eb6c1c',
            'secrect': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY'
        }
        mock_method = mock.Mock(return_value=HandleJson().get_value('api3/getbanneradvertver2', file_name=path))
        request.run_main = mock_method
        res = request.run_main('post', url, data)
        self.assertEqual(res['errorCode'], 1000)

    def beta4(self):
        url = host + 'api3/beta4'
        data = {
            'timestamp': '1561269343486',
            'uid': '7213561',
            'token': '66640986fb118dda4334719ac8afbf89',
            'uuid': '41b650ef846688193728ff7381eb6c1c',
            'secrect': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY',
        }
        mock_method = mock.Mock(return_value=HandleJson().get_value('api3/beta4', file_name=path))
        request.run_main = mock_method
        res = request.run_main('post', url, data)
        self.assertEqual(res['errorCode'], 1000)

    def test_new_register(self):
        username = '13211111'
        url = "register"
        data = {
            "user": username
        }

    def test_old_register(self):
        url = "register"
        data = {
            "user": "11111"
        }


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ImoocCase('test_banner'))
    suite.addTest(ImoocCase('beta4'))
    file_path = os.path.abspath(base_path + '/Report/report.html')
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is test", description="Mushishi test")
        runner.run(suite)
    f.close()
    # unittest.main()
