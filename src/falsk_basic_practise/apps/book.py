# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/12 15:23
from flask import Blueprint,render_template

bp = Blueprint('book',__name__,url_prefix='/book')

@bp.route('/list')
def book_list():
    return "图书管理"