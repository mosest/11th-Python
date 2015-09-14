#Tara Moses
#Assignment 3: Turtle Draws a Shape for You
#January 14, 2013

#1. Program asks the user to specify a number of sides.
#2. Program draws the user-specified shape centered on the canvas using Turtle.
#3. Program does not stop until the user tells it to.
#4. Program tells the user how many shapes were drawn.
#5. Program will work on any size canvas. :)

import turtle,math

def degrees_to_radians(degrees):
    pi = math.pi
    radians = float(pi*(degrees/180.0))
    return radians

print("Hello! I am going to draw a polygon for you today.\n")

draw = turtle.Turtle()
shape_count=0

window_height=float(draw.window_height()-20)
window_width=float(draw.window_width()-20)

if window_height<window_width:
    small_dimension=window_height
else:
    small_dimension=window_width

perimeter=float(math.pi*(small_dimension-50.0))

while True:

    num_sides=raw_input("How many sides would you like? (input an integer, please!): ")
    num_sides=int(num_sides)
    color=raw_input("What color do you want the shape to be? ")

    length=float(perimeter/num_sides)
    interior_angle=float(((180*(num_sides-2.0))/num_sides))

    if num_sides==3:
        length=float((small_dimension-20)*math.cos(degrees_to_radians(interior_angle/2.0)))

    apothem=float((length/2.0)*(float(math.tan(degrees_to_radians(interior_angle/2.0)))))         
    central_angle=float(360/(num_sides*2))

    draw.color(color)
    draw.fill(True)
    
    draw.dot()
    draw.up()
    draw.right(interior_angle-90.0)
    draw.forward(apothem)
    draw.left(90.0)
    draw.down()
    draw.forward(length/2.0)

    for i in range(num_sides-1):
        draw.left(180.0-interior_angle)
        draw.forward(length)
        
    draw.left(180.0-interior_angle)
    draw.forward(length/2.0)
    draw.up()
    draw.home()
    draw.down()

    draw.fill(False)
    
    shape_count=shape_count+1

    print("The smallest dimension is "+str(small_dimension)+".")
    print("The dimensions of this window are "+str(window_height)+" by "+str(window_width)+".")

    restart=raw_input("\nThere you go! Do you want me to draw another shape for you? (y/n): ")

    if restart=="y":
        draw.clear()
        print("\nOkay!\n")
    else:
        if shape_count==1:
            print("You drew 1 shape. Well, see you later!")
        else:
            print("You drew "+str(shape_count)+" shapes. Well, see you later!")
        break

    
