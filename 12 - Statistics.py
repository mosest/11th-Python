#Tara Moses
#Assignment 12: Statistics
#March 5, 2013

#1. program does things

import math

def find_stddev(list, average):
    sigma=0
    for number in list:
        sigma+=(number-average*1.0)**2
    standard_deviation=(sigma/(len(my_numbers)*1.0))
    return math.sqrt(standard_deviation)

def find_mode(list):
    list.sort()
    mode=list[0]
    for i in list:
        if list.count(i)>mode:
            mode=i
    return mode

default="numbers.txt"
print("This program will statistically analyze a set of data for you.")
file_name=raw_input("Enter a file name such as file.txt, or press enter to read from the default file: ")
if file_name=="":
    file_name=default
    
my_file=file(file_name)
my_numbers=[]

for line in my_file:
    num=int(line.strip())
    my_numbers.append(num)

count=len(my_numbers)
mode=find_mode(my_numbers)
median=my_numbers[len(my_numbers)/2]
minimum=min(my_numbers)
maximum=max(my_numbers)
mean=(sum(my_numbers)*1.0)/len(my_numbers)
standard_deviation=find_stddev(my_numbers, mean)

output_file=file("output.txt","w")
output_file.write("Count: "+str(count)+"\n")
output_file.write("Mode: "+str(mode)+"\n")
output_file.write("Median: "+str(median)+"\n")
output_file.write("Min: "+str(minimum)+"\n")
output_file.write("Max: "+str(maximum)+"\n")
output_file.write("Mean: "+str(mean)+"\n")
output_file.write("Standard Deviation: "+str(standard_deviation)+"\n")
output_file.close()

print("Please open output.txt to see statistics for this data set. Additionally, you can see your statistics printed in the Python shell. ")
print_data=raw_input("Would you like to print your statistics? (y/n): ")
if print_data=="y" or print_data=="Y":
    print("Count: "+str(count)+"\n")
    print("Mode: "+str(mode)+"\n")
    print("Median: "+str(median)+"\n")
    print("Min: "+str(minimum)+"\n")
    print("Max: "+str(maximum)+"\n")
    print("Mean: "+str(mean)+"\n")
    print("Standard Deviation: "+str(standard_deviation)+"\n")
else:
    pass
