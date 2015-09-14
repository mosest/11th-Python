#Tara Moses
#Assignment 23: Sierpinsky Triangle
#May 10, 2013

import turtle,Tkinter,math

def drawTriangle(t,side_length,order):
    t.ht()
    if order>0:
        t1=t.clone()
        t.forward(side_length/2)
        t2=t.clone()
        t.forward(side_length/2)
        t.left(120)
        t.forward(side_length)
        t.left(120)
        t.forward(side_length/2)
        t3=t.clone()
        t3.left(120)
        t.forward(side_length/2)
        
        drawTriangle(t1,side_length/2,order-1)
        drawTriangle(t2,side_length/2,order-1)
        drawTriangle(t3,side_length/2,order-1)

#start program now
t=turtle.Turtle()


print "*****Sierpinski's Triangle*****"
order=raw_input("What order would you like the triangle to be? Enter an integer: ")
order=int(order)
side_length=raw_input("How large (in pixels) would you like the triangle to be? Enter an integer: ")
side_length=int(side_length)

a=(side_length/2.0)/(math.cos(30.0*math.pi/180.0))
t.speed(0)
t.up()
t.left(210)
t.forward(a)
t.right(210)
t.down()
drawTriangle(t,side_length,order)
