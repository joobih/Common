#encoding=utf-8

from tornado import gen
import tornado.httpclient
import tornado.ioloop

@gen.coroutine
def _get_content(url_info):
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield http_client.fetch(url_info["url"])
    url_info["content"] = response.body
    raise gen.Return(url_info)

@gen.coroutine
def _get_contents(url_infos = []):
    if url_infos == []:
        raise gen.Return(None)
    responses = yield [_get_content(url) for url in url_infos ]
    raise gen.Return(responses)

def async_spider(url_infos):
    results = []
    while len(url_infos) > 20:
        task_urls = url_infos[:20]
        result = tornado.ioloop.IOLoop.current().run_sync(_get_contents,url_infos = task_urls)
        url_infos = url_infos[20:]
        results.extend(result)
    result = tornado.ioloop.IOLoop.current().run_sync(_get_contents,url_infos = url_infos)
    results.extend(result)
    return results

#import time
#t = time.time()
#url = {"url":"http://www.baidu.com"}
#url_infos = []
#for u in range(0,10):
#    url_infos.append(url)
#result = async_spider(url_infos)
#for r in result:
#    print(r)
#b = time.time()
#print(b-t)
