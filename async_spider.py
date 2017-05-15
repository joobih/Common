#encoding=utf-8

import sys
if sys.version < '3':
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
else:
    import asyncio
    import time
    import json
    from urllib import parse
    from aiohttp import ClientSession


    """
    假设url_info的结构如下
    {
        "url":"http://a.com",
        "extra":"other infos"
    }
    最后返回一个新的url_info json对象增加content 字段表示抓取到的结果 内容
    """
    async def _get_content(url_info):
        print(url_info)
        async with ClientSession() as session:
            url = url_info["url"]
            async with session.get(url) as r:
                response = await r.read()
                url_info["content"] = response
                return url_info

    async def _get_contents(loop,url_infos):
        tasks = []
        for url_info in url_infos:
            future = asyncio.ensure_future(_get_content(url_info))
            tasks.append(future)
        responses = await asyncio.gather(*tasks)
        return responses

    def async_spider(url_infos):
        loop = asyncio.get_event_loop()
        results = []
        while len(url_infos) > 20:
            task_urls = url_infos[:20]
            result = loop.run_until_complete(_get_contents(loop,task_urls))
            url_infos = url_infos[20:]
            results.extend(result)
        result = loop.run_until_complete(_get_contents(loop,url_infos))
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
