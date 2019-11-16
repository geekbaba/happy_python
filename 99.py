#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
一个乘法表
'''
for x in range(1,10):
    s = ""
    for y in range(1,10):
        #if x <= y:
        if y <= x:
            s += str(y) + "x" + str(x) + " = " 
            s += str(x*y) + " "
            if (x*y)<10:
                s+= " "
    print(s)


