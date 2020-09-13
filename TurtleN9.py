import turtle
import math



turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(10)


def polygon(r, n):
    turtle.pendown()
    for i in range (n):
        turtle.left(90 + 180/n)
        turtle.forward(2 * r * math.sin(math.pi/n))
        turtle.right((180 - 360/n) / 2)
    turtle.penup()
    
    
for i in range (1, 10):
    turtle.penup()
    turtle.goto(20*i + 10, 0)
    polygon(20*i + 10, i + 2)
 
    