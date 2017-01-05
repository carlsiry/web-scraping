# coding=utf-8

# 逻辑行与物理行

# 逻辑行：逻辑上的意思的行数
# 一个逻辑行跨越多个物理行时必须使用行连接
print 'abc';print '123';print 'def'
print "we are \
family"
print  "It's very nice " \
    "of you"

# 物理行：实际上的看到的行数。
# 一个物理行一般可以包含多个逻辑行
# 一个物理行包含多个逻辑行用分号隔开
print 'a'
print 'abc';print '123';print 'def'

# 实例：1个物理行，3个逻辑行
print 'abc';print '123';print 'def'

# 实例：1个逻辑行，3个物理行
print '''这里是第一个物理行
这里是第二个物理行
这里是第三个物理行'''


