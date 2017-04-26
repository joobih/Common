#!/usr/bin/env python
# coding=utf-8

import os
import pika
import multiprocessing
import json

"""
    rabbitmq 消费者,接受指定topic中的数据，子类通过继承它才能够使用，只需实现data_process函数进行数据的处理
"""
class RQConsumer(object):
    def __init__(self,rq_queue,rq_host="127.0.0.1",rq_port=5672,kwags={}):
        try:
            #连接rabbit
            connection = pika.BlockingConnection(pika.ConnectionParameters(rq_host,int(rq_port)))
            self.channel = connection.channel()
            self.channel.basic_qos(prefetch_count = 1)
            #如果没有队列就创建
            self.channel.queue_declare(queue = rq_queue,durable = True)
            self.queue = rq_queue
        except Exception,e:
            print "RQConsumer __init__ occure a Exception:{}".format(e)
            return

    """
        data 为一个rabbitmq队列中的消息，子类通过继承该函数自行处理该数据
    """
    def data_process(self,data):
        raise NotImplementedError()

    #接收消息的回调函数
    def callback(self,ch,method,properties,body):
        try:
            print("Process is running at pid %s;data:%s" % (os.getpid(),body))
            data = json.loads(body)
            self.spider(data)
            #消息处理完成可以通知到队列完成了处理
            ch.basic_ack(delivery_tag = method.delivery_tag)
            #在此处理每条消息

        except Exception,e:
            print "occure a Exception:{}".format(e)
    
    def start(self,_call_back):
        print "start consumer..."
        self.channel.basic_consume(_call_back,queue = self.queue)
        self.channel.start_consuming()

"""
    单进程队列接收并处理函数
    param:
        Consumer: 自己实现了数据处理函数data_process的rabbitmq消费者类
        rq_host: rabbitmq的主机名
        rq_port: rabbitmq的端口
        rq_queue: rabbitmq的消息队列名
        kwags: 可变参数
"""
def TestConsumer(Consumer,rq_queue,rq_host,rq_port,kwags):
    consumer = Consumer(rq_queue,rq_host,rq_port,kwags)
    consumer.start(consumer.callback)

"""
    多进程队列接收并处理函数
    param:
        Consumer: 自己实现了数据处理函数data_process的rabbitmq消费者类
        rq_host: rabbitmq的主机名
        rq_port: rabbitmq的端口
        rq_queue: rabbitmq的消息队列名
        process_num: 开启的进程数量，默认以机器支持的cpu个数为参数
        kwags: 可变参数
"""
def multi_consumer(Consumer,rq_host,rq_port,rq_queue,process_num = 0,kwags = {}):
    try:
        p = multiprocessing.cpu_count()
        if process_num != 0:
            p = process_num
        pool = multiprocessing.Pool(processes = p)
        for i in xrange(p):
            pool.apply_async(TestConsumer,(Consumer,rq_host,rq_port,rq_queue,kwags))
        pool.close()
        pool.join()
        print "done"
    except Exception,e:
        print "Caught KeyboardInterrupt, terminating workers",e
        return
