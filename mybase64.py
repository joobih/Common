#!/usr/bin/env python
# coding=utf-8

import base64

"""
    字符串和base64编码的互相转换
"""
def b64encode(s):
    try:
        encode_str = base64.b64encode(s)
        return encode_str
    except Exception as exp:
        print("b64encode occure a Exception:{}".format(exp))
        return None

#将b64 通过base64解码
def b64decode(b64):
    try:
        decode_str = base64.b64decode(b64)
        return decode_str
    except Exception as exp:
        print("b64decode occure a Exception:{}".format(exp))
        return None

#if __name__ == "__main__":
#    a = "测试代码"
#    c = b64encode(a)
#    d = b64decode(c)
#    print(c)
#    print(d)
