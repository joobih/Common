#!/usr/bin/env python
# coding=utf-8
import os
import os.path
rootdir = "/opt"                                   # 指明被遍历的文件夹

def list_dir(rootdir):
    if not os.path.isdir(rootdir):
        return
    l = os.listdir(rootdir)
    for i in l:
        sub = os.path.join(rootdir,i)
        if os.path.isdir(sub):
            print sub+"/"
        else:
            print sub
        list_dir(sub)

list_dir(rootdir)

