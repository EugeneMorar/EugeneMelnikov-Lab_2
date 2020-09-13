import turtle
import math

turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(10000000)
turtle.penup()

turtle.left(180)
turtle.forward(200)
turtle.right(90)
turtle.pendown()


def arc(theta, r):
    for i in range (theta//3):
        turtle.forward(2*(math.pi)*r/3/10)
        turtle.right(3)
        
        
        
for i in range (5):
    arc(180, 10)
    arc(180,1)