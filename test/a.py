#encoding=utf-8
from multiprocessing import Process,Queue,Pool
import multiprocessing
import os, time, random

# 写数据进程执行的代码:
def write(q,lock):
#    lock.acquire() #加上锁
#    for value in ['A', 'B', 'C']:
    for value in range(0,10):
        lock.acquire() #加上锁
        print 'Put %d to queue...' % value        
        q.put(value)      
        lock.release() #释放锁  

# 读数据进程执行的代码:
def read(name,q,lock):
    while True:
        lock.acquire()
        if not q.empty():
            value = q.get(False)
            print 'process:{} .Get {} from queue.'.format(name,value)
            time.sleep(random.randint(0,2))
            lock.release()
        else:
            lock.release()
            print "queue is empty"
            break

if __name__=='__main__':
    manager = multiprocessing.Manager()
    # 父进程创建Queue，并传给各个子进程：
    q = manager.Queue()
    lock = manager.Lock() #初始化一把锁
    p = Pool()
    pw = p.apply_async(write,args=(q,lock))    
    pr1 = p.apply_async(read,args=("p1",q,lock))
    pr2 = p.apply_async(read,args=("p2",q,lock))
    pr3 = p.apply_async(read,args=("p3",q,lock))
    pr4 = p.apply_async(read,args=("p4",q,lock))
    print "all is over"
    p.close()
    p.join()
    
    print " --"
    print '所有数据都写入并且读完'
