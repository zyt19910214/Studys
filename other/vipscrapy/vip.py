# -*- coding: utf-8 -*-
"""
  ---------------------------
  @File: tk.py
  @Author: zyt
  @Date: 2017/12/6 9:03
  @Software: Pycharm
  @Version: Python2.7
  ---------------------------
"""


import os, sys
import ttk
import json
import requests
import webbrowser
import  time
from scrapy import cmdline

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
        self.master.title('VIP视频点播平台')
        self.master.geometry('425x720')
        self.createWidgets()


    def createWidgets(self):
        self.top = self.winfo_toplevel()
        self.style = Style()

        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.062, rely=0.071, relwidth=0.887, relheight=0.876)

        # tab1
        self.TabStrip1__Tab1 =Frame(self.TabStrip1)
        self.TabStrip1__Tab1variable = StringVar()

        self.TabStrip1__Tab1Lbl = Label(self.TabStrip1__Tab1, font = ('楷体',20),text='播放列表').grid(row=0,column=0,columnspan=4,rowspan=1,sticky=W)
        self.TabStrip1__Tab1listb = Listbox(self.TabStrip1__Tab1, height=30, width=52, selectmode=BROWSE)


        global records
        for r in records:
            try:
                self.TabStrip1__Tab1listb.insert(1, r['name'])
            except Exception as e:
                pass
        Button(self.TabStrip1__Tab1, text='刷新', command=self.refresh_list).grid(row=0,column=2,rowspan=1,sticky=E)
        Button(self.TabStrip1__Tab1, text='播放', command=self.start).grid(row=0,column=3,rowspan=1,sticky=W)
        self.TabStrip1__Tab1listb.grid(row=2,column=0,columnspan=4,rowspan=4)
        sl = Scrollbar(self.TabStrip1__Tab1)
        self.TabStrip1__Tab1listb.see(50)
        self.TabStrip1__Tab1listb['yscrollcommand'] = sl.set
        sl.grid(row=2,columnspan=4,rowspan=4,sticky='NSE')
        sl['command'] =   self.TabStrip1__Tab1listb.yview
        self.TabStrip1.add(self.TabStrip1__Tab1, text='爱奇艺')

        # tab2
        self.TabStrip1__Tab3 = Frame(self.TabStrip1)

        self.TabStrip1.add(self.TabStrip1__Tab3, text='腾讯')


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def refresh_list(self):
        global records
        self.TabStrip1__Tab1listb.delete(0, END)
        for r in records:
            try:
                self.TabStrip1__Tab1listb.insert(1, r['name'])
            except Exception as e:
                pass
    def start(self):
        cmdline.execute("scrapy crawl vip".split())
        records = [json.loads(regex.sub(r"\\\\", line).replace("'", '"')) for line in open('info.json')]

        num = self.TabStrip1__Tab1listb.curselection()[0]
        print(records[(len(records) - num - 1)]['name']+'  '+records[(len(records) - num-1)]['url'])
        webbrowser.open(records[(len(records) - num-1)]['url'])

if __name__ == "__main__":

    regex = re.compile(r'\\(?![/u"])')
    records = [json.loads(regex.sub(r"\\\\", line).replace("'", '"')) for line in open('info.json')]
    top = Tk()
    Application(top).mainloop()