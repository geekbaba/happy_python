#!/usr/bin/python
# -*- coding: UTF-8 -*-

import turtle
colors=['red','blue','green']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%3])	#设置画笔的颜色
    t.width(x/100+1)			#笔尖的宽度
    t.forward(x)				#笔向前移动多少
    t.left(120)				#笔的角度调整 120度
