#!/usr/bin/env python
# coding=utf-8

import base64

"""
    字符串和base64编码的互相转换
"""
class myBase64():
    #将字符串s 经过base64编码
    def b64encode(self,s):
        try:
            b64 = base64.b64encode(s)
            print b64,type(b64)
            return b64
        except Exception,e:
            print "b64encode occure a Exception:{}".format(e)
            return None

    #将b64 通过base64解码
    def b64decode(self,b64):
        try:
            s = base64.b64decode(b64)
            print s,type(s)
            return s
        except Exception,e:
            print "b64decode occure a Exception:{}".format(e)
            return None

if __name__ == "__main__":
    b = myBase64()
    a = "测试代码"
    c = b.b64encode(a)
    d = b.b64decode(c)
    print c
    print d
