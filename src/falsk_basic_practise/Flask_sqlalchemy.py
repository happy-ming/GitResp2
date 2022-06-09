# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/6 22:50
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,or_,not_

app = Flask(__name__)
# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flask_sql_demo'
# 动态追踪修改设置，如未设置只会提示警告，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

# 定义数据库模型  需要继承db.Model
class Role(db.Model):
    # 表名
    __tablename__ = 'roles'
    # db.Column表示一个字段
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)

    # 在一的一方，写关联
    # 与user模型发生关联，增加一个user属性
    # backref = 'role'表示role是User要用的属性
    user = db.relationship('User',backref = 'role')

    # repr()方法显示一个可读字符串
    def __repr__(self):
        return '<Role: %s %s>'% (self.name,self.id)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    email = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(32))
    # db.ForeignKey('roles.id')表示外键
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    # User希望有role属性，但是这个属性的定义，需要在另一个模型中定义backref = 'role'

    # repr()方法显示一个可读字符串
    def __repr__(self):
        return '<User: %s %s %s %s>' % (self.name, self.id,self.email,self.password)

def create_role():
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()

    # 再次插入一条数据
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()
    create_user(ro1,ro2)

def create_user(ro1,ro2):
    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@126.com', password='987654', role_id=ro1.id)
    us6 = User(name='wu', email='wu@163.com', password='456789', role_id=ro1.id)
    us7 = User(name='qian', email='qian@126.com', password='987654', role_id=ro2.id)
    us8 = User(name='liu', email='liu@163.com', password='456789', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4,us5,us6,us7,us8])
    db.session.commit()

def check_data():
    # 查询名字为wang的所有人
    User.query.filter_by(name='wang').all()
    # 返回第一个对象
    User.query.first()
    # 模糊查询,返回名字结尾字符为g的所有数据
    User.query.filter(User.name.endswith('g')).all()
    # 逻辑查询and
    User.query.filter(and_(User.name!='wang',User.email.endswith('163.com')).all())
    # 逻辑查询or
    User.query.filter(or_(User.name!='wang',User.email.endswith('163.com')).all())
    # 取反 not
    User.query.filter(not_(User.name!='wang').all())
    # 更新数据
    User.query.filter_by(name='zhang').update({'name':'li'})
# filter: 对象.属性 ==
# filter_by： 属性 =
# filter功能更强大，可以实现更多的一些查询，支持比较运算符

@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()
    # 创建数据
    create_role()
    app.run(debug=True)
