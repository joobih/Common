#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append("../db")
import pika
import json
#rabbitmq 生产者
class RQProduct():
    def __init__(self,queue,host="127.0.0.1",port=5672):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host,int(port)))
        self.channel = connection.channel()
        self.channel.queue_declare(queue = queue,durable = True)
        self.queue = queue

    def product(self,message):
        try:
            if isinstance(message,dict):
                message = json.dumps(message)
            self.channel.basic_publish(exchange = '',routing_key = self.queue,body = message)
        except Exception as e:
            print("product occure a exception:{};msg:{}".format(e,message))
            return

    def close(self):
        self.channel.close()


