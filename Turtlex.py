import turtle

def david():

    turtle.shape('turtle')
    turtle.shapesize(2)
    turtle.speed(5)
    
    
    for step in range (6):
        turtle.begin_fill()
        for i in range (3):
            turtle.forward(50)
            turtle.left(360/3)
        turtle.end_fill()
        turtle.forward(50)
        turtle.right(60)
    turtle.hideturtle()


david()
turtle.backward(200)
david()