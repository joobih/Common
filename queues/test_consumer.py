#!/usr/bin/env python
# coding=utf-8

import time
from rb_consumer import RQConsumer,multi_consumer,TestConsumer

class test(RQConsumer):

    def data_process(self,data):
        print data
        time.sleep(2)

if __name__ == "__main__":
    multi_consumer(test,"url_queues2","127.0.0.1",5672)
#    TestConsumer(test,"url_queues2","127.0.0.1",5672)
