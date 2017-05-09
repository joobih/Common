#!/usr/bin/env python
# coding=utf-8

import re
import time
import json

"""
    判断ip是否是正确的ip地址True--是ip地址,False--不是ip地址
"""
def checkip(ip):  
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')  
    if p.match(ip):  
        return True  
    else:  
        return False

"""
    判断字符串是否是合理的电话号码
"""
def is_legal_phone(phone):
    prefix = [130,131,132,133,134,135,136,137,138,139,145,147,150,151,152,153,155,156,157,158,159,176,177,178,180,181,182,183,184,185,186,187,188,189]
    if len(phone) != 11: 
        return -1
    if phone.isdigit():
        if int(phone[:3]) in prefix:
            return 0
    else:
        return -2

"""
    将时间戳转换为日期字符串,时间戳为精确到秒的整数
"""
def revert_to_str(t,div = '-'):
    _t = time.localtime(t)
    str_t = time.strftime("%Y{}%m{}%d %H:%M:%S".format(div,div),_t)
    return str_t

"""
    将日期字符串转换为时间戳
"""
def revert_to_timestamp(date,div = '-'):
    _t = time.strptime(date,"%Y{}%m{}%d %H:%M:%S".format(div,div))
    print(_t)
    time_stamp = time.mktime(_t)
    return time_stamp

"""
    讲字符串中包含有\u1234 字符的替换为原来的中文
"""
def unicode_to_gbk(u_str):
    result = json.loads('{"str":"%s"}' % u_str)
    return result["str"]
