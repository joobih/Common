#!/usr/bin/env python
# coding=utf-8

"""
    计算十进制数N中的二进制表达法中1的个数
"""
def binary(N):
    count = 0
    n = N
    while(n):
        count += 1
        n = n&(n-1)
    return count

print binary(10)
