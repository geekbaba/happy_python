#!/usr/bin/python
# -*- coding: UTF-8 -*-

#类4边形
import turtle
colors=['red','blue','green','orange']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%4])	#设置画笔的颜色
    t.width(x/100+1)			#笔尖的宽度
    t.forward(x)				#笔向前移动多少
    t.left(90)				#笔的角度调整 90度