#Tara Moses
#Assignment 6.4: First Number Divisible by 1, 2, ..., 16
#January 29, 2013

#1. Program tests whether a number is divisible by all numbers 1-16.
#2. Program outputs first number that satisfies conditions.

print("I'll print the first number that is divisible by every number")
print("from 1 to 16.")

num_to_find=700000.0

count=1

while True:
    if (num_to_find%16==0):
        if (num_to_find%15==0):
            if (num_to_find%14==0):
                if (num_to_find%13==0):
                    if (num_to_find%12==0):
                        if (num_to_find%11==0):
                            if (num_to_find%10==0):
                                if (num_to_find%9==0):
                                    print(str(num_to_find)+" is the smallest number divisible by 1-16. Yay!")
                                    break
                                else:
                                    print("Nope! It stopped at 9.")
                                    num_to_find=num_to_find+1.0
                            else:   
                                print("Nope! It stopped at 10.")
                                num_to_find=num_to_find+1.0
                        else:
                            print("Nope! It stopped at 11.")
                            num_to_find=num_to_find+1.0
                    else:
                        print("Nope! It stopped at 12.")
                        num_to_find=num_to_find+1.0
                else:
                    print("Nope! It stopped at 13.")
                    num_to_find=num_to_find+1.0
            else:
                print("Nope! It stopped at 14.")
                num_to_find=num_to_find+1.0
        else:
            print("Nope! It stopped at 15.")
            num_to_find=num_to_find+1.0
    else:
        print("Well, it's not "+str(num_to_find)+"!")
        num_to_find=num_to_find+1.0
        
