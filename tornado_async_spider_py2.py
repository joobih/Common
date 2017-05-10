#encoding=utf-8

from tornado import gen
import tornado.httpclient
import tornado.ioloop


@gen.coroutine
def single_spider(url_info = {}):
    if url_info == {}:
        raise gen.Return(None)
    url = url_info["url"]
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield http_client.fetch(url, raise_error = False)
    yield response.body
    return
#    raise gen.Return(response.body)
       
@gen.coroutine
def async_spider(url_infos = []):
    if url_infos == []:
        return None
#    tasks = []
    for url_info in url_infos:
        response = yield single_spider(url_info)
        yield response.body
#        tasks.append(response.body)

#    raise gen.Return(tasks)

url_infos = [{"url":"http://www.baidu.com"},]
result = tornado.ioloop.IOLoop.current().run_sync(async_spider,url_infos = url_infos)
print(result)
