# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-09-27 20:26:13
# @Last Modified by:   Marte
# @Last Modified time: 2017-09-2107 20:49:31
import socket
HOST = '127.0.0.1'
PORT = 5555

s = socket.socket()
s.connect((HOST,PORT))
while True:
    data = s.recv(1024)
    print data
    if data.strip() == '答对了...':
        break
    if data.strip():
        flag = True
        while flag:
            kel = raw_input(u'你要猜测的数据 :>>')
            if kel.strip():
                flag = False
        s.sendall(kel)
        if kel == 'exit':
            break
s.close()