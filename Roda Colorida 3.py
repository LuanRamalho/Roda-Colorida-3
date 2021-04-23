# -*- coding: utf-8 -*-
import turtle as t
t.Screen()
t.speed(0)
t.pensize()

def shape(size, sides):
    for i in range(sides):
        t.forward(sides)
        t.left(360/sides)

t.right(180)
t.penup()
t.forward(240)
t.left(90)
t.forward(20)
t.pendown()
t.left(90)

for j in range(18):
    for i in range(4):
        for colours in ['violet' , 'indigo' , 'blue' , 'green' , 'yellow' ,'orange' , 'red']:
            t.color(colours)
            shape(30,3)
            t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(80)
    
for i in range(4):
    for colours in ['violet' , 'indigo' , 'blue' , 'green' , 'yellow' , 'orange' , 'red']:
        t.color(colours)
        shape(30,3)
        t.forward(10)
    t.right(90)
    t.penup()
    t.forward(20)
    t.right(100)
    t.pendown()
    
for i in range(4):
    for colours in ['violet' , 'indigo' , 'blue' , 'green' , 'yellow' , 'orange' , 'red']:
        t.color(colours)
        shape(30,3)
        t.forward(10)

t.exitonclick()
    

















































