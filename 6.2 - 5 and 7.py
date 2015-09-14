#Tara Moses
#Assignment 6.2: All Except 5 and 7
#January 29, 2013

#1. Program prints out all numbers between 0 and a user-specified max.
#2. Program omits all multiples of 5 and 7.

print("I'm going to print out all the numbers between zero and another number.")
print("Except I won't print any multiples of 5 or 7. I hate those numbers.")
number=raw_input("What would you like the max number to be? ")

i=0
print("\n0")
while True:
    if (i%5!=0) and (i%7!=0):
        print(i)
    i=i+1
    if i==int(number)+1:
        break

print("\nThere you go! All the numbers between 0 and "+number+" except for multiples of 5 or 7.")
