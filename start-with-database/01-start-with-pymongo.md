# start with pymongo

## Python 下使用 MongoDB

### Python的字典与MonggoDB的文档

MongoDB数据的储存形式（文档）和Python的字典表示形式一致。所以，使用起来将会很方便。例如：

```
$ mongo
(mongo-shell)>
>use test
switch to db test
> shwo collections
student
> db.student.find().pretty()
{
    "_id" : ObjectId("5860c9d9bc1f5506a59fc9c0"),
    "age" : 23,
    "name" : "carson",
    "sex" : "male"
}

$ python
stu_a = { "id": 001, "name": "carson", "age": 18, "sex": "male"}

```

### Install PyMongo

**pymongo**模块：是Python对MongoDB操作的接口包，主要实现对MongoDB的几种操作：增删改查以及排序等功能

```
# Python2
pip install pymongo
# Python3
apt-get install python3-pip

# 安装GUN C compiler（GCC）（使用MongoDB的C扩展）
apt-get install build-essential python-dev

# 验证安装
python
> import pymongo
```

### 基本使用

连接数据库首先要用 **pymongo** 的 **`MongoClien`**实例指定 **IP**与端口，方法有两种：

1. 指定参数形式：`conn = MongoClient(host='127.0.0.1', port=27017)`（注意端口号是数字）
2. 传入 MongoDB URI 形式：`mongodb://[username:password@]host1:[:prot1][,host2:[:port2],...[,hostN[:portN]]][/[database][?options]]`，比如：

```
conn = MongoClient('mongodb://127.0.0.1:27019')
```

基本使用：

```
# coding=utf-8

from pymongo import MongoClient

#  连接本地数据库
client = MongoClient()

#  选择数据库或创建数据库
database = client.school
database = client['school']

# 批量连接使用
db_list = ['db1', 'db2', 'db3']
for each_db in db_list:
    db = client[each_db]
    collection = db.test
    #...

#  选择数据集或创建集合
collection = database.student

# 创建一条字典格式数据
stu_dic = {'name': 'carson', 'age': 23, 'sex': 'male'}

# 插入数据（字典格式）
collection.insert(stu_dic)
collection.insert_one(stu_dic)

# 查询集合中的所有数据
stu_all = colection.find() # 此处 stu_all 是一个pymongo对象
for each in stu_all:
    print(each['name'])

# 查询指定的文档
content = col.find({'age': 29})
content = col.find_one({'age': 23}) # =
content = col.find({'age': {'$lt':20} })  # 小于
content = col.find({'age': {'$lte':20} }) # <=
content = col.find({'age': {'$gt':20} }) # >
content = col.find({'age': {'$gte':20} }) # >=
content = col.find({'age': {'$ne':20} }) # not 
content = col.find({"$or": [{"age": "16"}, {"name": "carson"}]}) # or
content = col.find({{"age": "16"}, {"name": "carson"}})     # and

# 更新指定的数据
collection.update({'name': 'carson'}, {'$set':{'name': 'kingname'}}) # MongoDB 默认只更新单个文档
collection.update_many({'age': 20}, {'$set':{'age': 30}})
collection.update_one({'age': 20}, {'$set':{'name': 'kingname'}})

# 删除指定数据
collection.delete_one({'name': 'kingname'})
collection.delete_many({'name': 'carson'})

# 删除集合
database.people_info.drop()
```
