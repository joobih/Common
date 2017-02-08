#!/usr/bin/env python
# coding=utf-8

import re


"""
    判断ip是否是正确的ip地址True--是ip地址,False--不是ip地址
"""
def checkip(ip):  
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')  
    if p.match(ip):  
        return True  
    else:  
        return False 
