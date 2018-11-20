#-*- coding:utf-8 -*-
import os
from ctypes import *
import ctypes, sys
import time


class dirver(object):

    def __init__(self):
        # print(os.getcwd())
        self.test = cdll.LoadLibrary(os.getcwd() + '\\release\\MdmDriverApi.dll')

    # 启动驱动
    def startDrivers(self):
        return self.test.MdmStartDrivers()


    # 停止驱动
    def stopDrivers(self):
        return self.test.MdmStopDrivers()


    # 安装Mdm所有的驱动
    def installDriver(self):
        return self.test.MdmInstallDrivers()


    # 卸载Mdm所有的驱动
    def uninstallDriver(self):
        return self.test.MdmUninstallDrivers()


    # 使能文件或者文件保护
    def enable_file_protect(self):
        return self.test.EnableFileDirProtect()


    # 禁能文件或者文件保护
    def disable_file_protect(self):
        return self.test.DisableFileDirProtect()

if __name__ == "__main__":

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        try:
            dirver().uninstallDriver()
            time.sleep(4)


        except Exception as e:
            print(e)
            os.system('pause')
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

