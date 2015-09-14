#Tara Moses
#Assignment 3.2 - Turtle Draws Three Shapes!
#January 15, 2013

#1. Program will draw a shape where the user clicks.
#2. Shape drawn depends on what mouse button the user presses.

import turtle,random
from Tkinter import *

screen = turtle.Screen()
screen.colormode(255)

blue=(0,128,255)
pink=(240,132,153)
green=(91,179,28)

print("Click on the Turtle screen to draw a shape.\n")
print("Left-click for a blue circle.")
print("Right-click for a green triangle.")
print("Middle-click or press the 's' button for a pink square.")

while True:    
    def draw_square(x, y):
        num=random.randint(10,100)
        
        turtle.up()
        turtle.color(pink)
        turtle.goto(x, y)
        turtle.forward(num/2.0)
        turtle.down()
        turtle.begin_fill()
        turtle.right(90)
        turtle.forward(num/2.0)
        turtle.right(90)
        turtle.forward(num)
        turtle.right(90)
        turtle.forward(num)
        turtle.right(90)
        turtle.forward(num)
        turtle.right(90)
        turtle.forward(num/2.0)
        turtle.end_fill()

    def press_for_square():
        num=random.randint(10,100)
        
        turtle.up()
        turtle.color(pink)
        turtle.forward(num/2.0)
        turtle.down()
        turtle.begin_fill()
        turtle.right(90)
        turtle.forward(num/2.0)
        turtle.right(90)
        turtle.forward(num)
        turtle.right(90)
        turtle.forward(num)
        turtle.right(90)
        turtle.forward(num)
        turtle.right(90)
        turtle.forward(num/2.0)
        turtle.end_fill()

    def draw_circle(x, y):
        num=random.randint(10,100)
        
        turtle.up()
        turtle.color(blue)
        turtle.goto(x, y)
        turtle.down()
        turtle.begin_fill()
        turtle.circle(num/2)
        turtle.end_fill()

    def draw_triangle(x, y):
        num=random.randint(2,100)

        turtle.up()
        turtle.color(green)
        turtle.goto(x, y)
        turtle.right(60)
        turtle.forward(num/2.0)
        turtle.right(120)
        turtle.down()
        turtle.begin_fill()
        turtle.forward(num/2.0)
        turtle.right(120)
        turtle.forward(num)
        turtle.right(120)
        turtle.forward(num)
        turtle.right(120)
        turtle.forward(num/2.0)
        turtle.end_fill()
        
    screen.onscreenclick(draw_circle)
    screen.onscreenclick(draw_square, 2)
    screen.onkey(press_for_square, "s")
    screen.onscreenclick(draw_triangle, 3)

    turtle.listen()
    turtle.mainloop()
