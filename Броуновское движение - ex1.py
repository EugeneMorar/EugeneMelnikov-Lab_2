import turtle as t
import random as r
import math as m
import time 


t.penup()
t.goto(-200, -200)
t.pendown()
t.goto(-200, 200)
t.goto(200, 200)
t.goto(200, -200)
t.goto(-200, -200)
t.penup()
t.hideturtle()


t.shapesize(0.1)

n=10
T=100
dt=0.05

gas = [t.Turtle(shape = 'circle') for i in range (n)]

vx = [r.randint(-60, 60) for i in range (n)]
vy = [r.randint(-60, 60) for i in range (n)]

for i in range (n):
    gas[i].penup()
    gas[i].speed(100)
    gas[i].goto(r.randint(-199, 199), r.randint(-199, 199))

T=int(T/dt)


for ti in range (0, T, 1):
    for i in range (n):
        if (gas[i].xcor() >= 200) or (gas[i].xcor() <= -200):
            vx[i] = -vx[i]
        if (gas[i].ycor() >= 200) or (gas[i].ycor() <= -200):
            vy[i] = -vy[i]
        
        gas[i].goto(gas[i].xcor() + vx[i]*dt, gas[i].ycor() + vy[i]*dt)
    
