# coding=utf-8
# selenium web
import requests
import time
from selenium import webdriver

cookie1 = {
    "apsid": ""
}

driver = webdriver.Chrome()
driver.get("https://www.imooc.com/user/newlogin")
time.sleep(4)
# driver.find_element_by_id("js-signin-btn").click()
time.sleep(3)
driver.find_element_by_name("email").send_keys("mushishi_xu@163.com")
driver.find_element_by_name("password").send_keys("xu221168")
driver.find_element_by_class_name("moco-btn-lg").click()
time.sleep(3)
cookie = driver.get_cookies()
print('cookie--->', cookie)

for i in cookie:
    if i['name'] == 'apsid':
        cookie1['apsid'] = i['value']
print('cookie1--->', cookie1)
driver.close()

download_url = 'https://www.imooc.com/user/postpic'

file = {
    "fileField": ("test.jpg", open("E:/ytxu/test.jpg", "rb"), "image/jpg"),
    "type": "1"
}

res = requests.post(url=download_url, files=file, cookies=cookie1, verify=False).text
print(res)

"""
执行结果打印:

C:\xxpython.exe D:/interface-seleium-requsets/Study/cookie_study.py
cookie---> [{'domain': '.imooc.com', 'httpOnly': False, 'name': 'cvde', 'path': '/', 'secure': False, 'value': '5d622ad150f04-6'},
 {'domain': '.imooc.com', 'httpOnly': False, 'name': 'Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968', 'path': '/', 'secure': False, 'value': '1566714588'}, 
 {'domain': '.imooc.com', 'expiry': 1567319386.574788, 'httpOnly': False,'name': 'loginstate', 'path': '/', 'secure': False, 'value': '1'},
  {'domain': '.imooc.com', 'expiry': 1567319386.574847,'httpOnly': False, 'name': 'last_login_username', 'path': '/', 'secure': False, 'value': 'Mushishi_xu%40163.com'},
   {'domain': '.imooc.com', 'expiry': 1598250576.437852, 'httpOnly': False, 'name': 'imooc_isnew', 'path': '/','secure': False, 'value': '1'},
   
    {'domain': '.imooc.com', 'expiry': 1567319386.574822, 'httpOnly': False, 
    'name': 'apsid', 'path': '/', 'secure': False, 
    'value': 'I5ZTVmZmUzMGE1NDY2OTljZjFjYzkyMTMyMjk3MmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANzIxMzU2MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABNdXNoaXNoaV94dUAxNjMuY29tAAAAAAAAAAAAAAAAADg2NzQxY2UxZjE0NzMyOTY2YWRkYWUxYmNjOWIxNWM02ypiXdsqYl0%3DZW'}, 
   
    {'domain': '.imooc.com', 'expiry': 1566800987, 'httpOnly': False, 'name': 'IMCDNS', 'path': '/', 'secure': False, 'value': '0'},
     {'domain': '.imooc.com', 'expiry': 1598250587, 'httpOnly': False, 'name': 'zg_did', 'path': '/', 'secure': False, 'value': '%7B%22did%22%3A%20%2216cc77740bc3a-02a5bcaf985943-396a4507-144000-16cc77740bd35d%22%7D'}, 
     {'domain': '.imooc.com', 'expiry': 1598250576.437774, 'httpOnly': False, 'name': 'imooc_uuid', 'path': '/', 'secure': False, 'value': '512d2edb-9547-43f4-a2c8-47df0581f707'}, 
     {'domain': '.imooc.com', 'expiry': 1598250576.437896, 'httpOnly': False, 'name': 'imooc_isnew_ct', 'path': '/', 'secure': False, 'value': '1566714577'},
      {'domain': '.imooc.com', 'expiry': 1598250587, 'httpOnly': False, 'name': 'zg_f375fe2f71e542a4b890d9a620f9fb32', 'path': '/', 'secure': False, 'value': '%7B%22sid%22%3A%201566714577094%2C%22updated%22%3A%201566714587443%2C%22info%22%3A%201566714577101%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E6%85%95%E8%AF%BE%E7%BD%91%E6%95%B0%E6%8D%AE%E7%BB%9F%E8%AE%A1%5C%22%2C%5C%22Platform%5C%22%3A%20%5C%22web%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22FUhceq2fwfI%2C%22%7D'}, 
      {'domain': '.imooc.com', 'expiry': 1598250587, 'httpOnly': False, 'name': 'Hm_lvt_f0cfcccd7b1393990c78efdeebff3968', 'path': '/', 'secure': False, 'value': '1566714577'}]

cookie1---> {'apsid': 'I5ZTVmZmUzMGE1NDY2OTljZjFjYzkyMTMyMjk3MmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANzIxMzU2MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABNdXNoaXNoaV94dUAxNjMuY29tAAAAAAAAAAAAAAAAADg2NzQxY2UxZjE0NzMyOTY2YWRkYWUxYmNjOWIxNWM02ypiXdsqYl0%3DZW'}

Traceback (most recent call last):
  File "D:/Users/python-code/interface-seleium-requsets/Study/cookie_study.py", line 31, in <module>
    "fileField": ("test.jpg", open("E:/ytxu/test.jpg", "rb"), "image/jpg"),

FileNotFoundError: [Errno 2] No such file or directory: 'E:/ytxu/test.jpg'

Process finished with exit code 1


















"""