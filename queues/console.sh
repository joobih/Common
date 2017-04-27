#!/bin/bash                                                                                                                                                    
print_usage()
{
    echo "usage: $0 {start|stop}"
}
case "$1" in
    start)
        python test_consumer.py
        ;;
    stop)
        ps aux|grep "python test_consumer.py" | grep -v grep | awk '{print $2}' | xargs kill -9
        ;;
    *)  
        print_usage
esac

