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


t.shapesize(1)

number_of_turtles = 10
dt = 0.1

gas = [t.Turtle(shape = 'circle') for i in range (number_of_turtles)]

vx = [r.randint(-60, 60) for i in range (number_of_turtles)]
vy = [r.randint(-60, 60) for i in range (number_of_turtles)]

for i in range (number_of_turtles):
    gas[i].penup()
    gas[i].speed(100)
    gas[i].goto(r.randint(-199, 199), r.randint(-199, 199))


while (True):
    for i in range (number_of_turtles):
        if (gas[i].xcor() >= 200) or (gas[i].xcor() <= -200):
            vx[i] = -vx[i]
        if (gas[i].ycor() >= 200) or (gas[i].ycor() <= -200):
            vy[i] = -vy[i]
        
        gas[i].goto(gas[i].xcor() + vx[i]*dt, gas[i].ycor() + vy[i]*dt)
        
    for k in range (number_of_turtles):
            if (k!=i) and (abs(gas[i].xcor() - gas[k].xcor()) <= 1) and (abs(gas[i].ycor() - gas[k].ycor()) <= 1):
                vx[i], vx[k] = vx[k], vx[i]
                vy[i], vy[k] = vy[k], vy[i]
    

        
