#!/usr/bin/env python
# coding=utf-8

import sys
import base64
from PIL import Image

"""
    parser_pic:解析图片，获取图片的长宽并且按照比例缩小 默认0表示不缩小 取值(0,1]
        b64_pics:经过base64编码的图片数据
        smaller:图片缩小比例，取值范围为(0,1]
"""
def paser_pic(b64_pics, save_path, smaller=1):
    if sys.version < '3':
        from cStringIO import StringIO
        b64_pics = base64.b64decode(b64_pics)
        string_data = StringIO(b64_pics)
        im = Image.open(string_data)
        width, height = im.size
        if smaller != 1:
            small_img = im.resize((int(width*smaller), int(height*smaller)), Image.ANTIALIAS)
            small_img.save(save_path["small_path"])
        im.save(save_path["big_path"])
        return (width, height)
    else:
        from io import BytesIO
        b64_pics = base64.b64decode(b64_pics)
        bytes_data = BytesIO(b64_pics)
        print(bytes_data, type(bytes_data))
        im = Image.open(bytes_data)
        width, height = im.size
        if smaller != 1:
            small_img = im.resize((int(width*smaller), int(height*smaller)), Image.ANTIALIAS)
            small_img.save(save_path["small_path"])
        im.save(save_path["big_path"])
        return (width, height)

#f = "a.jpg"
#b = open(f,"rb")
#c = b.read()
#pic = base64.b64encode(c)
#save_path = {"small_path":"s.jpg","big_path":"b.jpg"}
#print(paser_pic(pic,save_path,0.5))
