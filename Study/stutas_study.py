#coding=utf-8
import requests
import json
url = 'http://www.imooc.com/order/test/ssssss'
#res = requests.get(url).status_code
res = requests.get(url).raise_for_status()
#res = requests.codes.ok


print(res)