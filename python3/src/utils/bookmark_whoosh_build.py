# -*- coding: utf-8 -*-
# @author wuwaki

import os
import yaml
from whoosh.index import create_in
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer


def main():
    # 使用结巴的中文分词
    analyzer = ChineseAnalyzer()

    # 创建 schema, stored 为 True 表示能够被检索
    schema = Schema(title=TEXT(stored=True, analyzer=analyzer), path=ID(stored=False),
                    content=TEXT(stored=True, analyzer=analyzer), id=TEXT(stored=True))

    # 读取 yaml 信息
    config = os.path.abspath(os.path.dirname(__file__))[:-5] + 'config.yaml'
    with open(config) as f:
        c = yaml.load(f.read())
        indexdir = c['index']

    # 存储schema信息至 indexdir 目录下
    if not os.path.exists(indexdir):
        os.mkdir(indexdir)
    idx = create_in(indexdir, schema)

    # 按照 schema 定义信息, 增加需要建立索引的文档
    # 注意: 字符串格式需要定义为 unicode 格式
    return idx
