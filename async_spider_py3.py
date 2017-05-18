#encoding=utf-8

import asyncio
import uvloop
import time
import json
from urllib import parse
from aiohttp import ClientSession

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Connection":"keep-alive",
}

"""
假设url_info的结构如下
{
    "url":"http://a.com",
    "extra":"other infos"
}
最后返回一个新的url_info json对象增加content 字段表示抓取到的结果 内容
"""
async def _get_content(url_info):
    async with ClientSession(headers=headers) as session:
        url = url_info["url"]
        async with session.get(url,timeout=10) as r:
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
#    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    results = []
    loop_num = 2
    if url_infos[0]["html_type"] == "txt":
        loop_num = 30
    elif url_infos[0]["html_type"] == "pic":
        loop_num = 2
    while len(url_infos) > loop_num:
        task_urls = url_infos[:loop_num]
        result = loop.run_until_complete(_get_contents(loop,task_urls))
        url_infos = url_infos[loop_num:]
        results.extend(result)
    result = loop.run_until_complete(_get_contents(loop,url_infos))
    results.extend(result)
    return results

import time
t = time.time()
url = {"url":"http://www.baidu.com","html_type":"txt"}
#url = {"url":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1495018130624&di=3ea1524ee141d1b869709fc82cf73306&imgtype=0&src=http%3A%2F%2Fwww.jahuaxia.cn%2Fupload%2Fimg%2F9YSLg4QbxNCw3hfPpivZN53vLogHuuYfoXs1UnAbXwxUUY69aWN1MQjWOMyWqWOnNfOQFAKVnd9kU0JwyVFvVto9uyyJpKV5S9FYCgox%2F3zyqNdTzA.jpg","html_type":"pic"}
url_infos = []
for u in range(0,200):
    url_infos.append(url)
result = async_spider(url_infos)
#for r in result:
#    print(r)
b = time.time()
print(b-t)
