#Tara Moses
#Assignment 8: Snowflake Fractal
#February 4, 2013

#1. Program draws a snowflake fractal depending on the user-specified fractal order.
#2. Program fills the snowflake with a certain user-specified color.

import turtle,Tkinter

order=int(raw_input("What order fractal would you like? "))
snowflake_color=raw_input("What color would you like it to be? ")

screen_width=turtle.window_width()-50.0
screen_height=turtle.window_height()-50.0


top_corner_x=-1*(screen_width/2.0)
top_corner_y=screen_height/2.0

directions="srsrs"
length=300.0

turtle.speed(0)
if order>4:
    turtle.tracer(3)
turtle.dot()
turtle.up()
turtle.goto(-150, 90)
turtle.down()
turtle.fillcolor(snowflake_color)
turtle.fill(True)

for i in range(order):
    if order==0:
        break
    directions=directions.replace("s"," slsrsls ")
    length=length/3.0

for letter in directions:
    if letter=="s":
        turtle.forward(length)
    elif letter=="r":
        turtle.right(120.0)
    elif letter=="l":
        turtle.left(60.0)

turtle.fill(False)

turtle.mainloop()
