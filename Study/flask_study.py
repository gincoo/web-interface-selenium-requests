#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from flask import Flask
from flask import request
import json
from Util.handle_json import write_value,read_json
app = Flask(__name__)

@app.route('/')
def Home():
    data = json.dumps({
        "username":"Mushishi_xu",
        "password":"111111"
    })

    return data

@app.route('/passport/user/login',methods=['GET'])
def Login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username and password:

        data = json.dumps({
            "username":username,
            "password":password,
            "code":"200",
            "message":"登陆成功",
            "info":"www.baidu.com"
        })
    else:
        data = json.dumps({
            "message":"请传递参数"
        })

    return data

@app.route('/mock',methods=['POST'])
def mock_data():
    '''
    模拟数据
    imooc.com
    {
        "key":"value"
    }
    '''
    return_data = {
        "message":None
    }
    mock_data = read_json()
    url = request.form.get("url")
    data = request.form.get("data")   
    try:
        data = json.loads(data)
        mock_data[url] = data
    except Exception:
        return_data['message'] = "你传递的数据不是json格式"
        return json.dumps(return_data)
    try:
        print("--->",mock_data)
        write_value(mock_data,file_name="/Config/user_data.json")
    except Exception:
        return_data['message'] = "写入数据失败"
        json.dumps(return_data)
    return_data['message'] = "写入成功"
    return json.dumps(return_data)
       

@app.route('/passport/user/post_login',methods=['POST'])
def post_login():
    request_method = request.method
    if request_method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")      
        data = json.dumps({
            "username":username,
            "password":password,
            "code":"200",
            "message":"登陆成功",
            "info":"www.Imooc.com"
        })
        #return data
    else:
        data = json.dumps({
            "message":"请求不合法"
        })
    return data

#https://www.imooc.com/passport/user/login?username=Mushishi_xu@163.com&password=111111

if __name__ == "__main__":
    app.run(debug=True)