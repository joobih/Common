#!/usr/bin/env python
# coding=utf-8

def singleton(cls):
    instance = {}
    def _singleton(*args, **kw):
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance
    return _singleton
