#encoding=utf-8

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Connection":"keep-alive",
}
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
    async with ClientSession(headers=headers) as session:
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
