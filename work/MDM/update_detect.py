# -*- coding: utf-8 -*-
# @File  : update_detect.py
# @Author: zyt
# @Date  : 2018/9/10 20:37
# @Desc  : 读取updatelog.txt文件，检测到升级后停止网络


from __future__ import print_function
import ctypes, sys
import os
import time

path1 = 'C:\\updatelog.txt'
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    path1 = 'C:\\update_s.xml'
    try:

        while True:
            if os.path.exists(path1):
                #x = os.popen('netsh interface set interface "wlan 7" disable', 'r')
                x = os.popen('netsh interface show interface' , 'r')
                result = x.read()
                x.close()
                print(result)
                break
            else:

                print('no update detect')

    except Exception as e:
        print(e)
        os.system('pause')
    os.system('pause')
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else: #in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)


