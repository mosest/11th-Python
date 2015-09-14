#Tara Moses
#Assignment 10: Hangman
#February 12, 2013

#1. Program runs through a game of Hangman with the user.
#2. Program plays rounds until the user says to stop.
#3. Program uses a cheerleader rather than a man to kill. :)

import urllib,random

def draw_man(count):
    if count==0:
        print("FIRST STRIKE: HER HEAD")
        print("-----|\n|    O\n|       \n|      \n|\n-------")
    elif count==1:
        print("SECOND STRIKE: HER BODY")
        print("-----|\n|    O\n|    |  \n|      \n|\n-------")
    elif count==2:
        print("THIRD STRIKE: HER LEG")
        print("-----|\n|    O\n|    |  \n|     \\\n|\n-------")
    elif count==3:
        print("FOURTH STRIKE: HER OTHER LEG")
        print("-----|\n|    O\n|    |  \n|   / \\\n|\n-------")
    elif count==4:
        print("FIFTH STRIKE: HER ARM")
        print("-----|\n|    O\n|  *-|  \n|   / \\\n|\n-------")
    elif count==5:
        print("SIXTH STRIKE: HER OTHER ARM")
        print("-----|\n|    O\n|  *-|-*\n|   / \\\n|\n-------")

def word_is_guessed(word,used_letters):
    count=0
    for letter in word:
        if letter in used_letters:
            count+=1
        else:
            pass
        
    if count==len(word):
        return True
    else:
        return False

def get_word(words):
    random_number=random.randint(0,len(words)-1)
    word=words[random_number].lower()
    return word

def masked_word(word,used_letters):
    string=""
    for character in word:
        if character in used_letters:
            string+=character
        else:
            string+=" _ "
    string=string.replace("  "," ")
    return string+"\n"

wordFile=urllib.urlopen("http://projecteuler.net/project/words.txt")
list_of_words=wordFile.readline()
list_of_words=list_of_words.replace("\"", "")
list_of_words=list_of_words.split(",")

while True:
    word_to_guess=get_word(list_of_words)
    wrong_guesses=0
    used_letters=""

    print("Welcome to a new round of \"Guess The Word or Kill The Cheerleader\"! You will have six chances to save her. \n")
    print("-----|\n|     \n|       \n|      \n|\n-------")

    while wrong_guesses<6 and word_is_guessed(word_to_guess,used_letters)!=True:
        print(masked_word(word_to_guess,used_letters))
        current_guess=raw_input("Guess a letter: ").lower()
        used_letters+=current_guess
        if current_guess in word_to_guess:
            pass
        else:
            print("Sorry, there is no "+current_guess+".")
            draw_man(wrong_guesses)
            wrong_guesses=wrong_guesses+1

    if wrong_guesses==6:
        print("You lose. The word was \""+word_to_guess+"\", and now your cheerleader is dead. So I guess you did win, in a sense.")

    if word_is_guessed(word_to_guess,used_letters):
        print("You win! The word was \""+word_to_guess+"\"! Your cheerleader is saved.")

    again=raw_input("Would you like to play again? (y/n): ")
    if again.lower()!="y":
        break
