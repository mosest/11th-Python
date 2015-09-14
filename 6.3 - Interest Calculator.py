#Tara Moses
#Assignment 6.3: Interest Calculator
#January 29, 2013

#1. Program asks user for initial investment,
#   goal amount, and interest rate.
#2. Program calculates approximately how many
#   years until the goal amount is reached.
#3. Program outputs the number of years.

initial=float(raw_input("Initial investment (in $USD): "))
goal=float(raw_input("Goal amount (in $USD): "))
interest=float(raw_input("Interest rate (percentage, not decimal): "))

print("\n")

years_to_double=72/interest
i=1
total=initial
while (total<=goal):
    years=i*years_to_double
    total=2*total
    print("After "+str(years)+" years, your total will be $"+str(total)+".")
    i=i+1

print("\nThere you go! You'll reach your goal in "+str(years)+" years. See you later.")
