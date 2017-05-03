#!/usr/bin/env python
# coding=utf-8

import time
from rb_consumer import RQConsumer,multi_consumer,TestConsumer

class test(RQConsumer):

    def __init__(self,rq_queue,rq_host="127.0.0.1",rq_port=5672,kwags={}):
        self.datas = []
        RQConsumer.__init__(self,rq_queue,rq_host,rq_port,kwags)

    def data_process(self,data):
        print data
        time.sleep(2)
#        if len(self.datas) < 10:
#            self.datas.append(data)
#        else:            
#            print self.datas
#            self.datas = []
#            time.sleep(2)

if __name__ == "__main__":
#    multi_consumer(test,"url_queues2","127.0.0.1",5672)
    TestConsumer(test,"url_queues2","127.0.0.1",5672)
