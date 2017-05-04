#!/usr/bin/env python
# coding=utf-8

import cStringIO
from PIL import Image
import base64

"""
    parser_pic:解析图片，获取图片的长宽并且按照比例缩小 默认0表示不缩小 取值(0,1]
        b64_pics:经过base64编码的图片数据
        smaller:图片缩小比例，取值范围为(0,1]
"""
def paser_pic(b64_pics,smaller = 1):
    string_data = cStringIO.StringIO(b64_pics)
    im = Image.open(string_data)
    width,height = im.size
    if smaller != 1:
        small_img = im.resize((int(width*smaller), int(height*smaller)),Image.ANTIALIAS)
        b64_small_pic = base64.b64encode(small_img.getvalue())
        return (width,height,b64_small_pic)
    return (width,height,b64_pics)


