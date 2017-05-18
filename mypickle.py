#!/usr/bin/env python
# coding=utf-8

import cPickle as pickle

"""
    将一个Python对象序列化和反序列化
    可以将一个Python对象序列化后的字符串经过base64编码后保存起来(存放到redis或则其他数据库中),
    当下次需要时提取出来base64解码再反序列化为Python对象
"""
class MyPickle(object):

    #将一个Python对象序列化为字符串
    def dumps(self, obj):
        try:
            dump_str = pickle.dumps(obj)
            return dump_str
        except Exception as exp:
            print("dumps occure a Exception:{}".format(exp))
            return None

    #将字符串反序列化为Python对象
    def loads(self, source_str):
        try:
            obj = pickle.loads(source_str)
            return obj
        except Exception as exp:
            print("loads occure a Exception:{}".format(exp))
            return None

if __name__ == "__main__":
    from mybase64 import myBase64
    p = MyPickle()
    l = [1, 2, 3, 4, "sraf"]
    import requests
#    a = requests.session()
    s = p.dumps(l)
    c = myBase64()
    d = c.b64encode(s)
    e = c.b64decode(d)
#    c_str = cy.encrypt(e)
    f = p.loads(e)
    print(f)
    p.loads(s)
