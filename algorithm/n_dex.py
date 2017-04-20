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
#        print dex

    return dex

for i in range(100):
    get_n_dex(i,11)
