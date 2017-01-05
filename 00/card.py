# # coding=utf-8
#
#
# # 名片盒：用来存储名片
# names = ['carson', 'jay']
#
# # 定义一个函数
# # 功能： 打印 名片夹列表
# def dis():
#     '''
#     display names
#     :return: none
#     '''
#     i = 1
#     for name in names:
#         print "第%d张：%s"%(i,name)
#         i += 1
#
#
# while True:
#
#     dis()
#     print '------应用菜单------'
#     print '新增名片请按--1'
#     print '------应用菜单------'
#     print '------应用菜单------'
#     name = raw_input('新增名片请按--1')
#     break


# print dis.__doc__

sum_dir_tree = input('请输入目录层数：' )

path = []
partition = '/'
sum = sum_dir_tree + 1

while sum_dir_tree :
    name = raw_input('请输入第%d部分的路径：'%(sum - sum_dir_tree))
    path.append(name)
    sum_dir_tree -= 1

# partition.join(path)
# print path
print  partition.join(path)