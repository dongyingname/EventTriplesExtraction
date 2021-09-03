# coding: utf-8
from triple_extraction import *

print('基于ltp依存句法分析和语义角色标注的事件三元组抽取!')
extractor = TripleExtractor()
# content = '李克强总理今天来我家了,我感到非常荣幸'
contents = [
    '基本同意坝址多年平均悬移质年输沙量为4.25万吨，推移质年输沙量按悬移质年输沙量的22%估列。',
    '（四）同意坝址及其下游有关断面的水位流量关系成果。',
    '3．基本同意对流量计井与调流阀室和下游护岸工程地质条件的评价意见。',
]
for content in contents:
    svos = extractor.triples_main(content)
    print('content:', content)
    print('svos:', svos)

print('基于百度DDParser依存句法分析的事件三元组抽取')
from baidu_svo_extract import *
extractor = SVOParser()
for content in contents:
    svos = extractor.triples_main(content)
    print('content:', content)
    print('svos:', svos)
