# coding=utf-8

import urllib

def demo():
    """
    演示 urllib 模块的使用：
        urllib.urlopen
            url: scheme('http:/file')
            data: 如果有，则变成 POST 方法，数据格式必须是 application/x-www-form-urlencoded
            返回类文件句柄：类文件句柄常用方法（read,readline,readlines,close,getcode）
    :return:
    """


    result = urllib.urlopen('http://blog.kamidox.com')

    # 0. 读取状态码
    print result.getcode()

    # 1. 读取所有内容clear
    # print result.read()

    # 2. 顺序读取一行
    # for i in range(3):
    #     print 'line %d: %s' %(i + 1, result.readline())
    # print result.readline() # fourth line

    # 3. 读取多行，返回行列表
    # line_list = result.readlines()
    # no = 1
    # for i in line_list:
        # print 'line %d: %s'%(no, i)
        # no += 1

    # 4. info(): 返回 httplib.HTTPMessage（没有官方文档） 实例
    #            headers
    #            gettype()
    #            getheader()/getheaders()
    #            items()/keys()/values()
    # msg = result.info()
    # print_list(dir(msg))
    # print_list(msg.headers) # 列表类型的头内容
    # print_list(msg.items()) # 元组类型的头内容
    # print msg.getheader('Content-Type') # 获得指定的头信息

    # 5. urllib.urlretrieve(url, filename, reporthook,data):
    #       reporthook: 下载状态报告，data：post的格式
    #       返回（filename, HTTPMessage)
    # def progress(blk, blk_size, total_size):
    #     print '%d-%d -- %.02f%%'%(blk * blk_size, total_size, (float)(blk*blk_size) * 100 / total_size)
    #
    # file_name, msg = urllib.urlretrieve('https://littlecarson.github.io', 'blog.html', reporthook=progress)
    # print file_name
    # print_list(msg.items())

def print_list(list):
    for i in list:
        print i

if __name__ == '__main__':
    demo()