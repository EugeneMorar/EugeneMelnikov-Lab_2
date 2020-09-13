import turtle


turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(10*100)
n=10*10

for i in range (n):

    turtle.forward(2*3.14*50/n)
    turtle.left(360/n)
turtle.hideturtle()