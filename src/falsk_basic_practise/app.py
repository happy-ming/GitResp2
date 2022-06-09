from flask import Flask
# - B/S：浏览器/服务器架构（客户端需要更新才行）
# - C/S：客户端/服务器架构（刷新页面即可更新）（可能会成为主流）
from flask import Flask,render_template,request,flash

# 创建应用实例
app = Flask(__name__)
app.secret_key = 'itheima'

# 视图函数（路由）
# 默认支持get请求，如果需要添加，需要使用methods指定
@app.route('/',methods = ["GET","POST"])
def index():
    # 返回字符串
    return "<h1>Hello world</h1>"
    # 返回模板
    # return render_template('index.html')

# 创建网页模板，传入数据 ----- jinja2模板
@app.route('/back',methods = ['POST','GET'])
def back_url():
    # 传入网址
    url_str = 'www.baidu.com'
    # 传入列表
    my_list = [1,3,5,7,9]
    # 传入字典
    my_dict = {
        "name":"张三",
        "url":"www.baidu.com"
    }
    return render_template('index.html',
                           url_str = url_str,my_list = my_list,
                           my_dict=my_dict)

# 使用<>传参，然后添加数据类型
@app.route('/order/<int:order_id>')
def get_order_id(order_id):
    # 需要在视图（）后填入参数，之后就可以使用
    return "order_id: %s" % order_id

# 表单处理
'''
实现表单的逻辑处理
1、路由需要有POST和GET请求 --- 判断请求方式
2、获取请求的参数
3、判断参数是否填写 & 密码是否相同
4、判断没得问题，则登录成功
'''
# 给模板传递消息--- 在前端页面输出消息
# flash --- 需要对内容进行加密，使用secret_key，做加密消息的混淆
# 模板中需要去遍历消息
@app.route('/login',methods = ["GET","POST"])
def login():
    # request 请求对象 --- 获取请求方式，数据
    # 1、判断请求方式
    if request.method == 'POST':
        # 2、获取请求的参数
        username= request.form.get('username')
        password = request.form.get('password')
        bypassword = request.form.get('bypassword')

        if not all([username,password,bypassword]):
            # print("参数不完整")
            flash("参数不完整")
        elif password != bypassword:
            # print("两次密码不一致")
            flash("两次密码不一致")
        else:
            return 'success'
    return render_template('login.html')

# 启动实施（只在当前模块运行）
if __name__ == '__main__':
    # run函数参数：
    '''
    debug ---- 代码更新是否自动启动，默认值：False
    threaded --- 是否开启多线程,默认值：False    
    port ---- 指定端口,默认值：5000
    host ---- 指定主机（设置0.0.0.0可以通过本地IP访问）,默认值：127.0.0.1
    '''
    app.run(debug=True)