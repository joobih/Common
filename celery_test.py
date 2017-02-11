#!/usr/bin/env python
# coding=utf-8

import time
from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//',backend='redis://localhost')

@app.task
def add(x, y):
    time.sleep(5)
    return x + y

