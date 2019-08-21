#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from mitmproxy import http
from Util.handle_json import get_value
import json
class GetData:

    def request(self,flow):
        request_data = flow.request
        self.request_url = request_data.url
        request_pr = request_data.query
        request_form = request_data.urlencoded_form
        print("url:-------->",self.request_url)
        #print("request_pr:------------->",request_pr)
        #print("request_form:---------->",request_form)

    def response(self,flow):
        if 'imooc' in self.request_url or 'mukewang' in self.request_url:
            response_data = flow.response
            host = self.request_url.split(".com")
            base_url = host[0]
            url = host[1]
            #/api3/getbanneradvertver2
            #api3/getbanneradvertver2?aaa=sss
            if "?" in host[1]:
                url = url.split("?")[0]
            print("====>",url)
            data = json.dumps(get_value(url))
            print("----->data:",data)
            response_data.set_text(data)
            '''
            response_header = response_data.headers
            conten_type = response_header['Content-Type']
            print("========>",conten_type)
            if conten_type == 'image/jpeg':
                print("这个返回的是图片")
            elif  'json' in conten_type:
                print("code=========>",response_data.status_code)
                print("response=======>",response_data.text)
            else:
                print("格式不是我们预期的")
            '''
            #1、高级得mock
            
addons = [
    GetData()
]

