#!/usr/bin/env python
# coding=utf-8

from rb_product import RQProduct

p = RQProduct("url_queues2")
def send(n):
    for i in range(n):
        msg = {"data":"msg :{}".format(i)}
        p.product(msg)
        print msg

send(20)

