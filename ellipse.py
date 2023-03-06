from turtle import *

import turtle as tur
ws = tur.Screen()


def drawoval(rad):


    for i in range(2):
        tur.circle(rad,90)
        tur.circle(rad//2,90)





ws.bgcolor('black')

col=['cyan','blue','pink','purple',
     'yellow','green']

value=10
index=0

tur.speed(100)

for i in range(36):

    tur.seth(-value)

    tur.color(col[index])

    if index==5:
        index=0
    else:
        index+=1

    drawoval(30)

    value+=10

tur.hideturtle()
tur.exitonclick()