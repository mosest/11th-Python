#Tara Moses
#Assignment 18: Recursion Math
#April 24, 2013

def multiply(a,b):
    if b==0:
        return 0
    if b<0:
        return multiply(-a,-b)
    elif b>0:
        return a+multiply(a,b-1)

def power(a,b):
    if b==0:
        return 1
    if b<0:
        return power(1.0/a,-b)
    elif b>0:
        return a*power(a,b-1) 

def factorial(n):
    if n==0:
        return 1
    if n>0:
        return n*factorial(n-1)
    elif n<0:
        return "Impossible to calculate factorial of negative integers"

def draw_triangle(n):
    if n>0:
        print "*"*n
        return draw_triangle(n-1)

#program starts here
while True:
    print "I'll multiply things for you!"
    a=raw_input("Enter the first factor: ")
    b=raw_input("Enter the second factor: ")
    print a,"*",b,"=",multiply(int(a),int(b))
    again=raw_input("Would you like to multiply anything else? (y/n): ")
    if again!="y" and again!="Y":
        break

while True:
    print "\nI'll raise things to powers for you!"
    a=raw_input("Enter the base number: ")
    b=raw_input("Enter what power you'd like it raised to: ")
    print str(a)+"^"+str(b)+"="+str(power(int(a),int(b)))
    again=raw_input("Would you like to raise anything else to a power? (y/n): ")
    if again!="y" and again!="Y":
        break

while True:
    print "\nI'll find the factorial of a number for you!"
    a=raw_input("Enter what number you'd like to find the factorial of: ")
    print factorial(int(a))
    again=raw_input("Would you like to find the factorial of something else? (y/n): ")
    if again!="y" and again!="Y":
        break
    
while True:
    print "\nI'll draw a triangle for you!"
    a=raw_input("Enter how long you want the triangle base to be: ")
    draw_triangle(int(a))
    again=raw_input("Would you like to draw another triangle? (y/n): ")
    if again!="y" and again!="Y":
        break
