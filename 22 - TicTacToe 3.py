#Tara Moses
#Assignment 22: TicTacToe 3
#May 3, 2013

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
                return "I SCREWED UP BIG TIME."

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

#program starts here
one_count=0
two_count=0
cat_count=0

print "******TIC-TAC-TOE******"
print "1. Computer vs. Computer"
print "2. Computer vs. Player"
print "3. Player 1 vs. Player 2\n"

while True:
    board=Board()
    num_players=raw_input("Choose an option, please (1/2/3): ")
    if num_players=="1":
        print "Computer vs. Computer"

        #program
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
                    print "X chooses position",i
                    board.place(i,"X")
                    print board
                else:
                    count-=1
            elif count%2==0:
                if board.canPlace(i):
                    print "@ chooses position",i
                    board.place(i,"@")
                    print board
                else:                          
                    count-=1
            if board.findWinner()!="Cat wins!":
                break
            if board.isFull():
                break        
        print "Game over! "+str(board.findWinner())
        if board.findWinner()=="X wins!":
            one_count+=1
        elif board.findWinner()=="@ wins!":
            two_count+=1
        else:
            cat_count+=1
        #end program
        
        again=raw_input("Would you like to play again? (y/n): ")
        if again!="y" and again!="Y":
            break
    elif num_players=="2":
        print "Computer vs. Player. Player plays as X's."
        
        #program
        random_nums=[]
        count=0
        print board

        for i in range(50):
            x=random.randint(0,8)
            random_nums.append(x)
            
        for i in random_nums:
            count+=1
            if count%2==1: #if it's player's turn
                player_pos=raw_input("Where would you like to place your token? (0/8): ")
                player_pos=int(player_pos)
                if board.canPlace(player_pos):
                    print "Player chooses position",player_pos
                    board.place(player_pos,"X")
                    print board
                else: #if player can't place token at player_pos
                    print "That spot is taken."
                    count-=1
            elif count%2==0: #if it's computer's turn
                if board.canPlace(i): #if computer can place token at i
                    print "Computer chooses position",i
                    board.place(i,"@")
                    print board
                else: #if computer can't place token at i               
                    count-=1 #make it the computer's turn again
            if board.findWinner()!="Cat wins!":
                break
            if board.isFull():
                break        
        print "Game over! "+str(board.findWinner())
        if board.findWinner()=="X wins!":
            one_count+=1
        elif board.findWinner()=="@ wins!":
            two_count+=1
        else:
            cat_count+=1
        #end program
        
        again=raw_input("Would you like to play again? (y/n): ")
        if again!="y" and again!="Y":
            break
    elif num_players=="3":
        print "Player 1 vs. Player 2. Player 1 is X's; Player 2 is @'s."
        
        #program
        count=0
        print board
            
        for i in range(50):
            count+=1
            if count%2==1: #if it's player 1's turn
                player1_pos=raw_input("Where would Player 1 like to place his/her token? (0/8): ")
                player1_pos=int(player1_pos)
                if board.canPlace(player1_pos):
                    print "Player 1 chooses position",player1_pos
                    board.place(player1_pos,"X")
                    print board
                else: #if player 1 can't place token at player1_pos
                    print "That spot is taken."
                    count-=1
            elif count%2==0: #if it's player 2's turn
                player2_pos=raw_input("Where would Player 2 like to place his/her token? (0/8): ")
                player2_pos=int(player2_pos)
                if board.canPlace(player2_pos): #if player 2 can place token player2_pos
                    print "Player 2 chooses position",player2_pos
                    board.place(player2_pos,"@")
                    print board
                else: #if player 2 can't place token at player2_pos
                    print "That spot is taken."
                    count-=1 #make it player 2's turn again
            if board.findWinner()!="Cat wins!":
                break
            if board.isFull():
                break        
        print "Game over! "+str(board.findWinner())
        if board.findWinner()=="X wins!":
            one_count+=1
        elif board.findWinner()=="@ wins!":
            two_count+=1
        else:
            cat_count+=1
        #end program

        again=raw_input("Would you like to play again? (y/n): ")
        if again!="y" and again!="Y":
            break
    else:
        pass
print "X won",one_count,"times, @ won",two_count,"times, and cat won",cat_count,"times."
