#Tara Moses
#Assignment 1: Calculator/ASCII
#January 11, 2013

#1. This program adds, subtracts, multiplies and divides two numbers
#       (integer or decimal) the user chooses.
#2. If the user inputs a non-number character, he or she will be prompted to enter a new number.
#3. The program divides numbers accurately.
#4. The program runs until the user tells it to stop, or when the user inputs a character other than "y" or "n".
#5. The ASCII art is shown when program stops. ASCII art is a cute kitten.

def is_number(s): #this method tests whether a string is numerical. s is a string.
    try:
        a=float(s)
        return True
    except ValueError:
        return False

restart=""

print("I'm going to add, subtract, multiply, and divide some numbers for you today!\n")
    
while True:

    string1=raw_input("A number, please: ")

    while is_number(string1)!=True:
        print("Um... that's not a number, haha. Try again.\n")
        string1=raw_input("A number, please: ")

    string2=raw_input("\nAnother number, if you will: ")

    while is_number(string2)!=True:
        print("Not a number. Try again.\n")
        string2=raw_input("Another number, if you will: ")

    double1=float(string1)
    double2=float(string2)

    sum=str(double1+double2)
    difference=str(double1-double2)
    product=str(double1*double2)
    quotient=str(double1/double2)

    print("\n")
    print(string1+" + "+string2+" = "+sum)
    print(string1+" - "+string2+" = "+difference)
    print(string1+" x "+string2+" = "+product)
    print(string1+" / "+string2+" = "+quotient)
    print("\n")

    restart=raw_input("Thank you! Would you like to input two more numbers? (y/n): ")

    if restart=="y":
        print("\nOkay!\n")
    else:
        if restart!="n":
            print("...I'll take that as a 'no'. Bye!\n")
            print("                      _                        \n                      \`*-.                    \n                       )  _`-.                 \n                      .  : `. .                \n                      : _   '  \               \n                      ; *` _.   `*-._          \n                      `-.-'          `-.       \n                        ;       `       `.     \n                        :.       .        \    \n                        . \  .   :   .-'   .   \n                        '  `+.;  ;  '      :   \n                        :  '  |    ;       ;-. \n                        ; '   : :`-:     _.`* ;\n               [bug] .*' /  .*' ; .*`- +'  `*' \n                     `*-*   `*-*  `*-*'        \n")
            break
        else:
            print("\nAww, okay. Bye!\n")
            print("                      _                        \n                      \`*-.                    \n                       )  _`-.                 \n                      .  : `. .                \n                      : _   '  \               \n                      ; *` _.   `*-._          \n                      `-.-'          `-.       \n                        ;       `       `.     \n                        :.       .        \    \n                        . \  .   :   .-'   .   \n                        '  `+.;  ;  '      :   \n                        :  '  |    ;       ;-. \n                        ; '   : :`-:     _.`* ;\n               [bug] .*' /  .*' ; .*`- +'  `*' \n                     `*-*   `*-*  `*-*'        \n")
            break
