#!/usr/bin/env python
# coding=utf-8

import jieba

"""
    将字符串content按照model模式分词 model 分别有全模式(all) ,精确模式(accurate),搜索引擎模式(search_engine)三种
    待分词的字符串可以是gbk字符串，urf-8 字符串或则unicode
"""
def word_cut(content,model = "accurate"):
#    seg_content = []
    if model == "accurate":
        seg_content = jieba.cut(content,cut_all = False)
    elif model == "all":
        seg_content = jieba.cut(content,cut_all = True)
    elif model == "search_engine":
        seg_content = jieba.cut_for_search(content)
    else:
        print "不支持这种模式",model
        return ""
#print ", ".join(seg_content)
    seg = []
    for s in seg_content:
        seg.append(s)
#    seg = ", ".join(seg_content)
    for s in seg:
        print s
    return seg

content = """
开发者可以指定自己自定义的词典，以便包含jieba词库里没有的词。虽然jieba有新词识别能力，但是自行添加新词可以保证更高的正确率 
"""
print word_cut(content)
print word_cut(content,model = "all")
print word_cut(content,model = "search_engine")
