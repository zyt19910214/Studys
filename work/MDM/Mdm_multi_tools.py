#-*- coding:utf-8 -*-
from __future__ import print_function
import ctypes, sys
import os
import time
import os, sys
import ttk
import threading
import shutil
import json
import subprocess
from dll_learn import dirver

if sys.version_info[0] == 2:

    from Tkinter import *
    from tkFont import Font
    from ttk import *
    # Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    import tkMessageBox
    from tkMessageBox import *

    # Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    # import tkFileDialog
    # import tkSimpleDialog
else:  # Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    from tkinter import scrolledtext
    import tkinter.messagebox
    # import tkinter.filedialog as tkFileDialog
    # import tkinter.simpledialog as tkSimpleDialog    # askstring()


class Application_ui(Frame):

    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('MDM 测试工具')
        self.master.geometry('600x400')
        self.createWidgets()

    def createWidgets(self):

        self.top = self.winfo_toplevel()
        self.style = Style()

        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.062, rely=0.071, relwidth=0.887, relheight=0.876)

        # tab1
        self.TabStrip1__Tab1 = Frame(self.TabStrip1)
        self.TabStrip1__Tab1Lbl = Label(self.TabStrip1__Tab1, text='').grid(row=0)
        self.TabStrip1__Tab2Lbl = Label(self.TabStrip1__Tab1, text='功能描述：读取当前策略').grid(row=1,
                                                                                                              column=0,
                                                                                                           columnspan=2,sticky=W)
        self.TabStrip1__Tab1Lbl = Label(self.TabStrip1__Tab1, text='当前策略').grid(row=2)
        self.TabStrip1__Tab1e1 = StringVar()
        self.TabStrip1__Tab1e1.set('C:\\Program Files (x86)\\mdmgr\\Startegy.json')
        self.TabStrip1__Tab1text = Text(self.TabStrip1__Tab1,width=65,height=16)
        self.TabStrip1__Tab1text.grid(row=2,column=1,columnspan=3,rowspan=1)
        button1 = Button(self.TabStrip1__Tab1, text='嵌入式系统', command=self.Change_to_qrs).grid(row=3, column=1, columnspan=1)
        button2 = Button(self.TabStrip1__Tab1, text='非嵌入式系统', command=self.Change_to_fqrs).grid(row=3, column=2, columnspan=1)
        button = Button(self.TabStrip1__Tab1,text='查询',command=self.Get_startage).grid(row=3,column=3,columnspan=1)
        self.TabStrip1.add(self.TabStrip1__Tab1, text='查看策略')


        # tab2
        self.TabStrip1__Tab2 = Frame(self.TabStrip1)
        self.TabStrip1__Tab2Lb0 = Label(self.TabStrip1__Tab2, text='').grid(row=0)
        self.TabStrip1__Tab2Lbl = Label(self.TabStrip1__Tab2, text='功能描述：读取updatelog.txt文件，检测到升级后停止网络').grid(row=1, column=0,columnspan=2,sticky=W)
        self.TabStrip1__Tab2Lb12 = Label(self.TabStrip1__Tab2, text='响应结果').grid(row=3)
        self.TabStrip1__Tab2Lb2 = Label(self.TabStrip1__Tab2, text='网口名称').grid(row=2, column=0, columnspan=1)
        self.TabStrip1__Tab2e1 = StringVar()
        self.TabStrip1__Tab2e1.set('WLAN')
        self.TabStrip1__Tab2text = Text(self.TabStrip1__Tab2, width=65, height=16)
        self.TabStrip1__Tab2text.grid(row=3, column=1, columnspan=3, rowspan=1)
        self.TabStrip1__Tab2ID1 = Entry(self.TabStrip1__Tab2,textvariable=self.TabStrip1__Tab2e1,width=50)
        self.TabStrip1__Tab2ID1.grid(row=2,column=1,columnspan=3,sticky=W)
        button = Button(self.TabStrip1__Tab2,text='开始',command=self.update_detect).grid(row=4,column=3,columnspan=1)
        button = Button(self.TabStrip1__Tab2, text='恢复网络', command=self.back_net).grid(row=4, column=2, columnspan=1)

        self.TabStrip1.add(self.TabStrip1__Tab2, text='升级断网')


        # tab3
        self.TabStrip1__Tab3 = Frame(self.TabStrip1)
        self.TabStrip1__Tab3Lb0 = Label(self.TabStrip1__Tab3, text='').grid(row=0)
        self.TabStrip1__Tab3Lbl = Label(self.TabStrip1__Tab3, text='功能描述：MDMPC客户端升级借助准生产，修改升级配置文件').grid(row=1,column=0,columnspan=2,sticky=W)
        self.TabStrip1__Tab3Lb2 = Label(self.TabStrip1__Tab3, text='文件路径').grid(row=2,column=0,columnspan=1)
        self.TabStrip1__Tab3Lb2 = Label(self.TabStrip1__Tab3, text='响应结果').grid(row=3, column=0, columnspan=1,sticky=W)
        self.TabStrip1__Tab3e1 = StringVar()
        self.TabStrip1__Tab3e1.set('C:\\1.xml')
        self.TabStrip1__Tab3text = Text(self.TabStrip1__Tab3, width=60, height=16)
        self.TabStrip1__Tab3text.grid(row=3, column=1, columnspan=3, rowspan=1)
        self.TabStrip1__Tab3ID1 = Entry(self.TabStrip1__Tab3,textvariable=self.TabStrip1__Tab3e1,width=50)
        self.TabStrip1__Tab3ID1.grid(row=2,column=1,columnspan=3,sticky=W)
        button = Button(self.TabStrip1__Tab3, text='修改', command=self.modify_file).grid(row=4, column=2, columnspan=1)

        self.TabStrip1.add(self.TabStrip1__Tab3, text='修改升级文件')

        # tab4
        self.TabStrip1__Tab4 = Frame(self.TabStrip1)
        self.TabStrip1__Tab4Lb0 = Label(self.TabStrip1__Tab4, text='').grid(row=0)
        self.TabStrip1__Tab4Lbl = Label(self.TabStrip1__Tab4, text='功能描述：开启驱动签名检测，关闭驱动签名检测').grid(row=1,column=0,columnspan=2,sticky=W)

        button1 = Button(self.TabStrip1__Tab4, text='开启驱动签名检测', command=self.open_detective_qd).grid(row=2, column=1,columnspan=1)
        button2 = Button(self.TabStrip1__Tab4, text='关闭驱动签名检测', command=self.stop_detective_qd).grid(row=2, column=2, columnspan=1)
        self.TabStrip1__Tab4Lb2 = Label(self.TabStrip1__Tab4, text='功能描述：驱动管理').grid(row=3, column=0,
                                                                                                  columnspan=2,
                                                                                                  sticky=W)
        button3 = Button(self.TabStrip1__Tab4, text='安装Mdm所有驱动', command=self.install_driver).grid(row=4, column=1,columnspan=1)
        button4 = Button(self.TabStrip1__Tab4, text='卸载Mdm所有驱动', command=self.uninstall_driver).grid(row=4, column=2,columnspan=1)
        button5 = Button(self.TabStrip1__Tab4, text='启用Mdm所有驱动', command=self.start_driver).grid(row=5, column=1,columnspan=1)
        button6 = Button(self.TabStrip1__Tab4, text='停止Mdm所有驱动', command=self.stop_driver).grid(row=5, column=2,columnspan=1)
        button7 = Button(self.TabStrip1__Tab4, text='开启文件保护', command=self.start_file_protect).grid(row=6, column=1,
                                                                                                 columnspan=1)
        button8 = Button(self.TabStrip1__Tab4, text='关闭文件保护', command=self.stop_file_protect).grid(row=6, column=2,
                                                                                                columnspan=1)

        self.TabStrip1__Tab4Lb2 = Label(self.TabStrip1__Tab4, text='功能描述：一键卸载Mdm').grid(row=7, column=0,
                                                                                     columnspan=2,
                                                                                     sticky=W)

        button8 = Button(self.TabStrip1__Tab4, text='pc一键卸载', command=self.unistall_mdm).grid(row=8, column=1,
                                                                                                   columnspan=1)
        button8 = Button(self.TabStrip1__Tab4, text='嵌入式一键卸载', command=self.unistall_mdm2).grid(row=8, column=2,
                                                                                              columnspan=1)
        self.TabStrip1.add(self.TabStrip1__Tab4, text='驱动')


class Application(Application_ui):

    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Get_startage(self):
        self.TabStrip1__Tab1text.delete(0.0,END)
        path = self.TabStrip1__Tab1e1.get()
        if os.path.exists(path):
            try:
                f = open(path, 'r')
                ss = json.load(f)
            except Exception as e:
                self.TabStrip1__Tab1text.insert(INSERT, e)

            timeStruct = time.localtime(os.stat(path).st_mtime)
            u_time = time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)
            # print(u"文件修改时间："+u_time)
            self.TabStrip1__Tab1text.insert(INSERT,u"【文件修改时间】："+u_time+u'\n')
            self.TabStrip1__Tab1text.insert(INSERT,u'【唯一标识imei】：' + ss['imei']+'\n')
            self.TabStrip1__Tab1text.insert(INSERT,u'【策略版本version】：' + ss['version']+'\n')
            # print(u'唯一标识imei: ' + ss['imei'])
            # print(u'策略版本version: ' + ss['version'])
            for c in ss['content']:
                if c['type'] == 'extendStrategy':
                    self.TabStrip1__Tab1text.insert(INSERT, u'【外设策略】：\n')
                    # print(u'外设策略：')
                    for x in c['content']['items']:
                        # print(x['name'])
                        if x['name'] == "disableUsb":
                            if x['value'] == 2:
                                self.TabStrip1__Tab1text.insert(INSERT, u' USB管控状态:关\n')
                                #print(u' USB管控状态:关')
                            else:
                                self.TabStrip1__Tab1text.insert(INSERT, u' USB管控状态:开\n')
                                #print(u' USB管控状态:开')
                        elif x['name'] == "disableBluetooth":
                            if x['value'] == 2:
                                self.TabStrip1__Tab1text.insert(INSERT, u' 蓝牙管控状态:关\n')
                                #(u' 蓝牙管控状态:关')
                            else:
                                self.TabStrip1__Tab1text.insert(INSERT, u' 蓝牙管控状态:开\n')
                                # print(u' 蓝牙管控状态:开')
                        elif x['name'] == "disableWifi":
                            if x['value'] == 2:
                                self.TabStrip1__Tab1text.insert(INSERT,u' WIFI管控状态:关\n')
                                #print(u' WIFI管控状态:关')
                            else:
                                self.TabStrip1__Tab1text.insert(INSERT, u' WIFI管控状态:开\n')
                                #print(u' WIFI管控状态:开')
                        elif x['name'] == "disableCamera":
                            if x['value'] == 2:
                                self.TabStrip1__Tab1text.insert(INSERT, u' 摄像头管控状态:关\n')
                                #print(u' 摄像头管控状态:关')
                            else:
                                self.TabStrip1__Tab1text.insert(INSERT, u' 摄像头管控状态:开\n')
                                #print(u' 摄像头管控状态:开')
                        elif x['name'] == "disableMic":
                            if x['value'] == 2:
                                self.TabStrip1__Tab1text.insert(INSERT, u' 录音管控状态:关\n')
                                #print(u' 录音管控状态:关')
                            else:
                                self.TabStrip1__Tab1text.insert(INSERT, u' 录音管控状态:开\n')
                                #print(u' 录音管控状态:开')
                        else:
                            if x['value'] == 2:
                                self.TabStrip1__Tab1text.insert(INSERT,x['name'] + u':关\n')
                                #print(x['name'] + u':关')
                            else:
                                self.TabStrip1__Tab1text.insert(INSERT, x['name'] + u':开\n')
                                #print(x['name'] + u':开')
                elif c['type'] == 'appStrategy':
                    self.TabStrip1__Tab1text.insert(INSERT, u'【应用管控策略】：\n')
                    #print(u'应用管控策略：')
                    for x in c['content']['items']:
                        # print (x['content'])
                        if not x['content'] :
                            self.TabStrip1__Tab1text.insert(INSERT, u' 无管控应用\n')
                            #print(u'无管控应用')
                        else:
                            for i in x['content']['appList']:
                                self.TabStrip1__Tab1text.insert(INSERT, ' ' + i['name'] + '--' + i['packageName']+'\n')
                                #print(i['name'] + '--' + i['packageName'])
                elif c['type'] == 'netStrategy':
                    self.TabStrip1__Tab1text.insert(INSERT, u'【网络管控策略】：\n')
                    # print(u'网络管控策略：')
                    for x in c['content']['items']:
                        if not x['content']:
                            self.TabStrip1__Tab1text.insert(INSERT, (u' 无网络管控\n'))
                            #print(u'无网络管控')
                        else:
                            for i in x['content']['appList']:
                                self.TabStrip1__Tab1text.insert(INSERT, ' ' + i['packageName'] + '--' + i['name'] + '\n')
                                # print(i['packageName'] + '--' + i['name'])
            showinfo(title='提示', message="查询成功")
        else:
            self.TabStrip1__Tab1text.insert(INSERT,'不存在策略文件')

    def Change_to_qrs(self):
        self.TabStrip1__Tab1e1.set("Z:\\Program Files (x86)\\MDMTemp\\Startegy.json")
        showinfo(title='提示', message="切换到嵌入式成功")
        self.Get_startage()

    def Change_to_fqrs(self):
        self.TabStrip1__Tab1e1.set("C:\\Program Files (x86)\\mdmgr\\Startegy.json")
        showinfo(title='提示', message="切换到非嵌入式成功")
        self.Get_startage()

    def open_detective_qd(self):
        print(os.path.curdir)
        child = subprocess.Popen(os.getcwd()+'\\release\\start.bat', shell=False)
        if child:
            a = tkMessageBox.askokcancel('提示', '开启驱动检测成功，是否立即重启电脑？')
            if a:
                showinfo(title='提示', message="立即重启电脑！")
                os.popen('shutdown -r -t 00')

            else:
                pass

    def stop_detective_qd(self):

        child = subprocess.Popen(os.getcwd()+'\\release\\stop.bat', shell=False)
        if child:
            # showinfo(title='提示', message="关闭驱动检测成功")
            a = tkMessageBox.askokcancel('提示', '关闭驱动检测成功，是否立即重启电脑？')
            if a:
                showinfo(title='提示', message="立即重启电脑！")
                os.popen('shutdown -r -t 00')

            else:
                pass

    def install_driver(self):
        if dirver().installDriver() == 0:
            showinfo(title='提示', message="安装驱动成功！")
        else:
            showinfo(title='提示', message="安装驱动失败！")


    def uninstall_driver(self):
        if dirver().uninstallDriver() == 0:
            showinfo(title='提示', message="卸载驱动成功！")
        else:
            showinfo(title='提示', message="卸载驱动失败！")


    def start_driver(self):
        if dirver().startDrivers() == 0:
            showinfo(title='提示', message="启动驱动成功！")
        else:
            showinfo(title='提示', message="启动驱动失败！")

    def stop_driver(self):
        if dirver().stopDrivers() == 0:
            showinfo(title='提示', message="停止驱动成功！")
        else:
            showinfo(title='提示', message="停止驱动失败！")


    def start_file_protect(self):
        if dirver().enable_file_protect() == 0:
            showinfo(title='提示', message="开启文件保护成功！")
        else:
            showinfo(title='提示', message="开启文件保护失败！")

    def stop_file_protect(self):
        if dirver().disable_file_protect() == 0 :
            showinfo(title='提示', message="关闭文件保护成功！")
        else:
            showinfo(title='提示', message="关闭文件保护失败！")

    def unistall_mdm(self):

        a = tkMessageBox.askokcancel('提示', '确认卸载Mdm？')
        if a:
            if dirver().stopDrivers() == 0:
                if dirver().uninstallDriver() == 0:
                    path1 = "C:\\Program Files (x86)\\mdmgr\\setup.ini"
                    if os.path.exists(path1):
                        os.remove(path1)
                    else:
                        pass
                    shutil.copyfile(os.getcwd()+'\\release\\setup.ini', path1)
                    # showinfo(title='提示', message="修改文件成功！")
                    path = os.getcwd()

                    s = threading.Thread(target=self.run2)
                    s.start()


                else:
                    showinfo(title='提示', message="卸载驱动失败！")
            else:
                showinfo(title='提示', message="停止驱动失败！")

        else:
            pass

    def run2(self):
        os.system('"C:\\Program Files (x86)\\mdmgr\\MDMUninstall.exe"')


    def unistall_mdm2(self):

        a = tkMessageBox.askokcancel('提示', '确认卸载Mdm？')
        if a:
            if dirver().stopDrivers() == 0:
                if dirver().uninstallDriver() == 0:
                    path1 = "Z:\\Program Files (x86)\\MDMTemp\\setup.ini"
                    if os.path.exists(path1):
                        os.remove(path1)
                    else:
                        pass
                    shutil.copyfile(os.getcwd()+'\\release\\setup.ini', path1)
                    # showinfo(title='提示', message="修改文件成功！")
                    path = os.getcwd()

                    s = threading.Thread(target=self.run2)
                    s.start()


                else:
                    showinfo(title='提示', message="卸载驱动失败！")
            else:
                showinfo(title='提示', message="停止驱动失败！")

        else:
            pass

    def modify_file(self):
        self.TabStrip1__Tab3text.delete(0.0,END)
        path1 = 'C:\\ClientVer.xml'
        path2 = 'C:\\Program Files (x86)\\mdmgr\\ClientVer.xml'
        path3 = self.TabStrip1__Tab3ID1.get()
        all_list = os.listdir(u"C:\\")
        all_list2 = os.listdir(u"C:\\Program Files (x86)\\mdmgr\\")
        if 'ClientVer.xml' in all_list:
            try:
                os.remove(path1)
                shutil.copyfile(path3, path1)
                self.TabStrip1__Tab3text.insert(INSERT, "从"+path3+"到"+path1+"复制成功！\n")
            except Exception as e:
                self.TabStrip1__Tab3text.insert(INSERT,e)
                raise e
        else:
            try:
                shutil.copyfile(path3, path1)
                self.TabStrip1__Tab3text.insert(INSERT, "从"+path3+"到"+path1+"复制成功！\n")
            except Exception as e:
                self.TabStrip1__Tab3text.insert(INSERT, e)

        if 'ClientVer.xml' in all_list2:
            try:
                os.remove(path2)
                shutil.copyfile(path3, path2)
                self.TabStrip1__Tab3text.insert(INSERT, "从" + path3 + "到" + path2 + "复制成功！\n")
            except Exception as e:
                self.TabStrip1__Tab3text.insert(INSERT, e)
        else:
            try:
                shutil.copyfile(path3, path2)
                self.TabStrip1__Tab3text.insert(INSERT, "从" + path3 + "到" + path2 + "复制成功！\n")
            except Exception as e:
                self.TabStrip1__Tab3text.insert(INSERT, e)

    def update_detect(self):
        s = threading.Thread(target=self.run)
        s.start()

    def back_net(self):
        x = os.popen('netsh interface set interface "' + self.TabStrip1__Tab2ID1.get() + '" enable', 'r')
        result = x.read()
        print (result)
        if result:
            self.TabStrip1__Tab2text.insert(INSERT, u'网络恢复成功')

    def run(self):
        self.TabStrip1__Tab2text.delete(0.0, END)
        path1 = 'C:\\update_s.xml'
        try:

            while True:
                if os.path.exists(path1):
                    x = os.popen('netsh interface set interface "'+self.TabStrip1__Tab2ID1.get()+'" disable','r')
                    result = x.read()
                    x.close()
                    print(result)
                    if result:
                        self.TabStrip1__Tab2text.delete(0.0, END)
                        self.TabStrip1__Tab2text.insert(INSERT, result.decode('GBK')+u' --ok\n')
                    break
                else:
                    self.TabStrip1__Tab2text.insert(INSERT,"no update detect\n")
                    print('no update detect')

        except Exception as e:
            self.TabStrip1__Tab2text.insert(INSERT, e)
            print(e)




if __name__ == "__main__":

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        try:
            top = Tk()
            Application(top).mainloop()

        except Exception as e:
            print(e)
            os.system('pause')
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
