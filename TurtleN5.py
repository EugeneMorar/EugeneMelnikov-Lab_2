import turtle


turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(10)
n=10

for i in range (1,n+1):
    for k in range (4):
        turtle.left(90)
        turtle.forward(2*20*i)
    turtle.penup()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
turtle.hideturtle()





