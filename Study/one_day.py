import requests
import json
url = 'https://www.imooc.com/api3/updateversion'
get_url = 'https://www.imooc.com/apiw/logo?callback=jQuery2100784114534733817_1560664870423&_=1560664870424'
#(1,2,3,4,)
data = {
    'v':'5.1.2',
    'v_code':'5120',
    'token':'5c1d2b3f9ac501dc8a5c2345bd7b9603',
    'uuid':'41b650ef846688193728ff7381eb6c1c',
    'secrect':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiZTIxNmY0OWMzZGQ2NmQwZTVjNzNiZDE4ZDI2MmJjOTciLCJkZXZpY2UiOiJtb2JpbGUifQ.gm0p9UKTfosbv4buUlD1u5d0-T2EtXNd5QQUe9ZlHe0',
    'app_id':'1',
    'plat_id':'2',
    'timestamp':'1560660339989',
    'uid':'7213561',
    'type':'0'
}
res_text = requests.get(get_url,verify=False).text
print(res_text)
#res = requests.post(url,data,verify=False)
#json_res = res.json()
#print(json.dumps(json_res,indent=4,ensure_ascii=False))