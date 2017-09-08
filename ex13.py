from sys import argv

script, first, second, third = argv

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

input("good job  ")


# RUN: open the cmd,type path> python ex13, arg1, arg2, arg3
#argv: variable list
#unpack argv, then assign the arguments in argv to the variables on the left of "="