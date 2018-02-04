# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:49:47 2018

Day 14 - 编写test_db.py

@author: Harbinger
"""

from models import User, Blog, Comment
from transwarp import db

db.create_engine(user='www-data', password='www-data', database='awesome')
u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
u.insert()
print('new user id:', u.id)

u1 = User.find_first('where email=?', 'test@example.com')
print('find user\'s name:', u1.name)
u1.delete()

u2 = User.find_first('where email=?', 'test@example.com')
print('find user:', u2)