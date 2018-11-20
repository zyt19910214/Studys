# -*- coding: utf-8 -*-
# @File  : 111.py
# @Author: zyt
# @Date  : 2018/10/8 10:27
# @Desc  :

n = 10
m = 4
l = [x for x in range(1,n+1)]
print(l)
print(len(l))
for x in range(n):
    if x*m <= len(l):
        l.remove(l[x*m-1])
    else:
        print(x*m-1-len(l))
        l.remove(l[x*m-len(l)])

print(l)

