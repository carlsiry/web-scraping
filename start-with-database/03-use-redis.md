# 使用 Redis


## 安装 Redis

- Linux

```
wget http://download.redis.io/releases/redis-3.2.1.tar.gz
tar xzf redis-3.2.1.tar.gz
cd redis-3.2.1
make

#运行解压以后的文件夹下面的src文件夹中的redis-server文件启动redis服务
src/redis-server
```

- Mac：使用homebrew安装

```
brew update
brew install redis

#运行Redis
redis-server
```

- Redis没有Windows的官方安装包，只有第三方的安装包：

```
下载安装文件zip包：https://github.com/MSOpenTech/redis/releases
解压以后的文件夹，使用命令行运行里面的redis-server即可。
```

> 官方文档：http://redis.io/topics/quickstart

## Redis-Py 的基本使用

安装：

`sudo pip install redis`

**连接池**

由于创建连接非常消耗系统资源，所以不应该频繁的创建/断开到redis数据库的连接，需要使用连接池来管理 Redis 的连接。
Redis-py已经有一个 **ConnectionPool** 类来帮我们完成了这个事情。我们要做得只是创建连接池，然后使用。其他的一切，Redis-py会自动帮我们完成。

```
import redis

connection_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

def getValue(key):
    server = redis.Redis(connection_pool=connection_pool)
    response = server.get(key)
    return resoponse

def setValue(key, value):
    server = redis.Redis(connection_pool=connection_pool)
    server.set(key, value)

# redis.Redis()和redis.StrictRedis()的区别:

# redis.StrictRedis这个类严格根据Redis的命令语法来实现
# redis.Redis这个类是 redis.StrictRedis 的子类，它复写了一些命令来保证向后兼容老的 Redis-py版本，如果不需要实现向后兼容，可以使用 redis.StrictRedis, 否则使用 redis.Redis
```
