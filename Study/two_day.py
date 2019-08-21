#coding=utf-8
import requests
import json
#上传文件
#url = 'https://www.imooc.com/user/postpic'
download_url = 'http://file.mukewang.com/imoocweb/webroot/mobile/imooc7.2.010102001android.apk'
file = {
    "fileField":("test.jpg",open("E:/ytxu/test.jpg","rb"),"image/jpg"),
    "type":"1"
}
cookie = {
    "apsid":"I5ZTVmZmUzMGE1NDY2OTljZjFjYzkyMTMyMjk3MmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANzIxMzU2MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABNdXNoaXNoaV94dUAxNjMuY29tAAAAAAAAAAAAAAAAADVjZDY5ZWYxMGQ2MmFlZDVmNTJkYWQ0ZWNhNjU5MjZhz%2BMFXc%2FjBV0%3DZW"
}
res = requests.get(download_url)
with open("mukewang.apk","wb") as f:
    f.write(res.content)
#res = requests.post(url,files=file,cookies=cookie,verify=False).json()
print(res)
#res = requests.post(url,files=file,cookies=cookie,verify=False).json()
print(res)
