# coding=utf-8

import re
import csv

# with open('index.html', 'r', encoding='utf-8') as f:
with open('index.html') as f:
    str_html = f.read()

# 1. 先抓大后抓小: 先获得所有包含一层楼的所有内容
all_floors = \
    re.findall('j_l_post clearfix  "(.*?)p_props_tail', str_html, re.S)
    # re.findall('l_post l_post_bright j_l_post clearfix  "(.*?)p_props_tail props_appraise_wrap', str_html, re.S)
# print all_floors

# 2. 获取每个楼层里的发帖人、内容、时间
result_list = []
for each in all_floors:
    result = {
        'username': re.findall('username="(.*?)"', each, re.S)[0],
        'content': re.findall('j_d_post_content ">(.*?)<', each, re.S)[0].replace('            ', ''),
        'deploy_time': re.findall('tail-info">(2017-.*?)<', each)[0]
    }
    result_list.append(result)

# with open('result.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=['username', 'content', 'deploy_time'])
#     writer.writeheader()
#     writer.writerows(result_list)

for each in result_list:
    print each['username']
    print each['content']
    print each['deploy_time']
