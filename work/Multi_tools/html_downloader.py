# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: ‘Na‘
@software: PyCharm
@file: html_downloader.py
@time: 2017/10/22 22:26
"""
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
