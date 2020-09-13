import turtle
import math

turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(10000000)

dphi=360/(2*10**2 )
k=0.001
phi=0

for i in range (2*10**3):

    turtle.forward(k*dphi*math.sqrt(1+phi**2))
    turtle.left(dphi)
    phi+=dphi