import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Valentine's Day Special")

# Turtle setup
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(3)
pen.color("red", "pink")

# Heart drawing function
def draw_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

# Write message
def write_message():
    pen.up()
    pen.setpos(-10, -180)
    pen.color("white")
    pen.down()
    pen.hideturtle()
    pen.write("Happy Valentine's Day ❤️", align="center", font=("Comic Sans MS", 18, "bold"))

# Draw the heart and message
draw_heart()
write_message()

# Keep the screen open
turtle.done()
