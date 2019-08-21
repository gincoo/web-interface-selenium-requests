#coding=utf-8
import requests
import json
import time
from selenium import webdriver
cookie1 = {
    "apsid":""
}
opt = webdriver.ChromeOptions()
opt.set_headless()
driver = webdriver.Chrome(options=opt)
driver.get("https://www.imooc.com/user/newlogin")
time.sleep(4)
#driver.find_element_by_id("js-signin-btn").click()
time.sleep(3)
driver.find_element_by_name("email").send_keys("mushishi_xu@163.com")
driver.find_element_by_name("password").send_keys("xu221168")
driver.find_element_by_class_name("moco-btn-lg").click()
time.sleep(3)
cookie = driver.get_cookies()
for i in cookie:
    if i['name'] == 'apsid':
        cookie1['apsid'] = i['value']
driver.close()
#dict
#requests jar
cookie_jar = requests.utils.cookiejar_from_dict(cookie1)
print("-------->",cookie_jar)
session = requests.Session()
session.cookies = cookie_jar

#登陆
download_url = 'https://www.imooc.com/user/postpic'
file = {
    "fileField":("test.jpg",open("E:/ytxu/test.jpg","rb"),"image/jpg"),
    "type":"1"
}
res = session.post(url=download_url,files=file,verify=False)

print(session.headers)
print("--------------------")
print(res.request.headers)
#下单
#.post()