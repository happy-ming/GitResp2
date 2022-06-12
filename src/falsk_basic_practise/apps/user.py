# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/12 15:27
from flask import Blueprint,render_template

# url_prefix:必须在端口后面跟/user
# 参数static_folder可以指定静态文件的路径
# 参数template_folder参数可以设置模板的路径
bp = Blueprint('user',__name__,url_prefix='/user')

@bp.route('/list')
def user_list():
    return render_template('user.html')

