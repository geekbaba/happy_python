#!/usr/bin/python

import turtle
colors=['red','purple','blue','green','yellow','orange']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])	#设置画笔的颜色
    t.width(x/100+1)			#笔尖的宽度
    t.forward(x)				#笔向前移动多少
    t.left(59)				#笔的角度调整 59度