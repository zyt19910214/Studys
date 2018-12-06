# -*- coding: utf-8 -*-
"""
  ---------------------------
  @File: PersonTp_generate.py
  @Author: zyt
  @Date: 2018/12/5 16:20
  @Software: Pycharm
  @Version: Python2.7
  @dec: 生成ECSS人员模板导入数据
  ---------------------------
"""

import Tkinter
from Tkinter import *
from tkMessageBox import  *
import MutiTools
import random
import threading

reload(sys)
sys.setdefaultencoding('utf-8')

top =Tkinter.Tk()
Label0 =Label(top,text="ECSS人员导入数据生成工具",font=('Helvetica',18)).grid(row=0,columnspan=3)
Label1 =Label(top,text="工具使用说明：\n 1.人员数量为生成的总人数（取值：1000的倍数） \n 2.参照dept.txt中部门路径在ECSS中创建部门 \n 3.多个部门用英文逗号分隔",justify=LEFT,fg='red').grid(row=2,column=2,rowspan=3)
Label2 =Label(top,text="人员数量：").grid(row=2,)
Label3 =Label(top,text="根部门名称：").grid(row=3)
Label4 =Label(top,text="二级部门名称：").grid(row=4)
Label5 =Label(top,text="三级部门名称：").grid(row=5)

e1 = StringVar()
e1.set('3000')
e2 = StringVar()
e2.set('信大捷安测试专用')
e3 = StringVar()
e3.set('西安研究院,郑州总部,北京分公司,上海分公司,深圳分公司')
e4 = StringVar()
e4.set('测试部,开发部,设计部,人事部,行政部,财务部,审计部')

ID1 = Entry(top,textvariable=e1,width=80)
ID2 = Entry(top,textvariable=e2,width=80)
ID3 = Entry(top,textvariable=e3,width=80)
ID4 = Entry(top,textvariable=e4,width=80)

ID1.grid(row=2,column=1)
ID2.grid(row=3,column=1)
ID3.grid(row=4,column=1)
ID4.grid(row=5,column=1)

def pa():
    person_num = int(ID1.get())
    # 构造name
    name_list = MutiTools.get_faker_data('name', person_num)
    data_dic = {}
    data_dic[0] = name_list

    # 构造性别
    sex = ['男', '女']
    sex_list = [sex[random.randint(0, 1)] for x in range(person_num)]
    data_dic[1] = sex_list

    # 构造排序号
    sort_list = [str(x + 1) for x in range(0, person_num)]
    data_dic[4] = sort_list

    # 构造手机号
    phone_list = MutiTools.get_faker_data('phone', person_num)
    data_dic[5] = phone_list

    # 构造邮箱
    email_list = MutiTools.get_faker_data('email', person_num)
    data_dic[6] = email_list

    # # 构造固定电话和传真
    tel_list = ['029-' + str(x + 1).rjust(7, '0') for x in range(0, person_num)]
    data_dic[7] = tel_list
    data_dic[8] = tel_list

    # # 构造job
    job_list = MutiTools.get_faker_data('job', person_num)
    data_dic[9] = job_list
    data_dic[10] = job_list

    # 构造工号
    jobNum_list = [str(x + 1).rjust(8, '0') for x in range(0, person_num)]
    data_dic[11] = jobNum_list

    # # 构造address
    address_list = MutiTools.get_faker_data('address', person_num)
    data_dic[12] = address_list

    # 构造部门
    dept_list = []

    # 根部门名称
    l1 = ID2.get().strip()
    dept_list.append(l1)

    # 二级部门
    l2 = [l2d.strip() for l2d in ID3.get().split(',')]
    for x in l2:
        dept_list.append(l1 + '>' + x)

    # 三级部门
    l3 = [l3d.strip() for l3d in ID4.get().split(',')]
    for x in l3:
        for y in l2:
            dept_list.append(l1 + '>' + y + '>' + y + u'的' + x)

    # 所有部门名称保存到dept.txt中
    with open('dept.txt', 'w') as f:
        for x in dept_list:
            f.write(x + '\n')

    dept_list2 = [dept_list[i % len(dept_list)] for i in range(0, person_num)]
    data_dic[2] = dept_list2

    # 构造组织
    zz_list = [l1 for x in range(0, person_num)]
    data_dic[3] = zz_list

    import xlrd
    from xlutils3.copy import copy

    old_excel = xlrd.open_workbook('pt2.xls', formatting_info=True)
    new_excel = copy(old_excel)
    ws = new_excel.get_sheet(0)
    for x in range(0, int(ID1.get()) / 1000):
        try:
            for key, value in data_dic.items():
                now = value[1000 * (x):1000 * (x + 1)]
                for y in range(len(now)):
                    ws.write(3 + y, key, now[y].decode('utf-8'))
        except Exception as e:
            raise e

        new_excel.save('personTemplate' + str(x + 1) + '.xls')
    showinfo(title='提示',message='数据生成完成！\n人员：'+str(person_num)+'人\n部门：'+str(len(dept_list))+'个')


button = Button(top,text='生成数据',comman=pa).grid(row=6,column=2)


top.mainloop()
