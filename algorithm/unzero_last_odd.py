#!/usr/bin/env python
# coding=utf-8
def leave_ten(ten):
    t = ten
    while(t%10==0):
        t = int(t/10)
    return t

def ten(L):
    i = 0
    l_even = []
    l_five = []
    l_odd = []
    while(i<len(L)):
        t = leave_ten(L[i])
        L[i] = t
        if L[i]%10 not in(1,3,5,7,9):
            l_even.append(L[i])
        if L[i]%10 == 5:
            l_five.append(L[i])
        if L[i]%10 in (1,3,7,9):
            l_odd.append(L[i])
        i += 1
    if l_even != [] and l_five == []:
        return 0
    if l_even == []:
        return 1
    
    if len(l_even)<len(l_five):
        min_len = len(l_even)
    else:
        min_len = len(l_five)
    L1=[]
    i = 0
    while i< min_len:
        L1.append(l_five[i]*l_even[i])
        i += 1
    if min_len == len(l_even):
        L1[min_len:min_len] = l_five[min_len:len(l_five)]
    else:
        L1[min_len:min_len] = l_even[min_len:len(l_even)]
    
    return ten(L1)

L = []
for i in range(1,1000):
    L.append(i)
L = [2,3,4,5,6,7,9,10,100,5,15,5]
print (ten(L))
