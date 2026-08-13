import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("lightblue")   # background colour

pen = turtle.Turtle()
pen.speed(3)
pen.pensize(4)
pen.color("purple")

# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()

