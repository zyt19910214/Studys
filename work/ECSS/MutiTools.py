# -*- coding: utf-8 -*-
"""
  ---------------------------
  @File: MutiTools.py
  @Author: zyt
  @Date: 2017/12/29 10:59
  @Software: Pycharm
  @Version: Python2.7
  ---------------------------
"""
import datetime
import os
import time
from faker import Faker



def my_split(my_string,split_byl):
    """
    将字符串拆分为list
    @param my_string:指定字符串
    @param split_byl:分割符
    return:list
    """
    my_list = my_string.split(split_byl)

    return my_list


def rename_file(file_name):
    """
    修改已存在文件的名称，前缀前日期,格式为%Y%m%d%H%M%S
    @param file_name:原文件名称
    return: 带日期的重命名文件名称
    """
    name_list = my_split(file_name,".")
    # 获取当前时间，并格式化
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    # 组合当前文件名，并修改
    new_file_name = name_list[0]+'_'+str(now_time)+'.'+name_list[1]
    os.renames(file_name,new_file_name)
    print(name_list[0]+u'已修改为：'+new_file_name)


def get_add_zero_str(str,length):
    """
    指定字符串str前补0到length位
    @param str: 已存在的指定字符串
    @param length: 需要的字符串长度
    return:length位带0的str
    """
    ling_list = []
    for x in range(length-len(str)):
        ling_list.append('0')
    s = ''.join(ling_list) + str
    return s


def get_add_head_str(str1, i):
    """
    指定长度字符串str1后面变为i
    @param str1: 已存在的指定字符串
    @param i: 当前值
    return:
    """
    s = str1[:-len(str(i))] + str(i)
    return s


def get_column_from_txt(table_name,num):
    """
    获取生成的数据的某一列的值
    @param table_name: 去.txt的文件名称
    @param num: 列数
    return:某列的值list
    """
    column_list = []
    f = open(os.getcwd()+'/data/'+table_name+'.txt','r')
    line = f.readline()
    while line:
        column_list.append(line.split('|')[num].strip())
        line = f.readline()
    return column_list

def get_one_line_from_txt(table_name):
    """
    获取生成的数据的某一列的值
    @param table_name: 去.txt的文件名称
    @param num: 列数
    return:某列的值list
    """
    line_list = []
    f = open(os.getcwd()+'/data/'+table_name+'.txt','r')
    line = f.readline()
    if line:
        return line
    else:
        print('文件为空')


def get_all_line_from_conf(table_name):
    f = open(os.getcwd() + '/config/' + table_name + '.txt', 'r')
    lines = f.readlines()
    if lines:
        return lines
    else:
        print('文件为空')

def get_valid_line_from_txt(table_name,num,num2,str):
    """
    获取生成的数据的某一列的值获取另一列的值
    @param table_name: 去.txt的文件名称
    @param num: 依据列数
    @param num2: 获取的列数
    @param str: 匹配字符
    return:某列的值list
    """
    valid_list = []
    f = open(os.getcwd()+'/data/'+table_name+'.txt','r')
    line = f.readline()
    while line:
        split_list = line.split('|')
        if split_list[num].strip() == str:
            valid_list.append(split_list[num2])
        line = f.readline()
    return valid_list

def get_valid_line_from_conf(table_name,num,num2,str):
    """
    获取生成的数据的某一列的值获取另一列的值
    @param table_name: 去.txt的文件名称
    @param num: 依据列数
    @param num2: 获取的列数
    @param str: 匹配字符
    return:某列的值list
    """
    valid_list = []
    f = open(os.getcwd()+'/config/'+table_name+'.txt','r')
    line = f.readline()
    while line:
        split_list = line.split('|')
        if split_list[num].strip() == str:
            valid_list.append(split_list[num2])
        line = f.readline()
    return valid_list

def get_valid_lines_from_txt(table_name,num,str):
    valid_list = []
    f = open(os.getcwd() + '/data/' + table_name + '.txt', 'r')
    line = f.readline()
    while line:
        split_list = line.split('|')
        if split_list[num].strip() == str:
            valid_list.append(split_list)
        line = f.readline()
    return valid_list

def get_column_from_conf(table_name,num):
    """
    获取生成的数据的某一列的值
    @param table_name: 去.txt的文件名称
    @param num: 列数
    return:某列的值list
    """
    column_list = []
    f = open(os.getcwd()+'/config/'+table_name+'.txt','r')
    line = f.readline()
    while line:
        column_list.append(line.split('|')[num])
        line = f.readline()
    return column_list

def get_id_from_conf(str):
    try:
        n_id = 0
        f = open(os.getcwd()+'/config/id.txt','r')
        line= f.readline()
        while line:
            if str in line:
                n_id = line.split(':')[1]
                break
            else:
                line = f.readline()
        if n_id != 0:
            return n_id
        else:
            print("不存在自增id")
    except Exception as e:
         print(e)


def get_faker_data(name,num):
    """
    使用faker生成不重复的固定个数的数据，并返回data_list
    @param name: 需要生成的数据类型
    @param num: 数据个数
    @return: 生成的数据list
    """
    fake = Faker(locale='zh_CN')
    data_list = []
    if name == 'name':
        while True:
            one_name = fake.name()
            data_list.append(one_name.encode('utf-8'))
            if len(data_list) == num:
                break
    if name == 'address':
        while True:
            address = fake.address()
            data_list.append(address.encode('utf-8'))
            if len(data_list) == num:
                break
    if name == 'job':
        while True:
            job = fake.job()
            data_list.append(job.encode('utf-8').replace('/',''))
            if len(data_list) == num:
                break
    if name == 'email':
        while True:
            job = fake.email()
            data_list.append(job.encode('utf-8').replace('/', ''))
            data_set = set(data_list)
            if len(data_set) == num:
                break
        data_list = list(data_set)
    if name == 'dept':
        while True:
            job = fake.company_suffix()
            data_list.append(job.encode('utf-8').replace('/', ''))
            if len(data_list) == num:
                break
    if name == 'company':
        while True:
            company = fake.company()
            data_list.append(company.encode('utf-8').replace('/', ''))
            if len(data_list) == num:
                break
    if name == 'phone':
        while True:
            phone = fake.phone_number()
            data_list.append(phone.encode('utf-8').replace('/', ''))
            data_set = set(data_list)
            if len(data_set) == num:
                break
            data_list = list(data_set)
    return data_list


def get_now_utc_time():
    """
    获取当前utc秒值
    :return:
    """
    now_utc_time = int(round(time.time()*1000))
    return str(now_utc_time)

def get_tree_c_code(num):
    if num <= 0:
        return 'error'
    else:
        l,l2 = [x for x in range(10)],[]

        l.extend([chr(x) for x in range(65,91)])
        for x in l:
            for i in l:
                l2.append(str(x)+str(i))
        return l2[num-1]

if __name__ == '__main__':
    print get_tree_c_code(1200)

