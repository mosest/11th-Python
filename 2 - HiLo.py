#Tara Moses
#Assignment 2: High-Low Game
#January 11, 2013

#1. This program is designed to generate a random integer in a user-designated range, and
#       let the user guess the number, giving hints such as "too high," "WAY too high," "too low,"
#       and "WAY too low" when appropriate.
#2. User can choose the difficulty of the game, including one level which allows the user to set the range.
#3. The program ends only when the user tells it to.
#4. The program reports how many games the user has won at the end of the game.
#5. The program does not crash when the range is set incorrectly.
#6. The program does not crash when a non-integer character is entered. Anywhere. ANYWHERE.

import random

def is_difficulty(s): #this method tests whether a number is a suitable choice for level of difficulty.
    try:
        a=int(s)
        if int(s)<6:
            return True
    except ValueError:
        return False

def is_number(e): #this method tests whether a string is a number.
    try:
        a=int(e)
        return True
    except ValueError:
        return False

restart=""
lower_limit=5
upper_limit=5
win_count=0

while True:
    print("Welcome to The High-Low Game! Be sure to guess integers only; it makes the game easier. For everyone.\n")
    print("1. Weak (number is within range 1-10)")
    print("2. Easy (number is within range 1-100)")
    print("3. Medium (number is within range 1-1000)")
    print("4. Difficult (number is within range 1-100,000)")
    print("5. Custom (choose your range by inputting integers)")    

    difficulty=raw_input("\nChoose your difficulty (1/2/3/4/5): ")

    while is_difficulty(difficulty)!=True:
        difficulty=raw_input("That's not a difficulty level. Please enter a number between 1 and 5: ")

    if int(difficulty)==1:
        lower_limit=1
        upper_limit=10
    if int(difficulty)==2:
        lower_limit=1
        upper_limit=100
    if int(difficulty)==3:
        lower_limit=1
        upper_limit=1000
    if int(difficulty)==4:
        lower_limit=1
        upper_limit=100000
    if int(difficulty)==5:
        lower_limit=raw_input("\nWhat is the lowest number in the range? ")
        lower_limit=int(lower_limit)
        upper_limit=raw_input("What is the highest number in the range? ")
        upper_limit=int(upper_limit)

        while upper_limit<lower_limit:
            print("Your lowest number is higher than your highest number. Try again.")
            lower_limit=raw_input("\nThe lowest number? ")

            while is_number(lower_limit)!=True:
                lower_limit=raw_input("Not a number. Try again: ")
            lower_limit=int(lower_limit)
            
            upper_limit=raw_input("The highest number? ")

            while is_number(upper_limit)!=True:
                upper_limit=raw_input("Not a number. Try again: ")    
            upper_limit=int(upper_limit)

    number=random.randint(lower_limit, upper_limit)

    print("The range is from "+str(lower_limit)+" to "+str(upper_limit)+".\n")

    while True:
        guess=raw_input("Guess a number: ")

        while is_number(guess)!=True:
            guess=raw_input("That's not a number! Guess again: ")

        if int(guess)>number:
            if int(guess)>upper_limit:
                print("WAY too high. Dude, that's above the range.")
            else:
                print("Too high.")
        if int(guess)<number:
            if int(guess)<lower_limit:
                print("WAY too low. Dude, that's below the range.")
            else:
                print("Too low.")
        if int(guess)==number:
            win_count=win_count+1
            print("You got it! The number was "+str(number)+".")
            break
    
    restart=raw_input("\nWould you like to play again? (y/n): ")
    if restart=="y":
        print("")
    else:
        if restart=="n":
            if win_count==1:
                print("You won 1 time. Thanks for playing!")
            else:
                print("You won "+str(win_count)+" times. Thanks for playing!")
            break
        else:
            print("\n...Well, since you didn't type 'y' or 'n', I guess I'll just take it as a no.")
            if win_count==1:
                print("(By the way, you won 1 time. Thanks for playing!)")
            else:
                print("(By the way, you won "+str(win_count)+" times. Thanks for playing!)")
        break
