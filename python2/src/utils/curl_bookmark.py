# -*- coding: utf-8 -*-
# @author wuwaki
# @date 2018/1/14

import requests
import bookmarks
import bookmark_whoosh_build as whbuild
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
}

# bookmarks
pages = bookmarks.main()

# 检索
idx = whbuild.main()

writer = idx.writer()


def add_doc(path, title, content):
    writer.add_document(title=title,
                        path=path,
                        content=content,
                        id=path)


def main():
    for path, _ in pages.viewitems():
        try:
            name = _['name']
            path_unicode = path.decode('utf-8')
            print '正在建立索引: {}'.format(name.encode('utf-8'))
            if len(name.split('.')) > 1 and name.split('.')[-1] == 'pdf':
                add_doc(path_unicode, name, u'pdf内容木有加载~')
            else:
                html = requests.get(_['url'], headers=header, timeout=5)
                if html.status_code == requests.codes.ok:
                    add_doc(path_unicode, name, extract_pure_text(html) or u"空页面~")
                else:
                    add_doc(path_unicode, name, u'网页内容未能正确加载~')
        except:
            print '请求失败'

    writer.commit()


def extract_pure_text(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    for script_style in soup(['script', 'style']):
        # 去除 script 和 style 标签
        script_style.extract()
    text = soup.get_text()
    # trim 每一行的空格
    lines = (line.strip() for line in text.splitlines())
    # 去除每行文本内容中的空格
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # \n
    text = ''.join(chunk for chunk in chunks if chunk)
    return text


def test():
    html = requests.get('http://qifuguang.me/page/8/', headers=header, timeout=5)
    print extract_pure_text(html)


if __name__ == '__main__':
    main()
    # test()
