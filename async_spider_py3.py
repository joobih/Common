#!/usr/bin/env python
# coding=utf-8

import asyncio
import time
import json
from urllib import parse
from aiohttp import ClientSession


"""
假设url_info的结构如下
{
    "url":"http://a.com",
    "extra":"other infos",
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

#urls_info = [{"url":"http://img1.3lian.com/2015/w7/85/d/21.jpg"},{"url":"http://img0.imgtn.bdimg.com/it/u=246912836,1223468464&fm=23&gp=0.jpg"},{"url":"http://pic.58pic.com/58pic/13/71/40/95P58PICtdF_1024.jpg"}]
#result = async_spider(urls_info)
#print(result)

