#!/usr/bin/python 3

import sys
print("This is the name of the program:", sys.argv[0])
print("ArguementList:", str(sys.argv))
name = sys.argv[1]
age = sys.argv[2]

print("Hi " + name + " You are " + age + " years old!")
print(sys.argv[1])
print(sys.argv[2])
