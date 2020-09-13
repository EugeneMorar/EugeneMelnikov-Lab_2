import turtle
import math



turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(100)
turtle.penup()



def duocircle(theta):
    turtle.pendown()
    turtle.left(theta)
    for i in range (60):
        turtle.forward(2*(math.pi)*5/(360/60))
        turtle.left(360/60)
    for i in range (60):
        turtle.forward(2*(math.pi)*5/(360/60))
        turtle.right(360/60)  
        
        
n=3
for i in range(n):
    duocircle(360/n)
    