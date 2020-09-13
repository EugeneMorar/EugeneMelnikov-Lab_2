import turtle


turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(10000000)
turtle.left(90)

def circle(r):
    for i in range (60):
        turtle.forward(2*3.14*r/(360/60))
        turtle.left(360/60)
    for i in range (60):
        turtle.forward(2*3.14*r/(360/60))
        turtle.right(360/60)    

for i in range (5,20):
    circle(i)