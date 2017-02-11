#!/usr/bin/env python
# coding=utf-8

#import time
from celery import Celery
import requests
from headers import HEADERS

app = Celery('tasks', broker='amqp://guest@localhost//',backend='redis://localhost')

@app.task
def get_url(url,cookies = None,use_proxy = False):
    try:
        r = requests.get(url,headers = HEADERS,cookies = cookies)
        html = r.content
        return html
    except Exception,e:
        print e
        return ""
