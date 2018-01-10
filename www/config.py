# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:45:50 2018

Day 6 - 编写配置文件

@author: Harbinger
"""

"""
把所有的配置读取到config.py文件中
"""

import config_default

class Dict(dict):
    """
    Simple dict but support access as x.y style
    """
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has not attribute '%s'" % key)
    
    def __setattr__(self, key, value):
        self[key] = value
    
def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D

configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)