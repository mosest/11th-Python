#Tara Moses
#Assignment 3.3 - Turtle Goes on a Trip!
#January 20, 2013

#1. Program lets Turtle wander around the canvas.
#2. Program will call Turtle back to the origin if it gets farther than 200 pixels away.
#3. Program changes Turtle's color each time it is called back to the origin.
#4. Program does not stop until user closes the Python shell.

import turtle,random

turtle.pensize(4)

while True:
    step=random.randint(5, 100)
    turn=random.randint(0, 360)

    new_color=random.randint(1,9)

    if new_color==1:
        new_color="red"
    elif new_color==2:
        new_color="orange"
    elif new_color==3:
        new_color="yellow"
    elif new_color==4:
        new_color="light green"
    elif new_color==5:
        new_color="green"
    elif new_color==6:
        new_color="violet"
    elif new_color==7:
        new_color="dark blue"
    elif new_color==8:
        new_color="purple"
    else:
        new_color="black"
    
    turtle.forward(step)
    turtle.right(turn)
    
    if turtle.distance(0,0)>=200.0:
        turtle.up()
        turtle.home()
        turtle.color(new_color)
        turtle.down()
