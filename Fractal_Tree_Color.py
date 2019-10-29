from turtle import *

t = Turtle()
t.setheading(90)
t.penup()
t.setpos(0, -250)
t.pendown()


def fractal_tree_color(length, level):
    t.pensize(length / 10)
    if length < 20:
        t.pencolor("green")
    else:
        t.pencolor("brown")

    t.speed(0)
    if level > 0:
        t.fd(length)
        t.rt(30)
        fractal_tree_color(length * 0.7, level - 1)
        t.lt(90)
        fractal_tree_color(length * 0.5, level - 1)
        t.rt(60)
        t.penup()
        t.bk(length)
        t.pendown()


fractal_tree_color(200, 8)
