# coding=utf-8

import urllib2
import re
import itertools


def download(url, user_agent='carson', retries_num=2):
    '''
    下载所传入网址的网页，默认代理为:carson，服务器错误默认重试下载2次
    :param url: 网址
    :param user_agent: 用户代理，默认carson
    :param retries_num: 服务器错误重新下载次数，默认2
    :return: 返回获取到的网页
    '''
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if retries_num > 0:
            if hasattr(e, 'code') and (500 <= e.code < 600):
                return download(url, user_agent, retries_num-1)
    return html

def crawl_sitemap(url):
    '''
    爬取所传入robots.txt地址文件中的所有网站地图网页
    :param url: 网站robots的文件地址
    :return: void
    '''
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        #  scrap html here
        # ...

def iteration():
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-{}'.format(page)
        html = download(url)
        if html is None:
            # received an error trying to download this webpage
            # so assume have reached the last country ID and can stop downloading
            break
        else:
            # success - can scrape the result
            # ...
            pass


def iteration2():
    # maximum number of consecutive download errors allowed
    max_errors = 5
    # current number of consecutive download errors
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d' % page
        html = download(url)
        if html is None:
            # received an error trying to download this webpage
            num_errors += 1
            if num_errors == max_errors:
                # reached maximum number of
                # consecutive errors so exit
                break
        else:
            num_errors = 0


def get_links(html):
    '''Return a list of links from html'''
    # a regular expression to extract all links from the web_page
    web_page_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',
                          re.IGNORECASE)
    # list of all links from the web_page
    return web_page_regex.findall(html)



# crawl_sitemap('http://example.webscraping.com/sitemap.xml')

# download('http://httpstat.us/500', 'littlecarson', 3)

# print download('http://www.meetup.com', 'little_carson', 3)

