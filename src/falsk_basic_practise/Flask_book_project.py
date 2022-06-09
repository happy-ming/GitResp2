# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/7 11:01
from flask import Flask,render_template,request,flash,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
app.secret_key = 'mashibing'
'''
主要步骤：
    1、配置数据库
    2、添加模型
    3、添加数据
    4、使用模板显示数据库的查询的数据
    5、使用WTF显示表单
    6、实现相关的增删操作
'''
# 1、数据库的配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flask_book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

# 实现数据模型
# 作者模型
class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)

    books = db.relationship('Book',backref = 'author')

    def __repr__(self):
        return "Author: %s" % self.name

# 图书模型
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    author_id = db.Column(db.Integer,db.ForeignKey('authors.id'))

    def __repr__(self):
        return "Books: %s %s"%(self.name,self.author_id)

def create_author():
    author1 = Author(name='张三')
    author2 = Author(name='李四')
    author3 = Author(name='知音')

    db.session.add_all([author1,author2,author3])
    db.session.commit()
    create_book(author1,author2,author3)

def create_book(author1,author2,author3):
    book1 = Book(name='看戏',author_id = author1.id)
    book2 = Book(name='看官',author_id = author1.id)
    book3 = Book(name='位置',author_id = author2.id)
    book4 = Book(name='清酒', author_id=author2.id)
    book5 = Book(name='平级', author_id=author3.id)
    book6 = Book(name='林玖', author_id=author3.id)

    db.session.add_all([book1,book2,book3,book4,book5,book6])
    db.session.commit()

# 自定义表单类
class AuthorForm(FlaskForm):
    author = StringField('作者',validators=[DataRequired()])
    book = StringField('书籍',validators=[DataRequired()])
    submit = SubmitField('提交')

# 删除作者
@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    # 查询数据库，是否有该作者
    author = Author.query.get(author_id)

    if author:
        try:
            # 查询之后删除
            Book.query.filter_by(author_id=author.id).delete()
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            flash("删除作者失败")
            db.session.rollback()
    else:
        flash("不存在该作者")

    return redirect(url_for("index"))

# 删除书籍 ----> 网页中删除 ----> 点击需要发送书籍的ID给删除书籍的路由 ---> 路由需要接收参数
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    # 1、查询数据库，是否有该ID的书籍
    book = Book.query.get(book_id)

    # 2、如果有就删除
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash("删除失败")
            db.session.rollback()
    else:
        flash("书籍不存在")

    # redirect：重定向，需要传入网络/路由地址
    # url_for(“index”)：需要传入视图函数名，返回改视图函数对应的路由地址
    print(url_for("index"))
    return redirect(url_for("index"))


@app.route('/',methods = ['POST','GET'])
def index():
    # 实例化表单类
    author_form = AuthorForm()

    '''
    添加数据的逻辑验证
    '''
    # 调用WTF函数实现验证
    if author_form.validate_on_submit():
        # 获取数据
        author_name = author_form.author.data
        book_name = author_form.book.data

        # 判断作者是否存在
        author = Author.query.filter_by(name=author_name).first()
        if author:
            # 对于书籍进行判断
            book = Book.query.filter_by(name=book_name).first()
            if book:
                flash("已经存在同名的书籍")
            else:
                #  书籍不存在
                try:
                    new_book = Book(name=book_name,author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash("添加书籍失败")
                    db.session.rollback()
        else:
            # 作者不存在
            try:
                # 添加作者
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()
                # 添加书籍
                new_book = Book(name=book_name,author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                print(e)
                flash("添加作者失败")
                db.session.rollback()
    else:
        # 验证不通过
        if request.method == 'POST':
            flash('参数错误')

    # 查询所有的数据
    authors = Author.query.all()
    return render_template('book.html',authors=authors,form=author_form)

if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()
    # 创建数据
    create_author()
    app.run(debug=True)
