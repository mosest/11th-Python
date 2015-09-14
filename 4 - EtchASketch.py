#Tara Moses
#Assignment 4: Etch-a-Sketch
#January 21, 2013

#1. Program lets user control the turtle's movements, whether it draws or not,
#   the color, and the width of the line that the turtle draws.
#2. Program will clear the canvas when the user presses 'e'.

import turtle
from Tkinter import *

screen = turtle.Screen()

print("Use the 'wasd' keys to draw something on the Turtle canvas.\n")
print("Press the 'up' arrow key to stop the turtle from drawing.")
print("Press the 'down' arrow key to make the turtle draw again.")
print("Press the 'left' arrow key to change colors.")
print("Press the 'right' arrow key to change the line width.\n")
print("Press 'e' to clear your drawing.")

def west():
    turtle.setheading(180.0)
    turtle.forward(20.0)

def east():
    turtle.setheading(0.0)
    turtle.forward(20.0)

def north():
    turtle.setheading(90.0)
    turtle.forward(20.0)

def south():
    turtle.setheading(270.0)
    turtle.forward(20.0)

def pick_up_tail():
    turtle.up()

def put_down_tail():
    turtle.down()

def change_color():
    color = raw_input("What color do you want the turtle to draw in? ")
    turtle.color(color)

def change_width():
    width = float(raw_input("How wide would you like the turtle's line to be? "))
    turtle.pensize(width)

def clear():
    turtle.clear()

screen.onkey(west, "a")
screen.onkey(east, "d")
screen.onkey(north, "w")
screen.onkey(south, "s")
screen.onkey(pick_up_tail, "Up")
screen.onkey(put_down_tail, "Down")
screen.onkey(clear, "e")
screen.onkey(change_color, "Left")
screen.onkey(change_width, "Right")

screen.listen()
turtle.mainloop()
