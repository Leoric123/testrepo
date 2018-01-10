# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:34:21 2018

Day 6 - 编写配置文件

@author: Harbinger
"""

"""
开发环境的默认配置文件
"""

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'IchbinWoody123',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}