import turtle

def draw_square(pen, length, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    for i in range(4):
        pen.forward(length)
        pen.right(90)


def draw_triangle(pen, length, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    for i in range(3):
        pen.forward(length)
        pen.right(120)


def draw_rectangle(pen, length_a, length_b, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)