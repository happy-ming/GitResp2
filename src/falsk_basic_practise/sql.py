# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/7 9:51
'''
from Flask_sqlalchemy import *
添加数据

role = Role(name='admin')
db.session.add(role)
db.session.commit()

user = User(name='zhangsan',role_id = user_id)
db.session.add(user)
db.session.commit()

修改数据
user.name = 'lisi'
db.session.commit()

删除数据
db.session.delete(user)
db.session.commit()

常用的SQLAlchemy的查询过滤器
filter()	把过滤器添加到原查询上，返回一个新查询
filter_by()	把等值过滤器添加到原查询上，返回一个新查询
limit	使用指定的值限定原查询返回的结果
offset()	偏移原查询返回的结果，返回一个新查询
order_by()	根据指定条件对原查询结果进行排序，返回一个新查询
group_by()	根据指定条件对原查询结果进行分组，返回一个新查询

常用的SQLAlchemy查询执行器
all()	以列表形式返回查询的所有结果
first()	返回查询的第一个结果，如果未查到，返回None
first_or_404()	返回查询的第一个结果，如果未查到，返回404
get()	返回指定主键对应的行，如不存在，返回None
get_or_404()	返回指定主键对应的行，如不存在，返回404
count()	返回查询结果的数量
paginate()	返回一个Paginate对象，它包含指定范围内的结果

'''

