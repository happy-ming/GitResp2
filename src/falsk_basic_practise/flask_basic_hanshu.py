# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/10 14:09
from flask import Flask,make_response,request,redirect,url_for,abort

app = Flask(__name__)

# 获取request请求值
app.route('/request/<path:info>',methods=['POST','GET'])
def request_url(info):
    # 完整的请求URL
    # return request.url
    '''
        url：127.0.0.1:5000/request/abc/def?username=xiaoming&pwd=123
    	网页返回值：http://127.0.0.1:5000/request/abc/def?username=xiaoming&pwd=123
    '''
    # 去掉GET参数的URL  网页返回值：http://127.0.0.1:5000/request/abc/def
    # return request.base_url
    # 只有主机和端口的URL 网页返回值：http://127.0.0.1:5000/
    # return request.host_url
    # 装饰器中写的路由地址 网页返回值：/request/abc/def
    # return request.path
    # 请求方法类型
    # return request.method
    # 远程地址
    # return request.remote_addr
    '''
    网页返回值：127.0.0.1:5000
    '''
    # 获取url参数
    # return request.args.get('username')
    # return request.args.get('pwd')
    # return str(request.args)
    # 获取headers信息
    return request.headers.get('User-Agent')

# 响应的构造
@app.route('/response/')
def response():
    # 构造一个404状态码,默认是200
    # return 'not found',404
    # 自定义构造一个响应，然后返回200，构造也可以指定状态码404
    return make_response('我是通过函数构造的响应',404)

# 重定向
@app.route('/old/')
def old():
    # 根据视图函数找到路由,指向方法：<url_for>中的参数'new'指向的是<函数名>
    return redirect(url_for('new',username='xiaoxiang'))
@app.route('/new/<username>')
def new(username):
    return '我是'+username

#终止abort
@app.route('/login/')
def login():
    # return '欢迎登录'
    # 此处使用abort可以主动抛出异常
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)