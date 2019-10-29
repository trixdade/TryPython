from turtle import *

t = Turtle()
t.setheading(90)
t.penup()
t.setpos(0, -250)
t.pendown()


def sierpinski(length, level):
    t.speed(0)
    if level == 0:
        return
    t.begin_fill()
    t.color('red')

    for i in range(3):
        sierpinski(length / 2, level - 1)
        t.fd(length)
        t.lt(120)
    t.end_fill()


sierpinski(200, 6)
