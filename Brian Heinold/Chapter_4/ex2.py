"""
Write a program that asks the user to enter a number. If the number is negative, print out a message
telling them they can’t enter a negative. Otherwise print out the square root of that number.
"""
from math import sqrt

val = eval(input("Insert a value: "))

if val < 0:
    print("You can't insert negative values")

else:
    print(f"sqrt({val}) = {sqrt(val)}")