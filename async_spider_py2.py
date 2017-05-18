#encoding=utf-8

from tornado import gen
import tornado.httpclient
import tornado.ioloop

HEADERS = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Connection":"keep-alive",
}

@gen.coroutine
def _get_content(url_info):
    http_client = tornado.httpclient.AsyncHTTPClient()
    request = tornado.httpclient.HTTPRequest(
        url=url_info["url"],
        method='GET',
        headers=HEADERS
    )
    response = yield http_client.fetch(request)
    url_info["content"] = response.body
    raise gen.Return(url_info)

@gen.coroutine
def _get_contents(url_infos=None):
    if url_infos is None:
        raise gen.Return(None)
    responses = yield [_get_content(url) for url in url_infos]
    raise gen.Return(responses)

def async_spider(url_infos):
    results = []
    loop_num = 2
    if url_infos[0]["html_type"] == "txt":
        loop_num = 30
    elif url_infos[0]["html_type"] == "pic":
        loop_num = 2
    while len(url_infos) > loop_num:
        task_urls = url_infos[:loop_num]
        result = tornado.ioloop.IOLoop.current().run_sync(_get_contents, url_infos=task_urls)
        url_infos = url_infos[loop_num:]
        results.extend(result)
    result = tornado.ioloop.IOLoop.current().run_sync(_get_contents, url_infos=url_infos)
    results.extend(result)
    return results

def main():
    import time
    t = time.time()
    url = {"url":"http://www.baidu.com", "html_type":"txt"}
    url = {"url":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1495018130624&di=3ea1524ee141d1b869709fc82cf73306&imgtype=0&src=http%3A%2F%2Fwww.jahuaxia.cn%2Fupload%2Fimg%2F9YSLg4QbxNCw3hfPpivZN53vLogHuuYfoXs1UnAbXwxUUY69aWN1MQjWOMyWqWOnNfOQFAKVnd9kU0JwyVFvVto9uyyJpKV5S9FYCgox%2F3zyqNdTzA.jpg","html_type":"pic"}
    url_infos = []
    for u in range(0, 20):
        url_infos.append(url)
    result = async_spider(url_infos)
    #for r in result:
    #    print(r)
    b = time.time()
    print(b-t)

if __name__ == "__main__":
    main()
