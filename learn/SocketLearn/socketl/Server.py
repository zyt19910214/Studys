# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-09-27 20:26:13
# @Last Modified by:   Marte
# @Last Modified time: 2017-09-27 20:49:31
import socket
import random

HOST='127.0.0.1'
PORT=5555

s = socket.socket()
s.bind((HOST,PORT))
s.listen(10)
num = random.randint(0,10)
conn, addres = s.accept()
conn.send('服务器连接成功...')
print u"已经与",addres,u"建立连接"
print u"服务生成随机数为：" ,(str)(num)
while True:
    data = conn.recv(1024)
    print '用户猜测数为:', data

    if data == 'exit':
        conn.send('bye...')
        print '结束回话'
        break
    elif data == (str)(num):
        conn.send('答对了...')
        break
    else:
        conn.send('答错了...')


conn.close()