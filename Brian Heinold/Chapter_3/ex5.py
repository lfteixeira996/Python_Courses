"""
Write a program that asks the user to enter a positive number and then prints out the square root of
that number rounded to 2 decimal places.
"""
import math

n = eval(input("Positive Number: "))

print("Square root: ", "{:.2f}".format(math.sqrt(n)))

#or

print("Square root: ", round(math.sqrt(n), 2))
