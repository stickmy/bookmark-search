# -*- coding: utf-8 -*-
# @author wuwaki

from json import loads, dumps
from os.path import expanduser
import salt_str

# [{ 'name': 'url' }]
bookmark = {}

# MacOs Darwin

bookmark_file_name = expanduser("~/Library/Application Support/Google/Chrome/Default/Bookmarks")


def for_node(node):
    if node['type'] == 'url':
        name = node['name']
        # pdf 文件读取太慢, ban 掉
        if name != '':
            bookmark[salt_str.get_ranstr()] = {'url': node['url'], 'name': name}
    elif node['type'] == 'folder':
        for child in node['children']:
            for_node(child)
    else:
        return


def get_bookmark_dict(children):
    for child in children:
        for_node(child)


try:
    bookmark_file = open(bookmark_file_name, 'r', encoding='utf-8')
except IOError as e:
    if e.errno == 2:
        print('默认位置找不到 chrome 书签: {}'.format(e.filename))
        exit(1)

bookmark_contents = loads(bookmark_file.read())
bookmark_file.close()

bookmark_bar = bookmark_contents['roots']['bookmark_bar']['children']
other = bookmark_contents['roots']['other']['children']


def main():
    get_bookmark_dict(bookmark_bar)
    get_bookmark_dict(other)
    with open('bookmark.json', 'w') as f:
        f.write(dumps(bookmark, ensure_ascii=False))
    return bookmark
