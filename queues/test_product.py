#!/usr/bin/env python
# coding=utf-8

#import asyncio
#from aiohttp import ClientSession
from rb_product import RQProduct

p = RQProduct("url_queues2")
data = {"urls":[]}
def send(n):
    for i in range(n):
#        msg = {"data":"msg :{}".format(i)}
#        data = {"urls":[]}
        data["urls"].append("msg:{}".format(i))
    p.product(data)
    print(data)

send(20)

