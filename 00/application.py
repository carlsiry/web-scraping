#coding=utf-8
import re
with open('text.txt') as f:
    text = f.read()
    # print re.findall("：(.*?\n.*?)，", text)
    print re.findall("：(.*?)，", text, re.S)

text = "我的银行卡账号是：12345，密码是：54321。扣扣账号是：1129247380，密码是：12345。"

result1 = re.search("账号是：(.*?)，密码是：(.*?)。", text)
result2 = re.search("账号是：(.*?)，", text).group()
print result1, result2
# <_sre.SRE_Match object at 0x000000000211DBE8> 账号是：12345，

print result1.group(1) # 12345
print result1.group(2) # 54321
print result1.group(0)
print result1.group(3)
