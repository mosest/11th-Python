#Tara Moses
#Assignment 20: TicTacToe 1
#April 29, 2013

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

#start actual program now
board=Board()
random_nums=[]
print board

for i in range(50):
        x=random.randint(0,8)
        random_nums.append(x)

for i in random_nums:
        if board.canPlace(i):
                print "now placing token at",i
                board.place(i,"@")
                print board
        else:
                print "Cannot place token at",i
