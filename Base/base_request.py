#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
import requests
import json
from Util.handle_cookie import write_cookie
from Util.handle_json import get_value
from Util.handle_init import handle_ini

class BaseRequest:
    def send_post(self,url,data,cookie=None,get_cookie=None,header=None):
        '''
        发送post请求
        '''
        response = requests.post(url=url,data=data,cookies=cookie,headers=header)
        if get_cookie !=None:
            '''
            {"is_cookie":"app"}
            '''
            cookie_value_jar =  response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res
    
    def send_get(self,url,data,cookie=None,get_cookie=None,header=None):
        '''
        发视get请求
        '''
        response = requests.get(url=url,params=data,cookies=cookie,headers=header)
        if get_cookie !=None:
            cookie_value_jar = response.cookie
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])

        res = response.text
        return res
    
    def run_main(self,method,url,data,cookie=None,get_cookie=None,header=None):
        '''
        执行方法，传递method、url、data参数
        '''
        #return get_value(url)
        base_url = handle_ini.get_value('host')
        if 'http' not in url:
            url = base_url+url
        
        if method == 'get':
            res = self.send_get(url,data,cookie,get_cookie,header)
        else:
            res = self.send_post(url,data,cookie,get_cookie,header)
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        print("--->",res)
        return res

    
    
request = BaseRequest() 
if __name__ == "__main__":
    request = BaseRequest() 
    request.run_main('get','http://www.baidu.com/login',"{'username':'11111'}")