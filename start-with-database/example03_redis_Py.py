# coding=utf-8

import redis

r = redis.StrictRedis(host='127.0.0.1', port=6379)

# r.set('key', 'value')
# print r.get('key')
# r.set('name', 'carson')
print r.get('name')
print r.get('name') # 可以多次读取同一个 key
# r.append('name', ' Chen')
print r.get('name')
print r.keys()
r.delete('name')
print r.keys()
