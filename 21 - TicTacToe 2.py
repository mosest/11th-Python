#Tara Moses
#Assignment 21: TicTacToe 2
#May 1, 2013

import random

class Board:
        def __init__(self):
             self.nums=[[0,1,2],[3,4,5],[6,7,8]]

        def canPlace(self,pos):
             numbers=[0,1,2,3,4,5,6,7,8]
             row=pos/3
             col=pos%3
             spot=self.nums[row][col]
             if spot in numbers:
                return True
             else:
                return False

        def place(self,pos,token):
             row=pos/3
             col=pos%3
             self.nums[row][col]=token
             return

        def isFull(self):
            count=0
            for row in range(3):
                for col in range(3):
                    if isinstance(self.nums[row][col],int):
                        count+=1
            if count==0:
                return True
            else:
                return False

        def findWinner(self):
            count=0
            for i in range(3):
                if self.nums[i][0]==self.nums[i][1]==self.nums[i][2]=="X":
                    count=1
                elif self.nums[0][i]==self.nums[1][i]==self.nums[2][i]=="X":
                    count=1
            if self.nums[0][0]==self.nums[1][1]==self.nums[2][2]=="X":
                count=1
            elif self.nums[0][2]==self.nums[1][1]==self.nums[2][0]=="X":
                count=1
            for i in range(3):
                if self.nums[i][0]==self.nums[i][1]==self.nums[i][2]=="@":
                    count=2
                elif self.nums[0][i]==self.nums[1][i]==self.nums[2][i]=="@":
                    count=2
            if self.nums[0][0]==self.nums[1][1]==self.nums[2][2]=="@":
                count=2
            if self.nums[0][2]==self.nums[1][1]==self.nums[2][0]=="@":
                count=2

            #now return things yay
            if count==0:
                return "Cat wins!"
            elif count==1:
                return "X wins!"
            elif count==2:
                return "@ wins!"
            else:
                return "I FUCKED UP BIG TIME"

        def __str__(self):
            output=""
            output+="   |   |   \n"
            output+=" "+str(self.nums[0][0])+" | "+str(self.nums[0][1])+" | "+str(self.nums[0][2])+" \n"
            output+="   |   |   \n"
            output+="---+---+---\n"
            output+="   |   |   \n"
            output+=" "+str(self.nums[1][0])+" | "+str(self.nums[1][1])+" | "+str(self.nums[1][2])+" \n"
            output+="   |   |   \n"
            output+="---+---+---\n"
            output+="   |   |   \n"
            output+=" "+str(self.nums[2][0])+" | "+str(self.nums[2][1])+" | "+str(self.nums[2][2])+" \n"
            output+="   |   |   \n"
            return output

#program starts
board=Board()
random_nums=[]
count=0
print board

for i in range(50):
    x=random.randint(0,8)
    random_nums.append(x)

for i in random_nums:
    count+=1
    if count%2==1:
        if board.canPlace(i):
            print "now placing X at",i
            board.place(i,"X")
            print board
        else:
            count-=1
            print "can't place X at",i
    elif count%2==0:
        if board.canPlace(i):
            print "now placing @ at",i
            board.place(i,"@")
            print board
        else:                          
            count-=1
            print "can't place @ at",i
    if board.findWinner()!="Cat wins!":
        break
    if board.isFull():
        break
        
print "Game over! "+str(board.findWinner())
