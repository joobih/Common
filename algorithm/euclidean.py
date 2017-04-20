#!/usr/bin/env python
# coding=utf-8

"""
    欧几里得辗转相除法求最大公约数
"""
def gcd(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        return None
    if a%b == 0:
        return b
    r = a%b
    return gcd(b,r)

#print 10%20
print gcd(-20,3)
