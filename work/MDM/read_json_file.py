# -*- coding: utf-8 -*-
# @File  : read_json_file.py
# @Author: zyt
# @Date  : 2018/9/11 16:25
# @Desc  : 读取当前MDM接收到的策略，并展示

import json

path1 = "C:\\Program Files (x86)\\mdmgr\\Startegy.json"
path2 = "Z:\\Program Files (x86)\\MDMTemp\\Startegy.json"
content =''
try:
    f = open(path1,'r')
    ss = json.load(f)
except Exception as e:
    print(e)

print(u'唯一标识imei: '+ss['imei'])
print(u'策略版本version: '+ss['version'])
for c in ss['content']:
    if c['type'] == 'extendStrategy':
        print ('外设策略：')
        for x in  c['content']['items']:
            # print(x['name'])
            if x['name'] == "disableUsb":
                if x['value'] == 2:
                    print(' USB管控状态:关')
                else:
                    print(' USB管控状态:开')
            elif x['name'] == "disableBluetooth":
                if x['value'] == 2:
                    print(' 蓝牙管控状态:关')
                else:
                    print(' 蓝牙管控状态:开')
            elif x['name'] == "disableWifi":
                if x['value'] == 2:
                    print(' WIFI管控状态:关')
                else:
                    print(' WIFI管控状态:开')
            elif x['name'] == "disableCamera":
                if x['value'] == 2:
                    print(' 摄像头管控状态:关')
                else:
                    print(' 摄像头管控状态:开')
            elif x['name'] == "disableMic":
                if x['value'] == 2:
                    print(' 录音管控状态:关')
                else:
                    print(' 录音管控状态:开')
            else:
                if x['value'] == 2:
                    print (x['name'] + u':关')
                else:
                    print (x['name'] + u':开')
    elif c['type'] == 'appStrategy':
        print ('应用管控策略：')
        for x in c['content']['items']:
            if x['content'] == '':
                print('无管控应用')
            else:
                for i  in x['content']['appList']:
                    print (i['name'] +'--'+i['packageName'])
    elif c['type'] == 'netStrategy':
        print ('网络管控策略：')
        for x in c['content']['items']:
            if x['content'] == '':
                print('无网络管控')
            else:
                for i  in x['content']['appList']:
                    print (i['packageName'] +'--'+i['name'])