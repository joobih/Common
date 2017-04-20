#!/usr/bin/env python
# coding=utf-8

import re  
import hashlib
import uuid
import random
from random import randint
from urlparse import urlparse
from datetime import datetime

"""
    将url字符串进行检查,返回是否是合法的url字符串,True代表是,False代表否
"""
def is_normal_url(url):      
    if re.match(r'^https?:/{2}\w.+$', url):  
        return True
    else:  
        return False

"""
    使用正则表达式获取字符串content中包含的所有的url
"""
def paser_urls(content):
    urlParttern = r'https?://[\w\-\/]+[\.[\w\-\/]+]*'
    pattern = re.compile(urlParttern)
    urls = re.findall(pattern,content,0)
    return urls

content = """
    http://baidu.com https://www.baidu.com/a.jpg  
"""
urls = paser_urls(content)
print urls

"""
    将url进行分解,返回该url使用的协议,主机名,端口号,路径
"""
def analysis_url(url):
    u = urlparse(url)
    scheme = u.scheme
    hostname = u.hostname
    port = u.port
    path = u.path
    result = {
        "scheme":scheme,
        "hostname":hostname,
        "port":port,
        "path":path
    }
    return result


"""
    根据file_type生成一个唯一的文件名
"""
def get_file_name(file_type):
    uid = uuid.uuid4()
    t = datetime.now()
    t = str(t)
    t = t[:19]
    file_name = t + "_" + str(uid)
    file_name = file_name.replace(" ","_").replace(".","_").replace(":","_").replace("-","_") + ".{type_}".format(type_ = file_type)
    return file_name


"""
    将data字符串进行md5并返回
"""
def get_md5(data):
    m2 = hashlib.md5()
    m2.update(data)
    md5_str = m2.hexdigest()
    return md5_str

"""
    随机获取从[start -> end)之间的n个不相同的整数,若n比该区间大,就返回该区间打乱顺序的随机数
"""
def get_randints(start,end,n):
    data = [i for i in range(start,end)]
    random.shuffle(data)
    if n > end - start:
        return data
    else:
        return data[:n]

