# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 10:58:48 2018

Day 9 - 编写API

@author: Harbinger
"""

"""
JSON API definition
"""

import json, logging, inspect, functools

class APIError(Exception):
    """
    the base APIError which contains error(required), data(optional) and message(optional)
    """
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message
        
class APIValueError(APIError):
    """
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    """
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)
        
class APIResourceNotFoundError(APIError):
    """
    Indicate the resource was not found. The data specifies the resource name.
    """
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)

class APIPermssionError(APIError):
    """
    Indicate the api has no permission
    """
    def __init__(self, message=''):
        super(APIPermssionError,self).__init__('permission:forbidden', 'permission', message)