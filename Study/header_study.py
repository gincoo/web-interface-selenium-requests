#coding=utf-8
import requests
import hashlib
import json
imooc = "imooc.com"
md5 = hashlib.md5()

data = str({
    'user':'11111'
})
md5.update(data.encode('utf-8'))
res1 = md5.hexdigest()
print(res1)
header = {
    'Host':'m.imooc.com',
    'Connection':'keep-alive',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':'https://m.imooc.com/',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'token':res1
}
url = 'http://www.imooc.com'
res = requests.get(url,headers=header,verify=False).json()
print(res)