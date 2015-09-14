#Tara Moses
#Assignment 19: Trees
#April 26, 2013

import turtle

def draw_tree(l_t,order,length,l_angle,r_angle,l_percent,r_percent,width):
    if order==0:
        l_t.forward(length)
        return
    l_t.width(width)
    l_t.forward(length)
    r_t=l_t.clone()
    l_t.left(l_angle)
    r_t.right(r_angle)
    draw_tree(l_t,order-1,length*l_percent,l_angle,r_angle,l_percent,r_percent,width-1)
    draw_tree(r_t,order-1,length*r_percent,l_angle,r_angle,l_percent,r_percent,width-1)

print "I'll draw a tree to your liking!"
order=raw_input("What order would you like? ")
length=raw_input("How long do you want the trunk to be (in pixels)? ")
l_angle=raw_input("The left angle? ")
r_angle=raw_input("The right angle? ")
l_percent=raw_input("The left percent? Enter as a decimal: ")
r_percent=raw_input("The right percent? Enter as a decimal: ")
leaf_color=raw_input("What color would you like the leaves to be? ")

order=int(order)
length=int(length)
l_angle=int(l_angle)
r_angle=int(r_angle)
l_percent=float(l_percent)
r_percent=float(r_percent)

bob=turtle.Turtle()
bob.pencolor("black")
bob.fillcolor(leaf_color)
bob.left(90)
draw_tree(bob,order,length,l_angle,r_angle,l_percent,r_percent,order)
