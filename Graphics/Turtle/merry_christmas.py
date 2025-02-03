#!/usr/bin/env python3
import turtle
import random

# setup the window with a background colour
wn = turtle.Screen()
wn.bgcolor("#EFECCA")
wn.setup(width=800, height=600) 
wn.title("Merry Christmas")

# assign a name to your turtle
turtle = turtle.Turtle()
turtle.pensize(10)

colors = ["#7D8A2E", "#263248", "#FF8C00", "#F0C600"]

#
def snowflake(size, pensize, x, y):
    """ function that draws a snowflake """
    # turtle.pen(pensize=10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.forward(10*size)
    turtle.left(45)
    turtle.pendown()
    turtle.color("blue")

    for i in range(8):
        branch(size)
        turtle.left(45)



def branch(size):
    for i in range(3):
        for i in range(3):
            turtle.forward(10.0*size/3)
            turtle.backward(10.0*size/3)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(10.0*size/3)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(10.0*size)
    
def write_message():
    turtle.hideturtle()
    turtle.penup()
    turtle.color("red")
    turtle.goto(0, -200)
    turtle.write("Merry Christmas from Dilibe", align="center", font=("cursive", 24, "bold"))

snowflake(8, 6, 0, 0)
write_message()

wn.exitonclick()

