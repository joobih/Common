#!/bin/bash

print_usage(){
	echo "usage: $0 {start|stop}"
}

case "$1" in
	start)
		python $2 
		;;
	stop)
		ps aux|grep $2 | grep -v grep | awk '{print $2}' | xargs kill -9
		;;
	*)
		print_usage
esac
