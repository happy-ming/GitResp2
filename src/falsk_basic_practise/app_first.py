# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/12 15:58
from flask import Flask
from apps.book import bp as book_bp
from apps.user import bp as user_bp

app = Flask(__name__)
app.register_blueprint(book_bp)
app.register_blueprint(user_bp)

@app.route('/')
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)
