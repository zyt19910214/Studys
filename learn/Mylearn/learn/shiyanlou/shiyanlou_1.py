# -*- coding: utf-8 -*-

"""
@version: python2.7
@author: 'zyt'
@software: PyCharm
@time: 2018/4/29 12:52
"""

'''
写一个判断闰年的函数，参数为年、月、日。若是是闰年，返回True
'''

def is_leap_year(data):
    if int((data.split('-')[0]))%4 == 0:
        return True
    else:
        return False


for i in range(1900,2001):
    if is_leap_year(str(i)):
        print str(i) + ' is leap year'
    else:
        print str(i) + ' is not leap year'