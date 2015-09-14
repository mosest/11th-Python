#Tara Moses
#Assignment 5: Cookie Jar
#January 22, 2013

#1. Program does these things

import random

def is_not_valid(number):
    if number<=0 or number>highest or number>amount:
        return True
    else:
        return False

def is_int(number):
    try:
        number = int(number)
        return True
    except ValueError:
        return False

print("Welcome to The Cookie Jar Game. Your goal is to take the last cookie.")
print("You may take anywhere from 1 to 4 cookies from the jar.\n")

highest = 4
computer_wins = 0
user_wins= 0

while True:
    first = raw_input("Would you like to go first? (y/n): ")
    
    amount = random.randint(highest+10, 40)
    
    print("\nThere are "+str(amount)+" cookies in the jar.")

    if first=="n":
        computer_take = random.randint(1,highest)
        amount = amount-computer_take
        print("The computer takes "+str(computer_take)+" cookies.")
        print("There are now "+str(amount)+" cookies in the jar.\n")

    while True:

        #it's the user's turn
        
        user_take = raw_input("How many cookies do you want? ")
        while is_int(user_take)!=True or is_not_valid(int(user_take)):
            user_take = raw_input("Please enter a whole number between 1 and "+str(highest)+": ")
        amount = amount-int(user_take)
        print("There are now "+str(amount)+" cookies in the jar.\n")
        if amount==0:
            print("AWW YISS WINNER WINNER CHICKEN DINNERRRRR\n")
            user_wins = user_wins+1
            break
        
        #now it's the computer's turn
        
        if amount>highest and amount%(highest+1)!=0:
            computer_take = amount%(highest+1)
        elif amount>highest and amount%(highest+1)==0:
            computer_take = random.randint(1,highest)
        else:
            computer_take = amount
        amount = amount-computer_take
        print("The computer takes "+str(computer_take)+" cookies.")
        print("There are now "+str(amount)+" cookies in the jar.\n")

        if amount<=0:
            print("COMPUTER WINS. COMPUTER WINS. COMPUTER WINS.\n")
            computer_wins = computer_wins+1
            break

    play_again = raw_input("Would you like to play again? (y/n): ")

    if play_again=="n":
        break

print("\nGood game! The computer won "+str(computer_wins)+" times, and you won "+str(user_wins)+" times.")
