# 使用 MongoEngine

**ORM**（Object-relational mapping，对象关系映射），可以将对数据库的操作变为对象的操作。

**MongoEngine** 就是MongoDB的一个ORM库，我们使用MongoEngine以后，就可以通过直接操作对象来控制MongoDB。

安装：`sudo pip install mongoengine`

## 基本使用

1. 初始化连接

```
from mongoengine import *

# 本地连接
connect('数据库名')

# 远程连接
connect('数据库名', host='192.168.2.12', port=3456) #请注意端口号是数字不是字符串
```

2. 定义文档

定义一个类，继承 **MongoEngine** 的 **Document**类。类名对应MongoDB中的集合名，类变量对应每一条记录中的列名。

```
class People(Document):
  name = StringField(required=True) #请注意所有写了required=True的变量，在类初始化的时候都是必须填写的参数哦。
  age = IntField(required=True)
  sex = StringField(required=True)
  salary = IntField() #这里的IntField 或者StringField 对应了数据类型
```

3. 创建对象

```
someone = People(name='test__', age=18, sex='male', salary=2222)
#注意这里的参数name, age 和sex是不可以省略的，但是salary可以省略
someone.save()

someone = People('last__', 18, 'male', 22222)
someone.salary = 99999
someone.save()
kingname.age = 18
kingname.save()
```

4. 读取对象

```
for person in People.objects:
  print(person.name)
  print(person.age)
  print(person.sex)

# 按条件搜索
for person in People.objects(age=22):
  print(person.name)
```

5. 删除记录

```
name_list = People.objects(name='kingname')
for name in name_list:
    name.delete()
```

>官方文档：http://docs.mongoengine.org/tutorial.html

练习：

```
# 连接到本主机27017端口的数据库服务器的指定数据库
connect('earth')

# 定义文档的模式结构：字段-类型
class People(Document):
    """docstring for People"""
    name = StringField(required=True)
    age = IntField(required=True)
    sex = StringField(required=True)
    salary = IntField()

# 保存数据
# someone = People(name='test__', age=18, sex='male')
# someone.save()

# someone = People('last__', 18, 'male', 22222)
# someone.save()

# 查询所有数据
# for each in People.objects:
#     print each.name

# 查询指定条件的数据
carson_salary_list = People.objects(name='carson')
print carson_salary_list
for each in carson_salary_list:
    print(each.salary)

# 删除指定的数据
carson_salary_list.delete()
```
