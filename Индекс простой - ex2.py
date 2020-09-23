import turtle as t
import random as r
import math as m

tur.shape('turtle')
tur.shapesize(1)
tur.speed(1)
tur.color('red')

Zero = (0, 90, 20, -90, 20, -90, 40, -90, 20, -90, 20, 180, 20, 90, 20)
One = (0, -45, m.sqrt(2)*20, 135, 40, 180, 40, 90)
Two = (20, 90, 20, 45, m.sqrt(2)*20, -135, 20, 180, 20, 135, 20*m.sqrt(2), -45, 20, 90)
Three = (20, 135, m.sqrt(2)*20, -135, 20, 135, m.sqrt(2)*20, 180, m.sqrt(2)*20, -135, 20, 135, m.sqrt(2)*20, 45)
Four = (0, -90, 20, 180, 20, -90, 20, 90, 20, 180, 40, 90)
Five = (20, 180, 20, -90, 20, -90, 20, 90, 20, 90, 20, 180, 20, -90, 20, -90, 20, 90, 20, 90, 20)
Six = (0, 135, 20*m.sqrt(2), -45, 20, -90, 20, -90, 20, -90, 20, 135, m.sqrt(2)*20, 45)
Seven = (0, 90, 20, 180, 20, 45, 20*m.sqrt(2), -135, 20, 180, 20)
Eight = (20, 90, 40, 90, 20, 90, 20, 90, 20, 180, 20, 90, 20, 90, 20)
Nine = (20, 90, 20, 45, 20*m.sqrt(2), 180, 20*m.sqrt(2), -135, 20, 90, 20, 90, 20)

A=[One, Four, One, Seven, Zero, Zero]

def wan(n):
    if len(n)%2==0:
        for i in range (0, len(n)-1, 2):
            t.forward(n[i])
            t.right(n[i+1])
    else:
        for i in range (0, len(n)-1, 2):
            t.forward(n[i])
            t.right(n[i+1])
        t.forward(n[len(n)-1])

for k in range (6):
    t.pendown()
    wan(A[k])
    t.penup()
    t.goto(20*(2*k+2), 0)
