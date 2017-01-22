#!/usr/bin/env python
# coding=utf-8

import time

"""
    通过身份证号计算年龄 [23,9,2]--23岁,9个月2天
"""
def get_age_from_idcard(id_no):
    str_bir_day = id_no[12:14]
    str_bir_mon = id_no[10:12]
    str_bir_year = id_no[6:10]
#    bir_day = string.atoi(str_bir_day)
    bir_day = int(str_bir_day)
#    bir_mon = string.atoi(str_bir_mon)
    bir_mon = int(str_bir_mon)
#    bir_year = string.atoi(str_bir_year)
    bir_year = int(str_bir_year)
    current_date = time.gmtime()
    day = current_date[2] - bir_day
    mon = current_date[1] - bir_mon
    year = current_date[0] - bir_year
    if day < 0:
        day = day + 30
        mon = mon -1
    if mon < 0:
        mon = mon + 12
        year = year -1
    return (year, mon, day)


"""
    通过身份证号获取性别 -1---身份证号不正确;1---表示男;2---表示女
"""
def get_gender_from_idcard(id_no):
    if len(id_no) != 18:
        return -1
    id16_17 = id_no[16:17]
    if int(id16_17) & 0x01 != 0:
        return 1
    return 2

dcard = "532015192304207733"
print get_age_from_idcard(dcard)
print get_gender_from_idcard(dcard)
