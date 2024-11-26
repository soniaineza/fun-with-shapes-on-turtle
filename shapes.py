import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.speed(2)

pen.color("red")
pen.begin_fill()
for _ in range(3):
    pen.forward(100)
    pen.left(120)
pen.end_fill()

pen.penup()
pen.goto(-150, -100)
pen.pendown()

pen.color("green")
pen.begin_fill()
for _ in range(2):
    pen.forward(150)
    pen.right(90)
    pen.forward(80)
    pen.right(90)
pen.end_fill()

pen.penup()
pen.goto(200, 100)
pen.pendown()

# Hexagon
pen.color("purple")
pen.begin_fill()
for _ in range(6):
    pen.forward(80)
    pen.left(60)
pen.end_fill()

pen.hideturtle()
screen.mainloop()
