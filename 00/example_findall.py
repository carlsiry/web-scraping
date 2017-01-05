import re

example_text = '我是kingname, 我的微博账号是:kingname, 密码是:12345678, QQ账号是:99999, 密码是:890abcd, 银行卡账号是:000001, 密码是:654321, Github账号是:99999@qq.com, 密码是:7777love8888, 请记住他们。'


# user_password_without_parentheses = re.findall('账号是:.*?, 密码是:.*?,', example_text)
# print(user_password_without_parentheses)

user_password = re.findall('账号是:(.*?), 密码是:(.*?),', example_text)
print(user_password)
for each in user_password:
    print('账号: {}, 密码: {}'.format(each[0], each[1]))
