#!/usr/bin/env python
# coding=utf-8

import math

"""
    求等差数列的和
"""
def sequence_sum(an,d,a1):
    n = (int((an-a1)/d) + 1)
    return ((a1+an)*n) >> 1

"""
    给一个数num，求0-num之间约数的和
"""
def div_num(num):
    if num < 1:
        return 0
    i = 1
    sum = 0
    while(i<=num):
        d = int(int(num / int(num/i)) - i) + 1
        if d == 1:
            sum += i*int(num/i)
            i += 1
        elif d>1:
            an = int(num/int(num/i))
            a1 = i
            print("an,a1:%s,%s" % (an,a1)) 
            sum += sequence_sum(an, 1, a1) * int(num/i)
            i += d
        else:
            print("false")
            return 0
        if sum>1000000000000:
            sum %= 1000000000000        
#        print(i)
    return sum

print(sequence_sum(100, 1, 1))        
      
i = 1000000000000
print(div_num(i))
