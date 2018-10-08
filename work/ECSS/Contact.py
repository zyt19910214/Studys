
# -*- coding: utf-8 -*-
"""
  ---------------------------
  @File: Contact.py
  @Author: zyt
  @Date: 2017/12/6 10:42
  @Software: Pycharm
  @Version: Python2.7
  ---------------------------
"""


import requests
import json
import sys

import Tkinter
from Tkinter import *
from tkMessageBox import  *

reload(sys)

top =Tkinter.Tk()
top.title(u'集团通讯录测试工具')
Label1 =Label(top,text="用户ID：").grid(row=0)
Label4 =Label(top,text="查询条件：").grid(row=1)
Label2 =Label(top,text="获取通讯录的接口地址：").grid(row=2)
Label3 =Label(top,text="获取部门的接口地址：").grid(row=3)
Label5 =Label(top,text="查询结果：").grid(row=4)
e = StringVar()
e.set('353')
e4 = StringVar()
e4.set('')
e2 = StringVar()
e2.set('http://emm-contactmis.test.safecenter.com/mis/cm.contact.getecsscontactmembersfromserver/global')
e3 = StringVar()
e3.set('http://emm-contactmis.test.safecenter.com/mis/cm.contact.getecssdeptsfromserver/global')
ID1 = Entry(top,textvariable=e,width=120)
ID4 = Entry(top,textvariable=e4,width=120)
ID2 = Entry(top,textvariable=e2,width=120)
ID3 = Entry(top,textvariable=e3,width=120)
ID1.grid(row=0,column=3)
ID4.grid(row=1,column=3)
ID2.grid(row=2,column=3)
ID3.grid(row=3,column=3)
# ss  = tkinter.Lable(top,text=u'ss',width=30,height=2)
listb = Listbox(top,height=25,width=120,selectmode=BROWSE)
listb.grid(row=4,column=1,columnspan=4)
def Get_Connect():
    listb.delete(0,END)
    Args1=ID1.get()
    Args2=ID4.get()
    Args3 = {"userAccount": Args1,"queryCondition":Args2}

    Url=ID2.get()
    Url2 =ID3.get()
    Args  = json.dumps(Args3)
    try:
        r =requests.post(Url,Args)
        r2 = requests.post(Url2, Args)
    except Exception as e:
        listb.delete(0, END)
        listb.insert(0, e)
        listb.insert(1, "请求失败！检查URL是否正确~")
    if r.json()['result'] =='success' and r2.json()['result'] =='success':

        dept_list =r2.json()['data']['depts']
        dept_list.sort(key=lambda k: ((int)(k.get('sort', 0))), reverse=True)
        li = r.json()['data']['persons']
        li.sort(key=lambda k: ((int)(k.get('id', 0))), reverse=True)
        total = '联系人总数：', r.json()['data']['totalRecord']
        listb.insert(0, total)

        for i in range(len(dept_list)):

            listb.insert(1,u'部门：'+dept_list[i]['name'])
            for x in range(0, len(li)):
                if li[x]['deptId'] ==dept_list[i]['id']:
                    listb.insert(2,u'       人员-'+li[x]['id']+'___'+li[x]['name'])
    else:
        listb.delete(0, END)
        listb.insert(0,  r.json()['errInfo'])
    showinfo('消息','查询完成')
button = Button(top,text='查询',command=Get_Connect).grid(row=5,column=0,columnspan=4)
top.mainloop()
