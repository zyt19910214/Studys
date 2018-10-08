# coding=utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
import re


def geturl(keyword, answer1, answer2, answer3):
    count1, count2, count3, count4 = 0, 0, 0, 0
    for page in range(3):
        pn = page * 100 + 1
        html = baidu_search(keyword, pn)
        soup = BeautifulSoup(html, "html.parser")
        # print soup
        arr_list = soup.find_all('div', attrs={"div", re.compile(r'c-abstract')})
        for x in arr_list:
            count1 = str(x).count(answer1) + count1
            count2 = str(x).count(answer2) + count2
            count3 = str(x).count(answer3) + count3

    new_dict = {count1: answer1, count2: answer2, count3: answer3}
    # print len(new_dict)
    keys = new_dict.keys()
    keys.sort()

    # print answer1 + ": "+str(count1)
    # print answer2 + ": " + str(count2)
    # print answer3 + ": " + str(count3)

    return answer1 + ": " + str(count1), answer2 + ": " + str(count2), answer3 + ": " + str(count3)


def baidu_search(wd, pn):
    result_list = []

    # 设置多个user_agents，防止百度限制IP
    user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
                   'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+(KHTML, like Gecko)'
                   ' Element Browser 5.0',
                   'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)',
                   'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                   'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
                   'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) '
                   'Version/6.0 Mobile/10A5355d Safari/8536.25',
                   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0'
                   ' Safari/537.36',
                   'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']


    p = {'wd': wd}
    res = urllib2.urlopen(("http://www.baidu.com/s?" + urllib.urlencode(p) + "&pn={0}&cl=3&rn=100").format(pn))
    html = res.read()

    return html

