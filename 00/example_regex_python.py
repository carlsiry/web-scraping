import re

big_string = '我是kingname,我的微博密码是:12345678, QQ密码是:890abcd, 银行卡密码是:654321, Github密码是:7777love8888, 请记住他们。'

password_findall = re.findall('密码是:(.*?),', big_string)
print(password_findall)

big_string_mutil = '''
我是kingname,我的微博密码是:123
45678,
'''
password_findall_no_flag = re.findall('密码是:(.*?),', big_string_mutil)
password_findall_flag = re.findall('密码是:(.*?),', big_string_mutil, re.S)
print(password_findall_no_flag)
print(password_findall_flag)

password_search = re.search('密码是:(.*?),', big_string)
print(password_search)
print(password_search.group())
print(password_search.group(1))

