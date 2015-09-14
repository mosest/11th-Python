#Tara Moses
#Assignment 24: Tic-Tac-Toe, Turtle Edition
#May 15, 2013

import turtle,Tkinter,random

screen=turtle.Screen()
screen.colormode(255)
isRunning=False
a=20
b=100
blue=(0,128,255)
pink=(240,132,153)
cursor_pos=(0,0)
grid_pos=0
x_positions=[]
o_positions=[]
one_count=0
two_count=0
cat_count=0

def restartGame():
    global x_positions,o_positions
    drawBoard()
    x_positions=[]
    o_positions=[]    

def boardIsFull():
    spot_count=0
    if 0 in x_positions or 0 in o_positions:
        spot_count+=1
    if 1 in x_positions or 1 in o_positions:
        spot_count+=1
    if 2 in x_positions or 2 in o_positions:
        spot_count+=1
    if 3 in x_positions or 3 in o_positions:
        spot_count+=1
    if 4 in x_positions or 4 in o_positions:
        spot_count+=1
    if 5 in x_positions or 5 in o_positions:
        spot_count+=1
    if 6 in x_positions or 6 in o_positions:
        spot_count+=1
    if 7 in x_positions or 7 in o_positions:
        spot_count+=1
    if 8 in x_positions or 8 in o_positions:
        spot_count+=1

    if spot_count==9:
        return True
    else:
        return False

def xWins():
    global x_positions
    if 0 in x_positions and 1 in x_positions and 2 in x_positions:
        return True
    elif 3 in x_positions and 4 in x_positions and 5 in x_positions:
        return True
    elif 6 in x_positions and 7 in x_positions and 8 in x_positions:
        return True
    elif 0 in x_positions and 3 in x_positions and 6 in x_positions:
        return True
    elif 1 in x_positions and 4 in x_positions and 7 in x_positions:
        return True
    elif 2 in x_positions and 5 in x_positions and 8 in x_positions:
        return True
    elif 0 in x_positions and 4 in x_positions and 8 in x_positions:
        return True
    elif 6 in x_positions and 4 in x_positions and 2 in x_positions:
        return True
    else:
        return False

def oWins():
    global o_positions
    if 0 in o_positions and 1 in o_positions and 2 in o_positions:
        return True
    elif 3 in o_positions and 4 in o_positions and 5 in o_positions:
        return True
    elif 6 in o_positions and 7 in o_positions and 8 in o_positions:
        return True
    elif 0 in o_positions and 3 in o_positions and 6 in o_positions:
        return True
    elif 1 in o_positions and 4 in o_positions and 7 in o_positions:
        return True
    elif 2 in o_positions and 5 in o_positions and 8 in o_positions:
        return True
    elif 0 in o_positions and 4 in o_positions and 8 in o_positions:
        return True
    elif 6 in o_positions and 4 in o_positions and 2 in o_positions:
        return True
    else:
        return False

def catWins():
    if boardIsFull() and xWins()==False and oWins()==False:
        return True
    else:
        return False

def drawBoard():
    global b
    #actually draw the board :D
    turtle.ht()
    turtle.width(5)
    turtle.up()
    turtle.goto(-3*b/2.0,b/2.0)
    turtle.down()
    turtle.seth(0)
    turtle.forward(3*b)
    turtle.up()
    turtle.goto(-3*b/2.0,-b/2.0)
    turtle.down()
    turtle.seth(0)
    turtle.forward(3*b)
    turtle.up()
    turtle.goto(-b/2.0,3*b/2.0)
    turtle.down()
    turtle.seth(270)
    turtle.forward(3*b)
    turtle.up()
    turtle.goto(b/2.0,3*b/2.0)
    turtle.down()
    turtle.seth(270)
    turtle.forward(3*b)

def drawX(x,y):
    global isRunning,a,blue,cursor_pos,grid_pos,x_positions,one_count,two_count,cat_count,again
    if isRunning:
        return
    else:
        turtle.ht()
        isRunning=True
        turtle.up()
        turtle.speed(0)
        turtle.goto(x,y)
        turtle.right(45)
        turtle.width(5)
        turtle.fillcolor(blue)
        turtle.up()
        turtle.forward(3*a/2.0)
        turtle.down()

        #start drawing X
        turtle.fill(True)
        turtle.left(90)
        turtle.forward(a/2.0)
        turtle.left(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a/2.0)
        turtle.right(45)
        turtle.fill(False)
        #finish drawing X
        
        isRunning=False
        cursor_pos=(x,y)
        
        x,y=cursor_pos

        if x>=-b/2.0 and x<=b/2.0 and y>=-b/2.0 and y<=b/2.0:
            grid_pos=4
        elif x>b/2.0 and y>=-b/2.0 and y<=b/2.0:
            grid_pos=5
        elif x<-b/2.0 and y>=-b/2.0 and y<=b/2.0:
            grid_pos=3
        elif x>=-b/2.0 and x<=b/2.0 and y>b/2.0:
            grid_pos=1
        elif x>b/2.0 and y>b/2.0:
            grid_pos=2
        elif x<-b/2.0 and y>b/2.0:
            grid_pos=0
        elif x>=-b/2.0 and x<=b/2.0 and y<-b/2.0:
            grid_pos=7
        elif x>b/2.0 and y<-b/2.0:
            grid_pos=8
        elif x<-b/2.0 and y<-b/2.0:
            grid_pos=6

        x_positions.append(grid_pos)

        if xWins():
            print "X wins!"
            again=raw_input("Would you like to play again? (y/n): ")
            one_count+=1
            if again!="y" and again!="Y":
                print "X won",one_count,"times, O won",two_count,"times, and cat won",cat_count,"times. Click anywhere to exit."
                turtle.exitonclick()
            else:
                turtle.clear()
                restartGame()
        elif oWins():
            print "O wins!"
            again=raw_input("Would you like to play again? (y/n): ")
            two_count+=1
            if again!="y" and again!="Y":
                print "X won",one_count,"times, O won",two_count,"times, and cat won",cat_count,"times. Click anywhere to exit."
                turtle.exitonclick()
            else:
                turtle.clear()
                restartGame()
        elif catWins():
            print "Cat wins!"
            again=raw_input("Would you like to play again? (y/n): ")
            cat_count+=1
            if again!="y" and again!="Y":
                print "X won",one_count,"times, O won",two_count,"times, and cat won",cat_count,"times. Click anywhere to exit."
                turtle.exitonclick()
            else:
                turtle.clear()
                restartGame()
        else:
            pass

def drawO(x,y):
    global isRunning,a,pink,cursor_pos,grid_pos,o_positions,one_count,two_count,cat_count,again
    if isRunning:
        return
    else:
        isRunning=True
        turtle.up()
        turtle.speed(0)
        turtle.fillcolor(pink)
        turtle.width(5)
        turtle.goto(x,y)
        turtle.setheading(270)
        turtle.forward(a)
        turtle.setheading(0)
        turtle.down()

        #start drawing O
        turtle.fill(True)
        turtle.circle(a)
        turtle.fill(False)
        #finish drawing O)
        
        isRunning=False        
        cursor_pos=(x,y)
        
        x,y=cursor_pos

        if x>=-b/2.0 and x<=b/2.0 and y>=-b/2.0 and y<=b/2.0:
            grid_pos=4
        elif x>b/2.0 and y>=-b/2.0 and y<=b/2.0:
            grid_pos=5
        elif x<-b/2.0 and y>=-b/2.0 and y<=b/2.0:
            grid_pos=3
        elif x>=-b/2.0 and x<=b/2.0 and y>b/2.0:
            grid_pos=1
        elif x>b/2.0 and y>b/2.0:
            grid_pos=2
        elif x<-b/2.0 and y>b/2.0:
            grid_pos=0
        elif x>=-b/2.0 and x<=b/2.0 and y<-b/2.0:
            grid_pos=7
        elif x>b/2.0 and y<-b/2.0:
            grid_pos=8
        elif x<-b/2.0 and y<-b/2.0:
            grid_pos=6

        o_positions.append(grid_pos)

        if xWins():
            print "X wins!"
            again=raw_input("Would you like to play again? (y/n): ")
            one_count+=1
            if again!="y" and again!="Y":
                print "X won",one_count,"times, O won",two_count,"times, and cat won",cat_count,"times. Click anywhere to exit."
                turtle.exitonclick()
            else:
                turtle.clear()
                restartGame()
        elif oWins():
            print "O wins!"
            again=raw_input("Would you like to play again? (y/n): ")
            two_count+=1
            if again!="y" and again!="Y":
                print "X won",one_count,"times, O won",two_count,"times, and cat won",cat_count,"times. Click anywhere to exit."
                turtle.exitonclick()
            else:
                turtle.clear()
                restartGame()
        elif catWins():
            print "Cat wins!"
            again=raw_input("Would you like to play again? (y/n): ")
            cat_count+=1
            if again!="y" and again!="Y":
                print "X won",one_count,"times, O won",two_count,"times, and cat won",cat_count,"times. Click anywhere to exit."
                turtle.exitonclick()
            else:
                turtle.clear()
                restartGame()
        else:
            pass

#program starts here

print "******Tic-Tac-Toe, Turtle Edition******"
print "Play by yourself or with a friend.\n"
print "Left click to place an X; right click to place an O."

restartGame()

while True:    
    screen.onscreenclick(drawX)
    screen.onscreenclick(drawO, 3)
    
    screen.listen()
    turtle.mainloop()

