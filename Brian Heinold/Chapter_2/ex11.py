"""
Write a program that asks the user to enter a number and then prints out the letter A that many times,
all on the same line.
"""

val = eval(input("Insert a value: "))

for i in range(val):
    print("A", end=" ")