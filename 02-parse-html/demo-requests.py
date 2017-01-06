# coding=utf-8

import requests

 # 获取指定网址的源码
# html = requests.get('https://movie.douban.com/top250').content
# html = requests.get('https://movie.douban.com/top250').content # py3 下返回的是 byte 类型
# print html.decode()
# print html

# post 请求
with open('reg.png', 'rb') as f:
    data = {'smfile': f}
    content = requests.post('https://sm.ms/api/upload', files = data).content
    print content