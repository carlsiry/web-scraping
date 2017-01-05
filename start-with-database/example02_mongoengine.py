from mongoengine import *

connect('earth')

class People(Document):
    """docstring for People"""
    name = StringField(required=True)
    age = IntField(required=True)
    sex = StringField(required=True)
    salary = IntField()


# someone = People(name='test__', age=18, sex='male')
# someone.save()

# someone = People('last__', 18, 'male', 22222)
# someone.save()

# for each in People.objects:
#     print each.name

carson_salary_list = People.objects(name='carson')
print carson_salary_list
for each in carson_salary_list:
    print(each.salary)

carson_salary_list.delete()
