# Python script to demonstrate command line arguments

import sys

# `sys.argv` is a list of command line arguments 
n = len(sys.argv)   # number of command line arguments.
print("Total arguments passed:", n)
 
print("\nName of Python script:", sys.argv[0]) #name of the current Python script. 
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# add command line arguments and print result
sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])
     
print("\n\nResult:", sum)