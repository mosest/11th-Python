#Tara Moses
#Assignment 6.1: Fibonacci Sequence
#January 28, 2013

#1. Program prints out a user-specified number of terms
#   of the Fibonacci sequence.
#2. Program prints out the Fibonacci sequence until a
#   user-specified number is passed, in which case the
#   program stops.

print("I am going to print the Fibonacci Sequence for you!\n")
num_terms = int(raw_input("How many terms would you like to print? "))

first=1
second=1

print("\n"+str(first))
print(second)
for i in range(num_terms-2) :
    total=first+second
    print(total)
    first=second
    second=total
    
print("\nHey, I'm now gonna print out the Fibonacci sequence!")
stopping_point=int(raw_input("What number would you like to stop at? "))

first=1
second=1

print("\n"+str(first))
print(second)
total=first+second
while total<=stopping_point:
    total=first+second
    print(total)
    if total>=stopping_point:
        break
    first=second
    second=total

print("\nWell, it's been fun! Goodbye.")
