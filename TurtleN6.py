import turtle
import math



turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(1)

n=12

for i in range (n):
    turtle.forward(80)
    turtle.stamp()
    turtle.backward(80)
    turtle.left(360/n)
    