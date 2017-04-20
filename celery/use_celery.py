#!/usr/bin/env python
# coding=utf-8
from celery_test import add

result = add.delay(4,4)
print result.get()
