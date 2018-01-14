# -*- coding: utf-8 -*-
# @author wuwaki
# @date 2018/1/14

from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser
from os import path
from json import load
import sys
import yaml

config = path.abspath(path.dirname(__file__))[:-5] + 'config.yaml'
with open(config) as f:
    c = yaml.load(f.read())
    indexdir = c['index']

idx = open_dir(indexdir)


def load_bookmark():
    with open('bookmark.json', 'r') as bf:
        return load(bf)


def get_query_str():
    strs = sys.argv[1:]
    return 'and'.join(s for s in strs)


def main():
    with idx.searcher() as searcher:
        if len(sys.argv) < 2:
            print('请输入需要查询的关键字')
            exit(1)
        query_parse = MultifieldParser(['title', 'content'], schema=idx.schema)
        query_str = query_parse.parse(get_query_str())
        results = searcher.search(query_str)
        if len(results) == 0:
            print('没有搜索结果')
            exit(0)
        for r in results:
            doc = r.fields()
            bookmark_s = bookmark[doc['id']]
            print('name: {}, url: {}'.format(bookmark_s['name'], bookmark_s['url']))


if __name__ == '__main__':
    bookmark = load_bookmark()
    main()
