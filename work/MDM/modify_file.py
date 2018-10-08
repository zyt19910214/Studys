# -*- coding: utf-8 -*-
# @File  : modify_file.py
# @Author: zyt
# @Date  : 2018/9/4 16:09
# @Desc  : MDM　PC客户端升级借助准生产，修改配置文件


from __future__ import print_function
import ctypes, sys
import os
import shutil

path1 = 'C:\\ClientVer.xml'
path2 = 'C:\\Program Files (x86)\\mdmgr\\ClientVer.xml'
path3 = 'Z:\\1.xml'
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    all_list = os.listdir(u"C:\\")
    all_list2 = os.listdir(u"C:\\Program Files (x86)\\mdmgr\\")
    if 'ClientVer.xml' in all_list:
        try:
            os.remove(path1)
            shutil.copyfile(path3, path1)
        except Exception as e:
            raise e
    else:
        try:
            shutil.copyfile(path3, path1)
        except Exception as e:
            raise e

    if 'ClientVer.xml' in all_list2:
        try:
            os.remove(path2)
            shutil.copyfile(path3, path2)
        except Exception as e:
            raise e
    else:
        try:
            shutil.copyfile(path3, path2)
        except Exception as e:
            raise e

else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else: #in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)


