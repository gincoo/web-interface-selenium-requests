#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from mitmproxy import http
from Util.handle_json import get_value
import json
class MockServer:

    def request(self,flow):
        request_data = flow.request
        #imooc.com
        #127.0.0.1:5000
        self.request_url = request_data.url
        request_data.host='127.0.0.1'
        request_data.port=5000

    def response(self,flow):
        if 'imooc' in self.request_url or 'mukewang' in self.request_url:
            response_data = flow.response
            host = self.request_url.split(".com")
            #base_url = host[0]
            url = host[1]
            if "?" in host[1]:
                url = url.split("?")[0]
            data = json.dumps(get_value(url))
            response_data.set_text(data)          
addons = [
    MockServer()
]