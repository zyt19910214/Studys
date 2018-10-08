# -*- coding: utf-8 -*-
"""
  ---------------------------
  @File: Random_Chars.py
  @Author: zyt
  @Date: 2017/11/20 9:47
  @Software: Pycharm
  @Version: Python2.7
  ---------------------------
"""
import random
import string
import Tkinter
from Tkinter import *

top =Tkinter.Tk()
top.title("字符生成器")
Label1 =Label(top,text="字符串长度：").grid(row=0)
Label2 =Label(top,text="必须存在的字符：").grid(row=1)

sel1 = Tkinter.IntVar()
chk1 = Tkinter.Checkbutton(top,text="数字",variable=sel1)
sel2 = Tkinter.IntVar()
chk2 = Tkinter.Checkbutton(top,text="大写字母",variable=sel2)
sel3 = Tkinter.IntVar()
chk3 = Tkinter.Checkbutton(top,text="小写字母",variable=sel3)
sel4 = Tkinter.IntVar()
chk4 = Tkinter.Checkbutton(top,text="特殊字符",variable=sel4)
e = StringVar()
e.set('100')
e2 = StringVar()
e2.set('%^*')


ID1 = Entry(top,textvariable=e,width=60)
ID2 = Entry(top,textvariable=e2,width=60)
ID1.grid(row=0,column=3)
ID2.grid(row=1,column=3)
chk1.grid(row=3,column=0)
chk2.grid(row=3,column=1)
chk3.grid(row=4,column=0)
chk4.grid(row=4,column=1)
text = Text(top,width=60,height=15)
text.grid(row=3,column=3,columnspan=4,rowspan=2)



def my_chars():
    text.delete(0.0,END)
    need_length = int(ID1.get())

    list = []
    int_list = [i for i in range(48, 58)]
    upChar_list = [i for i in range(65, 91)]
    downChar_list = [i for i in range(97, 123)]
    specialChar_list = [i for i in range(33, 48)]
    l2 = [i for i in range(58, 65)]
    l3 = [i for i in range(91, 97)]
    l4 = [i for i in range(123, 127)]
    specialChar_list.extend(l2)
    specialChar_list.extend(l3)
    specialChar_list.extend(l4)

    stringList = []
    ran_str = ''
    stringList.append(str(sel1.get()))
    stringList.append(str(sel2.get()))
    stringList.append(str(sel3.get()))
    stringList.append(str(sel4.get()))
    ran_str = ''.join(stringList)
    print ran_str
    if ran_str == '1000':
        list = creat_random(int_list,need_length)
    elif ran_str == '0100':
        list = creat_random(upChar_list, need_length)
    elif ran_str == '0010':
        list = creat_random(downChar_list, need_length)
    elif ran_str == '0001':
        list = creat_random(specialChar_list, need_length)
    elif ran_str == '1100':
        # 数字+大写字母
        int_upChar_list = []
        int_upChar_list.extend(int_list)
        int_upChar_list.extend(upChar_list)
        list = creat_random(int_upChar_list, need_length)
    elif ran_str == '1010':
        # 数字+小写字母
        int_downChar_list = []
        int_downChar_list.extend(int_list)
        int_downChar_list.extend(downChar_list)
        list = creat_random(int_downChar_list, need_length)
    elif ran_str == '1001':
        # 数字+特殊字符
        int_special_list = []
        int_special_list.extend(int_list)
        int_special_list.extend(specialChar_list)
        list = creat_random(int_special_list, need_length)
    elif ran_str == '0110':
        # 小写字母+大写字母
        upChar_downChar_list = []
        upChar_downChar_list.extend(upChar_list)
        upChar_downChar_list.extend(downChar_list)

        list = creat_random(upChar_downChar_list, need_length)
    elif ran_str == '0011':
        # 小写字母+特殊字符
        downChar_special_list = []
        downChar_special_list.extend(downChar_list)
        downChar_special_list.extend(specialChar_list)
        list = creat_random(downChar_special_list, need_length)
    elif ran_str == '0101':
        # 大写字母+特殊字符
        upChar_special_list = []
        upChar_special_list.extend(upChar_list)
        upChar_special_list.extend(specialChar_list)
        list = creat_random(upChar_special_list, need_length)
    elif ran_str == '1110':
        # 数字+小写字母+大写字母
        int_upChar_downChar_list = []
        int_upChar_downChar_list.extend(int_list)
        int_upChar_downChar_list.extend(upChar_list)
        int_upChar_downChar_list.extend(downChar_list)
        list = creat_random(int_upChar_downChar_list, need_length)
    elif ran_str == '1101':
        # 数字+大写祖母+特殊字符
        int_upChar_special_list = []
        int_upChar_special_list.extend(int_list)
        int_upChar_special_list.extend(upChar_list)
        int_upChar_special_list.extend(specialChar_list)
        list = creat_random(int_upChar_special_list, need_length)
    elif ran_str == '1011':
        # 数字+小写字母+特殊字符
        int_downChar_special_list = []
        int_downChar_special_list.extend(int_list)
        int_downChar_special_list.extend(downChar_list)
        int_downChar_special_list.extend(specialChar_list)
        list = creat_random(int_downChar_special_list, need_length)
    elif ran_str == '0111':
        # 小写字母+大写字母+特殊字符
        upChar_downChar_special_list = []
        upChar_downChar_special_list.extend(specialChar_list)
        upChar_downChar_special_list.extend(upChar_list)
        upChar_downChar_special_list.extend(downChar_list)
        list = creat_random(upChar_downChar_special_list, need_length)
    elif ran_str == '1111':
        # all
        all_list = []
        all_list.extend(int_list)
        all_list.extend(upChar_list)
        all_list.extend(downChar_list)
        all_list.extend(specialChar_list)
        list = creat_random(all_list, need_length)
    else:
        print '参数错误'
        text.insert(INSERT, '参数错误，请重新输入')

    need_char = ID2.get()



    for i in range(len(need_char)):
        index = random.randint(0,need_length-1)
        if need_char[i] not in list:
            if list[index] not in need_char:
                print '替换%s为必须存在的字符...%s' % (list[index], need_char[i])
                list[index] = need_char[i]

    ran_str = ''.join(list)
    print ran_str
    text.insert(INSERT,ran_str)

def creat_random(now_list,len1):
    my_list=[]
    for x in range(len1):
        n = random.sample(now_list, 1)
        my_list.append(chr(n[0]))
    return my_list

button = Button(top,text='查询',command=my_chars).grid(row=5,column=0,columnspan=4)
top.mainloop()
