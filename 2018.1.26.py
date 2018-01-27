#!/usr/bin/env python
# _* _ coding:utf-8 _*_

f=open('C:/Users/q1284/Desktop/change file.txt','w')
f.write('似的发射点发射点'*10000)
f=open('C:/Users/q1284/Desktop/change file.txt','r+')
print(f.read())
f.close()
