import turtle
import math

turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(10000000)

turtle.penup()
turtle.forward(200)
turtle.left(90)



def arc(theta, r):
    turtle.pendown()
    for i in range (theta//3):
        turtle.forward(2*(math.pi)*r/(360/3))
        turtle.left(3)
    turtle.penup()

turtle.fillcolor('yellow')
turtle.begin_fill()
arc(360,40*5)
turtle.end_fill()

turtle.fillcolor('blue')
turtle.goto(-70, 4.5*25)
turtle.begin_fill()
arc(360, 28)
turtle.goto(130, 4.5*25)
arc(360, 28)
turtle.end_fill()


turtle.goto(2, -20)
turtle.pendown()
turtle.color('black')
turtle.width(20)
turtle.forward(70)
turtle.penup()


turtle.goto(-70-28*2, -30)
turtle.left(180)
turtle.color('red')
arc(180, 28+100)