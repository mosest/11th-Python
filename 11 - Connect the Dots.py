#Tara Moses
#Assignment 11: Connect the Dots
#February 22, 2013

#1. Program draws a picture according to the points in the file.

import turtle,Tkinter

screen=turtle.Screen()
screen.bgcolor("red")
x_coordinates_array=[]
y_coordinates_array=[]

file_of_dots=file("ConnectDots.txt")

for line in file_of_dots:
    line=line.strip()
    coordinates=line.split(" ")
    x,y=coordinates
    x=int(x)
    y=int(y)
    x_coordinates_array.append(x)
    y_coordinates_array.append(y)
    
turtle.fill(True)
for i in range(len(x_coordinates_array)):
    if i==0:
        turtle.up()
        turtle.goto(x_coordinates_array[i],y_coordinates_array[i])
        turtle.down()
    turtle.goto(x_coordinates_array[i],y_coordinates_array[i])
turtle.fill(False)

turtle.up()
turtle.color("white")

turtle.fill(True)
for i in range(len(x_coordinates_array)):
    if i==0:
        turtle.up()
        turtle.goto(x_coordinates_array[i]/2.0,y_coordinates_array[i]/2.0)
        turtle.down()
    turtle.goto(x_coordinates_array[i]/2.0,y_coordinates_array[i]/2.0)
turtle.fill(False)

turtle.mainloop()
