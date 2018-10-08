# -*- coding: utf-8 -*-

"""
@version: python2.7
@author: ‘Na‘
@software: PyCharm
@file: Zbaike.py
@time: 2017/10/22 23:26
"""
import pymongo
import random
from Tkinter import *
import webbrowser

root = Tk()
root.title(u'百度百科')
lable = Label(text=u'标题')
lable2 = Label(text=u'概述')
listb = Listbox(root, width=200)

t = Entry(root, insertontime=50, width=80)
# t = Text(root, height=1)
t2 = Text(root, height=15)
S = Scrollbar(root)
S.config(command=t2.yview)
t2.config(yscrollcommand=S.set)

def getbaike():

    connection = pymongo.MongoClient(host="localhost", port=27017)
    db = connection.test
    num = db.spiders.count()
    now_num = random.randint(0, num)
    data1 = db.spiders.find()[now_num]

    # data1 ='url: '+data['url']
    # data2 = 'title: ' + data['title']
    # data3 = 'summary: ' + data['summary']

    t.delete(0, END)
    t2.delete(0.0, END)

    t.insert(0, data1['title'])
    t2.insert(0.0, data1['summary'])


def getbaike2():
    global data
    t2.delete(0.0, END)
    my_value = t.get()

    my_value = my_value.encode('utf-8')
    connection = pymongo.MongoClient(host="localhost", port=27017)
    db = connection.test
    data = db.spiders.find({'title': my_value})
    if data.count() == 0:
        print u'查询未果~！'
    else:
        t2.insert(0.0, data[0]['summary'])


def getbaike3():

    webbrowser.open(data[0]['url'])


botton1 = Button(root, text=u'随机获取一个百科词条', command=getbaike)
botton2 = Button(root, text=u'查询', command=getbaike2)
botton3 = Button(root, text=u'详情', command=getbaike3)

lable.grid(row=0, columnspan=3)

t.grid(row=1, columnspan=3)
lable2.grid(row=2, columnspan=3)
S.grid(row=3, column=3, columnspan=3)
t2.grid(row=3, column=0, columnspan=3)

botton1.grid(row=4, column=0)
botton2.grid(row=4, column=1)
botton3.grid(row=4, column=2)
root.mainloop()
