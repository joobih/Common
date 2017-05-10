#encoding=utf-8

import sys

from tornado import gen
import tornado.httpclient
import tornado.ioloop


if sys.version > '3':
    print("py3")
    async def async_spider(url_info = []):
        if url_info == []:
            return None
        url = url_info["url"]
#        url = "http://www.baidu.com"
        http_client = tornado.httpclient.AsyncHTTPClient()
        response = await http_client.fetch(url)
        
#        print(response.body)
        return response.body
    
else:
    @gen.coroutine
    def async_spider(url_info):
        url = url_info["url"]
        http_client = tornado.httpclient.AsyncHTTPClient()
        response = yield http_client.fetch(url)
#        print(response.body)
        raise get.Return(response)
       
url_info = {"url":"http://www.baidu.com"}
result = tornado.ioloop.IOLoop.current().run_sync(async_spider,url_info = url_info)
print(result)
