#!/usr/bin/env python
# coding=utf-8

"""
    输入一个10进制数和N，输出N进制数表示法 1<=N<=36
"""
g_map = {}
for i in xrange(10):
    g_map[i] = str(i)

for i in xrange(26):
    a = chr(i + ord('A'))
    g_map[i+10] = a

#键值互换
g_map_rev = dict((value,key) for key,value in g_map.iteritems())

"""
    10 进制数i转换N进制数 输出字符串表示i的N进制数
"""
def get_n_dex(i, N):
    #保证传入参数为整数
    if not isinstance(N,int) or not isinstance(i,int):
        return ""
    #10进制数直接返回
    if N == 10:
        return i
    dex = ""
    while(i):
        index = i % N
        i = i / N
        dex = "{}{}".format(g_map[index],dex)
    return dex

for i in range(100):
    get_n_dex(i,11)

"""
    将一个N进制表达的数dex转换为10进制数
"""
def get_ten_dex(dex, N):
    if not isinstance(N,int) or not isinstance(dex,(int,str)):
        return ""
    if N == 10:
        return int(dex)
    num = 0
    i = 0
    while dex:
        last_ = dex[-1:]
        a = g_map_rev[last_]
        if a >= N:
            print "{}进制数里面不应该含有{}".format(N,last_)
            return None
        dex = dex[:-1]
        num += g_map_rev[last_] * (N ** i)
        i += 1
    return num

dex = "1F"
print get_ten_dex(dex,16)
