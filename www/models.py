# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 10:01:12 2017

Day 4 - 编写Model：把Web App需要的3个表用Model表示出来

@author: Harbinger
"""

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

"""
1 给Field增加一个default参数可以让ORM自己填入缺省值，并且缺省值可以作为函数对象传入，在调用save()时自动计算
2 创建时间create_at的缺省值是函数time.time，可以自动设置当前日期和时间
3 日期和时间用float类型存储，而不采用datetime类型，这样不必时区和时区转换的问题，排序和显示(用str)都非常简单
"""

class User(Model):
    __table__ = 'users'
    
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    create_at = FloatField(default=time.time)
    
class Blog(Model):
    __table__ = 'blogs'
    
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    create_at = FloatField(default=time.time)
    
class Comment(Model):
    __table__ = 'comments'
    
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    create_at = FloatField(default=time.time)