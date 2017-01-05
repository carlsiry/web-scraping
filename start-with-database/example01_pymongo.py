import pymongo

client = pymongo.MongoClient()
database = client.person_info
col = database.people

info_dict = {'name': 'carson', 'age': 0, 'sex': 'unknown', 'salary': 0}
col.insert(info_dict)

kingname = col.find()
for each in kingname:
    print(each['name'])

col.update({'name': 'carson'}, {'$set': {'age': 19, 'sex': 'male'}})
# col.update_many({'name': 'carson'}, {'$set': {'age': 19, 'sex': 'male'}})

# col.delete_one({'name': 'carson'})
col.drop()
