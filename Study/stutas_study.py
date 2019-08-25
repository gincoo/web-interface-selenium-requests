#coding=utf-8
import requests

# 如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，我们可以通过 Response.raise_for_status() 来抛出异常：

url = 'http://www.imooc.com/order/test/ssssss'
# url = 'http://www.baidu.com'
#res = requests.get(url).status_code
res = requests.get(url).raise_for_status()
#res = requests.codes.ok



print(res)