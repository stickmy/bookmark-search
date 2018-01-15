## WHAT

有时候遇到问题, google 解决了之后, 我们会把这篇文章收藏下来, 以便下次查看.
随着时间变长, 收藏的文章越来越多, 就经常找不着.
使用这个小工具, 帮助你找到你想要的文章, 可以支持标题以及文章内容检索.
![](http://g.recordit.co/kz17LNDtOe.gif)

## SUPPORT

- python2
- python3
- alfred-workflow
- (目前只支持 MacOs chrome)
- alfred workflow 第一次初始化可能比较慢, 根据书签多少来决定, 1-10分钟不等

## USAGE

```bash
# install
pip install -r requirements.txt

# initial
python src/reset.py

# search 支持多个关键字搜索
python src/utils/search.py `keyword`

# example
python src/utils/search.py 算法 最小生成树
```

## TODO

- 初始化比较慢, 可以考虑多线程实现
- 目前采用的 whoosh + jieba 做全文检索, 或许可以采用精确度更高的做法
- 支持 windows 等其他系统
