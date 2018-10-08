#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
import ttk
import json
import requests
if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *

    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):

    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('模拟领航平台发送数据')
        self.master.geometry('600x670')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()
        self.style = Style()

        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.062, rely=0.071, relwidth=0.887, relheight=0.876)

        # tab1
        self.TabStrip1__Tab1 = Frame(self.TabStrip1)
        self.TabStrip1__Tab1variable = StringVar()
        self.TabStrip1__Tab1box = ttk.Combobox(self.TabStrip1__Tab1,width=20,textvariable= self.TabStrip1__Tab1variable,values=['0201 用户开通','0202 用户变更','0203 用户退订','0207 用户停机','0208 用户复机'])
        self.TabStrip1__Tab1box.current(0)
        self.TabStrip1__Tab1box.grid(row=2,column=3,sticky=W)
        self.TabStrip1__Tab1Lb0 = Label(self.TabStrip1__Tab1, text='').grid(row=0)
        self.TabStrip1__Tab1Lbl = Label(self.TabStrip1__Tab1, text='流水号：').grid(row=1)
        self.TabStrip1__Tab1Lb2 = Label(self.TabStrip1__Tab1, text='操作类型：').grid(row=2)
        self.TabStrip1__Tab1Lb3 = Label(self.TabStrip1__Tab1, text='产品ID：').grid(row=3)
        self.TabStrip1__Tab1Lb4 = Label(self.TabStrip1__Tab1, text='销售品ID：').grid(row=4)
        self.TabStrip1__Tab1Lb5 = Label(self.TabStrip1__Tab1, text='客户产品计费标识：').grid(row=5)
        self.TabStrip1__Tab1Lb6 = Label(self.TabStrip1__Tab1, text='区域：').grid(row=6)
        self.TabStrip1__Tab1Lb7 = Label(self.TabStrip1__Tab1, text='客户编码：').grid(row=7)
        self.TabStrip1__Tab1Lb8 = Label(self.TabStrip1__Tab1, text='客户名称：').grid(row=8)
        self.TabStrip1__Tab1Lb9 = Label(self.TabStrip1__Tab1, text='用户手机号：').grid(row=9)
        self.TabStrip1__Tab1Lb10 = Label(self.TabStrip1__Tab1, text='AccType：').grid(row=10)
        self.TabStrip1__Tab1Lb11 = Label(self.TabStrip1__Tab1, text='AccName：').grid(row=11)
        self.TabStrip1__Tab1Lb12 = Label(self.TabStrip1__Tab1, text='用户姓名：').grid(row=12)
        self.TabStrip1__Tab1Lb12 = Label(self.TabStrip1__Tab1, text='费用：').grid(row=13)
        self.TabStrip1__Tab1Lb12 = Label(self.TabStrip1__Tab1, text='返回码：').grid(row=14)
        self.TabStrip1__Tab1Lb12 = Label(self.TabStrip1__Tab1, text='备注：').grid(row=15)
        self.TabStrip1__Tab1Lb12 = Label(self.TabStrip1__Tab1, text='响应结果：').grid(row=16)


        self.TabStrip1__Tab1e1 = StringVar()
        self.TabStrip1__Tab1e1.set('PLyuey!NAjd*Jb2y@hqOsKI%=BahK^$#')
        self.TabStrip1__Tab1e2 = StringVar()
        self.TabStrip1__Tab1e2.set('0202')
        self.TabStrip1__Tab1e3 = StringVar()
        self.TabStrip1__Tab1e3.set('Productid0000100')
        self.TabStrip1__Tab1e4 = StringVar()
        self.TabStrip1__Tab1e4.set('17000131')
        self.TabStrip1__Tab1e5 = StringVar()
        self.TabStrip1__Tab1e5.set('Bizid0000100')
        self.TabStrip1__Tab1e6 = StringVar()
        self.TabStrip1__Tab1e6.set('A0100')
        self.TabStrip1__Tab1e7 = StringVar()
        self.TabStrip1__Tab1e7.set('Custid0000100')
        self.TabStrip1__Tab1e8 = StringVar()
        self.TabStrip1__Tab1e8.set('集团CustName0000100')
        self.TabStrip1__Tab1e9 = StringVar()
        self.TabStrip1__Tab1e9.set('17629298189')
        self.TabStrip1__Tab1e10 = StringVar()
        self.TabStrip1__Tab1e10.set('1')
        self.TabStrip1__Tab1e11 = StringVar()
        self.TabStrip1__Tab1e11.set('AccName00001')
        self.TabStrip1__Tab1e12 = StringVar()
        self.TabStrip1__Tab1e12.set('用户姓名00001change')
        self.TabStrip1__Tab1e13 = StringVar()
        self.TabStrip1__Tab1e13.set('10')
        self.TabStrip1__Tab1e14 = StringVar()
        self.TabStrip1__Tab1e14.set('00000')
        self.TabStrip1__Tab1e15 = StringVar()
        self.TabStrip1__Tab1e15.set('用户查询成功')
        self.TabStrip1__Tab1ID1 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e1,width=50)
        self.TabStrip1__Tab1ID2 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e2,width=50)
        self.TabStrip1__Tab1ID3 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e3,width=50)
        self.TabStrip1__Tab1ID4 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e4,width=50)
        self.TabStrip1__Tab1ID5 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e5,width=50)
        self.TabStrip1__Tab1ID6 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e6,width=50)
        self.TabStrip1__Tab1ID7 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e7,width=50)
        self.TabStrip1__Tab1ID8 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e8,width=50)
        self.TabStrip1__Tab1ID9 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e9,width=50)
        self.TabStrip1__Tab1ID10 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e10,width=50)
        self.TabStrip1__Tab1ID11 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e11,width=50)
        self.TabStrip1__Tab1ID12 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e12,width=50)
        self.TabStrip1__Tab1ID13 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e13,width=50)
        self.TabStrip1__Tab1ID14 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e14,width=50)
        self.TabStrip1__Tab1ID15 = Entry(self.TabStrip1__Tab1,textvariable=self.TabStrip1__Tab1e15,width=50)

        self.TabStrip1__Tab1ID1.grid(row=1,column=3)
        #ID2.grid(row=2,column=3)
        self.TabStrip1__Tab1ID3.grid(row=3,column=3)
        self.TabStrip1__Tab1ID4.grid(row=4,column=3)
        self.TabStrip1__Tab1ID5.grid(row=5,column=3)
        self.TabStrip1__Tab1ID6.grid(row=6,column=3)
        self.TabStrip1__Tab1ID7.grid(row=7,column=3)
        self.TabStrip1__Tab1ID8.grid(row=8,column=3)
        self.TabStrip1__Tab1ID9.grid(row=9,column=3)
        self.TabStrip1__Tab1ID10.grid(row=10,column=3)
        self.TabStrip1__Tab1ID11.grid(row=11,column=3)
        self.TabStrip1__Tab1ID12.grid(row=12,column=3)
        self.TabStrip1__Tab1ID13.grid(row=13,column=3)
        self.TabStrip1__Tab1ID14.grid(row=14,column=3)
        self.TabStrip1__Tab1ID15.grid(row=15,column=3)

        self.TabStrip1__Tab1text = Text(self.TabStrip1__Tab1,width=50,height=8)
        self.TabStrip1__Tab1text.grid(row=16,column=1,columnspan=3,rowspan=1)
        button = Button(self.TabStrip1__Tab1,text='发送',command=self.Get_Connect).grid(row=17,column=0,columnspan=4)

        self.TabStrip1.add(self.TabStrip1__Tab1, text='集团用户')



        # tab2
        self.TabStrip1__Tab2 = Frame(self.TabStrip1)

        self.TabStrip1__Tab2variable = StringVar()
        self.TabStrip1__Tab2box = ttk.Combobox(self.TabStrip1__Tab2,width=20,textvariable= self.TabStrip1__Tab2variable,values=['0101 客户开通','0102 客户变更','0103 客户退订','0107 客户停机','0108 客户复机'])
        self.TabStrip1__Tab2box.current(0)
        self.TabStrip1__Tab2box.grid(row=2,column=3,sticky=W)

        self.TabStrip1__Tab2Lb0 = Label(self.TabStrip1__Tab2, text='').grid(row=0)
        self.TabStrip1__Tab2Lbl = Label(self.TabStrip1__Tab2, text='流水号：').grid(row=1)
        self.TabStrip1__Tab2Lb2 = Label(self.TabStrip1__Tab2, text='操作类型：').grid(row=2)
        self.TabStrip1__Tab2Lb3 = Label(self.TabStrip1__Tab2, text='产品ID：').grid(row=3)
        self.TabStrip1__Tab2Lb4 = Label(self.TabStrip1__Tab2, text='销售品ID：').grid(row=4)
        self.TabStrip1__Tab2Lb5 = Label(self.TabStrip1__Tab2, text='客户产品计费标识：').grid(row=5)
        self.TabStrip1__Tab2Lb6 = Label(self.TabStrip1__Tab2, text='区域：').grid(row=6)
        self.TabStrip1__Tab2Lb7 = Label(self.TabStrip1__Tab2, text='客户编码：').grid(row=7)
        self.TabStrip1__Tab2Lb8 = Label(self.TabStrip1__Tab2, text='客户账号：').grid(row=8)
        self.TabStrip1__Tab2Lb9 = Label(self.TabStrip1__Tab2, text='客户名称：').grid(row=9)
        self.TabStrip1__Tab2Lb10 = Label(self.TabStrip1__Tab2, text='固定电话：').grid(row=10)
        self.TabStrip1__Tab2Lb11 = Label(self.TabStrip1__Tab2, text='Email：').grid(row=11)
        self.TabStrip1__Tab2Lb12 = Label(self.TabStrip1__Tab2, text='faxCode：').grid(row=12)
        self.TabStrip1__Tab2Lb12 = Label(self.TabStrip1__Tab2, text='联系人：').grid(row=13)
        self.TabStrip1__Tab2Lb12 = Label(self.TabStrip1__Tab2, text='手机：').grid(row=14)
        self.TabStrip1__Tab2Lb12 = Label(self.TabStrip1__Tab2, text='地址：').grid(row=15)
        self.TabStrip1__Tab2Lb12 = Label(self.TabStrip1__Tab2, text='返回码：').grid(row=16)
        self.TabStrip1__Tab2Lb12 = Label(self.TabStrip1__Tab2, text='备注：').grid(row=17)
        self.TabStrip1__Tab2Lb12 = Label(self.TabStrip1__Tab2, text='响应结果：').grid(row=18)



        self.TabStrip1__Tab2e1 = StringVar()
        self.TabStrip1__Tab2e1.set('PLyuey!NAjd*Jb2y@hqOsKI%=BahK^$#')
        self.TabStrip1__Tab2e2 = StringVar()
        self.TabStrip1__Tab2e2.set('0202')
        self.TabStrip1__Tab2e3 = StringVar()
        self.TabStrip1__Tab2e3.set('Productid0000100')
        self.TabStrip1__Tab2e4 = StringVar()
        self.TabStrip1__Tab2e4.set('17000131')
        self.TabStrip1__Tab2e5 = StringVar()
        self.TabStrip1__Tab2e5.set('Bizid0000100')
        self.TabStrip1__Tab2e6 = StringVar()
        self.TabStrip1__Tab2e6.set('A0100')
        self.TabStrip1__Tab2e7 = StringVar()
        self.TabStrip1__Tab2e7.set('Custid0000100')
        self.TabStrip1__Tab2e8 = StringVar()
        self.TabStrip1__Tab2e8.set('CustAccount0001')
        self.TabStrip1__Tab2e9 = StringVar()
        self.TabStrip1__Tab2e9.set('集团CustName0000100')
        self.TabStrip1__Tab2e10 = StringVar()
        self.TabStrip1__Tab2e10.set('029-7456584')
        self.TabStrip1__Tab2e11 = StringVar()
        self.TabStrip1__Tab2e11.set('707150586@qq.com')
        self.TabStrip1__Tab2e12 = StringVar()
        self.TabStrip1__Tab2e12.set('faxCode0001')
        self.TabStrip1__Tab2e13 = StringVar()
        self.TabStrip1__Tab2e13.set('Linkman0001')
        self.TabStrip1__Tab2e14 = StringVar()
        self.TabStrip1__Tab2e14.set('17629298189')
        self.TabStrip1__Tab2e15 = StringVar()
        self.TabStrip1__Tab2e15.set('Address_0001')
        self.TabStrip1__Tab2e16 = StringVar()
        self.TabStrip1__Tab2e16.set('00000')
        self.TabStrip1__Tab2e17 = StringVar()
        self.TabStrip1__Tab2e17.set('用户查询成功')
        self.TabStrip1__Tab2ID1 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e1,width=50)
        self.TabStrip1__Tab2ID2 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e2,width=50)
        self.TabStrip1__Tab2ID3 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e3,width=50)
        self.TabStrip1__Tab2ID4 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e4,width=50)
        self.TabStrip1__Tab2ID5 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e5,width=50)
        self.TabStrip1__Tab2ID6 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e6,width=50)
        self.TabStrip1__Tab2ID7 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e7,width=50)
        self.TabStrip1__Tab2ID8 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e8,width=50)
        self.TabStrip1__Tab2ID9 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e9,width=50)
        self.TabStrip1__Tab2ID10 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e10,width=50)
        self.TabStrip1__Tab2ID11 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e11,width=50)
        self.TabStrip1__Tab2ID12 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e12,width=50)
        self.TabStrip1__Tab2ID13 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e13,width=50)
        self.TabStrip1__Tab2ID14 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e14,width=50)
        self.TabStrip1__Tab2ID15 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e15,width=50)
        self.TabStrip1__Tab2ID16 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e16,width=50)
        self.TabStrip1__Tab2ID17 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e17,width=50)

        self.TabStrip1__Tab2ID1.grid(row=1,column=3)
        #ID2.grid(row=2,column=3)
        self.TabStrip1__Tab2ID3.grid(row=3,column=3)
        self.TabStrip1__Tab2ID4.grid(row=4,column=3)
        self.TabStrip1__Tab2ID5.grid(row=5,column=3)
        self.TabStrip1__Tab2ID6.grid(row=6,column=3)
        self.TabStrip1__Tab2ID7.grid(row=7,column=3)
        self.TabStrip1__Tab2ID8.grid(row=8,column=3)
        self.TabStrip1__Tab2ID9.grid(row=9,column=3)
        self.TabStrip1__Tab2ID10.grid(row=10,column=3)
        self.TabStrip1__Tab2ID11.grid(row=11,column=3)
        self.TabStrip1__Tab2ID12.grid(row=12,column=3)
        self.TabStrip1__Tab2ID13.grid(row=13,column=3)
        self.TabStrip1__Tab2ID14.grid(row=14,column=3)
        self.TabStrip1__Tab2ID15.grid(row=15,column=3)
        self.TabStrip1__Tab2ID16.grid(row=16,column=3)
        self.TabStrip1__Tab2ID17.grid(row=17,column=3)

        self.TabStrip1__Tab2text = Text(self.TabStrip1__Tab2,width=50,height=8)
        self.TabStrip1__Tab2text.grid(row=18,column=1,columnspan=3,rowspan=1)

        button = Button(self.TabStrip1__Tab2,text='发送',command=self.Get_Connect2).grid(row=19,column=0,columnspan=4)

        self.TabStrip1.add(self.TabStrip1__Tab2, text='集团客户')

        # tab3
        self.TabStrip1__Tab3 = Frame(self.TabStrip1)
        self.TabStrip1__Tab3Lb0 = Label(self.TabStrip1__Tab3, text='').grid(row=0)
        self.TabStrip1__Tab3Lbl = Label(self.TabStrip1__Tab3, text='集团用户接口URL：').grid(row=1)
        self.TabStrip1__Tab3Lb2 = Label(self.TabStrip1__Tab3, text='集团客户接口URL：').grid(row=2)
        self.TabStrip1__Tab3e1 = StringVar()
        self.TabStrip1__Tab3e1.set('http://11.12.112.244:8183/ecms/api/saveEmp.do')
        self.TabStrip1__Tab3e2 = StringVar()
        self.TabStrip1__Tab3e2.set('http://11.12.112.244:8183/ecms/api/saveCus.do')
        self.TabStrip1__Tab3ID1 = Entry(self.TabStrip1__Tab3,textvariable=self.TabStrip1__Tab3e1,width=50)
        self.TabStrip1__Tab3ID2 = Entry(self.TabStrip1__Tab3,textvariable=self.TabStrip1__Tab3e2,width=50)
        self.TabStrip1__Tab3ID1.grid(row=1,column=3)
        self.TabStrip1__Tab3ID2.grid(row=2,column=3)
        self.TabStrip1.add(self.TabStrip1__Tab3, text='配置')




class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Get_Connect(self):

        now =  self.TabStrip1__Tab1box.get()[0:4]

        self.TabStrip1__Tab1text.delete(0.0,END)

        Args1 ={
            "opFlag":now,
            "emp":"<?xml version=\"1.0\"  encoding=\"UTF-8\"?><Package><StreamingNo>"+self.TabStrip1__Tab1ID1.get()+"</StreamingNo><OPFlag>"+now+"</OPFlag><ProductID>"+self.TabStrip1__Tab1ID3.get()+"</ProductID><OfferID>"+self.TabStrip1__Tab1ID4.get()+"</OfferID><BizID>"+self.TabStrip1__Tab1ID5.get()+"</BizID><AreaCode>"+self.TabStrip1__Tab1ID6.get()+"</AreaCode><CustID>"+self.TabStrip1__Tab1ID7.get()+"</CustID><CustName>"+self.TabStrip1__Tab1ID8.get()+"</CustName><UserID>"+self.TabStrip1__Tab1ID9.get()+"</UserID><AccType>"+self.TabStrip1__Tab1ID10.get()+"</AccType><AccName>"+self.TabStrip1__Tab1ID11.get()+"</AccName><ProductInfo><Product><ProductType>name</ProductType><ProductValue>"+self.TabStrip1__Tab1ID12.get()+"</ProductValue><ParentType></ParentType><AttributeAttach></AttributeAttach></Product><Product><ProductType>fee</ProductType><ProductValue>"+self.TabStrip1__Tab1ID13.get()+"</ProductValue><ParentType></ParentType><AttributeAttach></AttributeAttach></Product></ProductInfo><ReturnStatus>"+self.TabStrip1__Tab1ID14.get()+"</ReturnStatus><Summary>"+self.TabStrip1__Tab1ID15.get()+"</Summary></Package>"
        }
        Args =  json.dumps(Args1)
        print (Args)

        #Url='http://11.12.112.244:8183/ecms/api/saveEmp.do'
        Url = self.TabStrip1__Tab3ID1.get()
        headers = {"Content-Type":"application/json"}
        try:
            r =requests.post(Url,Args,headers = headers)
            print (r.json())
            self.TabStrip1__Tab1text.insert(INSERT,self.TabStrip1__Tab1box.get())
            self.TabStrip1__Tab1text.insert(INSERT,'----')
            self.TabStrip1__Tab1text.insert(INSERT,r.json()['result'])
            self.TabStrip1__Tab1text.insert(INSERT,"\n结果: "+str(r.json()['success']))

        except Exception as e:
            print (e)
            self.TabStrip1__Tab1text.insert(INSERT,e)
            self.TabStrip1__Tab1text.insert(INSERT, "请求失败！检查URL是否正确~")
    def Get_Connect2(self):

        now =  self.TabStrip1__Tab1box.get()[0:4]

        self.TabStrip1__Tab2text.delete(0.0,END)

        Args1 ={
            "opFlag":now,
            "cus":"<?xml version=\"1.0\"  encoding=\"UTF-8\"?><Package><StreamingNo>"+self.TabStrip1__Tab2ID1.get()+"</StreamingNo><OPFlag>"+now+"</OPFlag><ProductID>"+self.TabStrip1__Tab2ID3.get()+"</ProductID><OfferID>"+self.TabStrip1__Tab2ID4.get()+"</OfferID><BizID>"+self.TabStrip1__Tab2ID5.get()+"</BizID><AreaCode>"+self.TabStrip1__Tab2ID6.get()+"</AreaCode><CustID>"+self.TabStrip1__Tab2ID7.get()+"</CustID><CustAccount>"+self.TabStrip1__Tab2ID8.get()+"</CustAccount><CustName>"+self.TabStrip1__Tab2ID9.get()+"</CustName><ProductInfo><Product><ProductInstID>1</ProductInstID><ProductType>phone</ProductType><ProductValue>"+self.TabStrip1__Tab2ID10.get()+"</ProductValue><ParentType></ParentType><ProductParentInstID></ProductParentInstID><AttributeAttach></AttributeAttach></Product><Product><ProductInstID>2</ProductInstID><ProductType>email</ProductType><ProductValue>"+self.TabStrip1__Tab2ID11.get()+"</ProductValue><ParentType></ParentType><ProductParentInstID></ProductParentInstID><AttributeAttach></AttributeAttach></Product><Product><ProductInstID>3</ProductInstID><ProductType>faxCode</ProductType><ProductValue>"+self.TabStrip1__Tab2ID12.get()+"</ProductValue><ParentType></ParentType><ProductParentInstID></ProductParentInstID><AttributeAttach></AttributeAttach></Product><Product><ProductInstID>4</ProductInstID><ProductType>linkMan</ProductType><ProductValue>"+self.TabStrip1__Tab2ID13.get()+"</ProductValue><ParentType></ParentType><ProductParentInstID></ProductParentInstID><AttributeAttach></AttributeAttach></Product><Product><ProductInstID>5</ProductInstID><ProductType>mobile</ProductType><ProductValue>"+self.TabStrip1__Tab2ID14.get()+"</ProductValue><ParentType></ParentType><ProductParentInstID></ProductParentInstID><AttributeAttach></AttributeAttach></Product><Product><ProductInstID>6</ProductInstID><ProductType>address</ProductType><ProductValue>"+self.TabStrip1__Tab2ID15.get()+"</ProductValue><ParentType></ParentType><ProductParentInstID></ProductParentInstID><AttributeAttach></AttributeAttach></Product></ProductInfo><ReturnStatus>"+self.TabStrip1__Tab2ID16.get()+"</ReturnStatus><Summary>"+self.TabStrip1__Tab2ID17.get()+"</Summary></Package>"
        }
        Args =  json.dumps(Args1)
        print (Args)

        #Url='http://11.12.112.244:8183/ecms/api/saveEmp.do'
        Url = self.TabStrip1__Tab3ID2.get()
        headers = {"Content-Type":"application/json"}
        try:
            r =requests.post(Url,Args,headers = headers)
            print (r.json())

            self.TabStrip1__Tab2text.insert(INSERT,self.TabStrip1__Tab2box.get())
            self.TabStrip1__Tab2text.insert(INSERT,'----')
            self.TabStrip1__Tab2text.insert(INSERT,r.json()['result'])
            self.TabStrip1__Tab2text.insert(INSERT,"\n结果: "+str(r.json()['success']))

        except Exception as e:
            print (e)
            self.TabStrip1__Tab2text.insert(INSERT,e)
            self.TabStrip1__Tab2text.insert(INSERT, "请求失败！检查URL是否正确~")


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()