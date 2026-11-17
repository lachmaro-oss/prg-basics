import figures
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

figures.draw_square(pen, 100, -250, 50)
figures.draw_triangle(pen, 200, -50, 50)
figures.draw_rectangle(pen, 100, 150, 200, 50)

pen.hideturtle()
window.mainloop()