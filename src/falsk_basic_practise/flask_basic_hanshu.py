# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/10 14:09
from flask import Flask,make_response,request,redirect,url_for,abort,render_template

app = Flask(__name__)

# 当配置过多，需要模块来加载
# app.config.from_pyfile('setting.py',silent=True)

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
    # http://127.0.0.1:5000/request/abc/def?username=xiaoming&pwd=123
    # return request.args.get('username')
    # return request.args.get('pwd')
    # return str(request.args)
    # 获取headers信息
    return request.headers.get('User-Agent')

# 响应的构造
@app.route('/response/')
# 当访问一个结尾不带斜线的URL：/response，会被重定向到带斜线的URL：/response/上去。
# 但是当我们在定义response的url的时候，如果在末尾没有加上斜杠，但是在访问的时候又加上了斜杠，
# 这时候就会抛出一个404错误页面了：
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

# 重定向
'''
重定向是通过flask.redirect(location,code=302)这个函数来实现的，
location表示需要重定向到的URL，应该配合之前讲的url_for()函数来使用，
code表示采用哪个重定向，默认是302也即暂时性重定向，可以修改成301来实现永久性重定向。
'''
@app.route('/login/',methods=['POST','GET'])
def logins():
    return 'login page'

@app.route('/profile',methods=['POST','GET'])
def profile():
    name = request.args.get('name')

    if not name:
        # 如果没有name，说明没有登录，重定向到登录页面
        return redirect(url_for('login'))
    else:
        return name

@app.route('/',methods=['POST','GET'])
def jinjia2_test():
    variable = 12
    return render_template('jinjia2测试器.html',variable=variable)


# 类似于python中的函数，宏的作用就是在模板中重复利用代码，避免代码冗余。
# Jinja2支持宏，还可以导入宏，需要在多处重复使用的模板代码片段可以写入单独的文件，
# 再包含在所有模板中，以避免重复。
context={
    'username': '老萝卜',
    'age': 18
}
@app.route("/macrol/")
def demo_marco2():
    return render_template('macro2.html', **context)

if __name__ == '__main__':
    app.run(debug=True)