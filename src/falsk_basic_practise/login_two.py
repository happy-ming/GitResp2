# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/6 14:56
from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)
app.secret_key = 'itheima'
# 使用WTForms  表单验证插件
'''
wtforms中的Field类主要用于数据验证和字段渲染(生成html)：
    StringField    字符串字段，生成input要求字符串
    PasswordField　　密码字段，自动将输入转化为小黑点
    TextAreaField    多行文本字段
    DateField　　日期字段，格式要求为datetime.date一样
    IntergerField　　整型字段，格式要求是整数
    FloatField　　文本字段，值是浮点数
    BooleanField　　复选框，值为True或者False
    RadioField　　一组单选框
    SelectField　　下拉列表，需要注意一下的是choices参数确定了下拉选项，但是和HTML中的<select> 标签一样。
    MultipleSelectField　　多选字段，可选多个值的下拉列表

其中字段的参数有：
    label：字段别名，在页面中可以通过字段.label展示；
    validators：验证规则列表；
    filters：过氯器列表，用于对提交数据进行过滤；
    description：描述信息，通常用于生成帮助信息；
    id：表示在form类定义时候字段的位置，通常你不需要定义它，默认会按照定义的先后顺序排序。
    default：默认值
    widget：html插件，通过该插件可以覆盖默认的插件，更多通过用户自定义；
    render_kw：自定义html属性；
    choices：复选类型的选项 ;
    
常用的验证函数：
    DataRequired    确保字段中有值
    EqualTo     比较两个字段的值
    Length      验证输入的字符串长度
    NumberRange   验证输入的值在数字范围内
    URL         验证URL
    AnyOf       验证输入值在可选列表中
    NoneOf      验证输入值不在可选列表中
'''

# 首先自定义表单类
class LoginForm(FlaskForm):           # 验证        验证函数可以写多个
    username = StringField('用户名：',validators=[DataRequired()])
    password = PasswordField('密码：',validators=[DataRequired()])     # 比较    密码          错误时
    bypassword = PasswordField('确认密码：',validators=[DataRequired(),EqualTo('password','密码不一致')])
    submit = SubmitField('提交')

@app.route('/form_wtf',methods = ['POST','GET'])
def login():
    form = LoginForm()
    # request 请求对象 --- 获取请求方式，数据
    # 1、判断请求方式
    if request.method == 'POST':
        # 2、获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        bypassword = request.form.get('bypassword')

        # 3、验证参数，wtf可以一句实现所有的校验
        #  CSRF 跨站域请求伪造
        if form.validate_on_submit():
            print(username,password)
            return 'success'
        else:
            flash("参数有误！")
    render_template('login_two.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)

