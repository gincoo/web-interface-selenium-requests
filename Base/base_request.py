# coding=utf-8
import sys
import os
# base_path = os.path.dirname(os.getcwd())
# sys.path.append(base_path)
import requests
import json
from Util.handle_cookie import write_cookie
from Util.handle_init import handle_ini


# 基础接口请求封装类
# 使用的三方 requests 框架
#
class BaseRequest:

    def send_post(self, url, data, cookie=None, get_cookie=None, header=None):
        """
        post 请求
        :param url: 请求url
        :param data: 请求参数
        :param cookie: cookie
        :param get_cookie:
        :param header: 请求头
        :return:
        """
        response = requests.post(url=url, data=data, cookies=cookie, headers=header)
        if get_cookie != None:
            '''
            {"is_cookie":"app"}
            '''
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    def send_get(self, url, data, cookie=None, get_cookie=None, header=None):
        """
        get 请求
        :param url: 请求url
        :param data: 请求体
        :param cookie:  cookie
        :param get_cookie:
        :param header:  请求头
        :return:
        """
        response = requests.get(url=url, params=data, cookies=cookie, headers=header)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    def run_main(self, method, url, data, cookie=None, get_cookie=None, header=None):
        """
        执行请求 (默认必传method、url、data参数)
        :param method: get\post请求方式
        :param url: url
        :param data: 请求体
        :param cookie: cookie
        :param get_cookie:
        :param header: 请求头
        :return:
        """
        # return get_value(url)
        base_url = handle_ini.get_value('host')
        if 'http' not in url:
            url = base_url + url
        if method == 'get':
            res = self.send_get(url, data, cookie, get_cookie, header)
        else:
            res = self.send_post(url, data, cookie, get_cookie, header)

        try:
            res = json.loads(res)#dict转string
        except:
            print("这个结果是一个text")
        print("--->", res)
        return res


request = BaseRequest()
if __name__ == "__main__":
    request = BaseRequest()
    request.run_main('get', 'http://www.baidu.com/login', "{'username':'11111'}")
