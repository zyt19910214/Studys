# -*- coding: UTF-8 -*-

"""
@version: python2.7
@author: ‘Na‘
@software: PyCharm
@file: Connetdb.py
@time: 2017/10/22 22:47
"""
import pymongo

connection  = pymongo.MongoClient(host="localhost", port=27017)
db = connection.test
collection = db.test

post = {"name":"a.privacy.GingerMaster.a", "family":"GingMaster", "category":"隐私窃取",
        "behavior":u"非法获取手机root权限，强制开机自启动、强制联网、窃 取并上传用户手机中的IMEI、IMSI、SIM卡信息等隐私内容，还会将病毒组件伪装成PNG图片，从后台静默下载、安装恶意软件，消耗用户流量"}
malinfo = db.posts

malinfo.insert(post)
db.collection_names()

print malinfo.find_one()