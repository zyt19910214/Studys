# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: ‘Na‘
@software: PyCharm
@file: html_db.py
@time: 2017/10/22 23:07
"""

import pymongo


class HtmlDb(object):
    def __init__(self):
        self.datas = []
        self.connection = pymongo.MongoClient(host="localhost", port=27017)
        self.db = self.connection.test

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        spider = {"url": data['url'], "title": data['title'], "summary": data['summary']}
        mal_info = self.db.spiders
        mal_info.insert(spider)

    def output_db(self):
        connection = pymongo.MongoClient(host="localhost", port=27017)
        db = connection.test
        # print db
        # collection = db.test

        for data in self.datas:
            spider = {"url": data['url'], "title": data['title'], "summary": data['summary']}
            mal_info = db.spiders
            mal_info.insert(spider)
