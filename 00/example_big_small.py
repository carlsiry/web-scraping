#coding=utf-8

import re

example_text = '''
有效用户:
姓名: 张三
姓名: 李四
姓名: 王五
无效用户:
姓名: 死人
姓名: 僵尸
'''

# user = re.findall("姓名: (.*?)\n", example_text)
# print user


# user_big = re.findall('有效用户(.*?)无效用户', example_text, re.S)
# print('user_big 的值为: {}'.format(user_big))
#
# user_useful = re.findall('姓名: (.*?)\n', user_big[0])
# print(user_useful)

example = '''
<div class="info">回帖</div>
<div class="info">2016-07-20 12:00:00</div>
'''
content1 = re.findall('info">(20.*?)<', example)
content2 = re.findall('info">20(.*?)<', example)

print content1
print content2