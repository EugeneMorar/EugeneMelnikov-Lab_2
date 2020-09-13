import turtle
import math

k=int(input())

turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(5)
turtle.penup()
turtle.forward(150)
turtle.left(180)

def star(n):
    turtle.pendown()
    for i in range (n):
        turtle.forward(200)
        turtle.left(180 - 180/n)
star(k)
    

