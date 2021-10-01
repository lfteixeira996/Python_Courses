"""
Write a program that generates two random numbers from 1 to 10, and prints out the two numbers
and their sum.
"""
import random

val1 = random.randint(1, 10)
val2 = random.randint(1, 10)

print(val1, val2, (val1+val2))
