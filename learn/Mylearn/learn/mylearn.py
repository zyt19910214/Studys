# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: ‘Na‘
@software: PyCharm
@file: mylearn.py
@time: 2017/11/1 22:15
"""

import hashlib
import urllib2,json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def youdao(word):

    src = '677b318b7682d7ec%s'%word+'2'+'f48PDter84Pk59W0trMnF5GSmGDgzf8V'
    m2 = hashlib.md5()
    m2.update(src)
    nowsrc = m2.hexdigest()

    url = r'http://openapi.youdao.com/api?q=%s&from=zh-CHS&to=fr&appKey=677b318b7682d7ec&salt=2&sign=%s'%(word,nowsrc)

    reqs = urllib2.urlopen(url).read()

    fanyi = json.loads(reqs)
    print fanyi
    # 根据json是否返回一个叫“basic”的key来判断是否翻译成功
    if 'webdict' in fanyi.keys():
        # 下面是你自已来组织格式
        extend = fanyi['translation']

        trans = ''.join(extend)
        return trans
    else:
        return u'对不起，您输入的单词%s无法翻译，请检查拼写'% word

if __name__ == '__main__':
    nn = youdao("我爱你")
    print nn